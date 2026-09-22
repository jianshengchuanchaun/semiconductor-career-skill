"""Validate v1.1 evidence boundaries and optional Office structure without network calls."""
from pathlib import Path
from urllib.parse import urlparse
import argparse
import datetime as dt
from decimal import Decimal
import json
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.1.0'
WORD_REL = f'docs/半导体研究生就业规划手册_我的模拟电路世界_v{VERSION}.docx'
PPT_REL = f'presentations/半导体研一就业规划_10分钟推广_我的模拟电路世界_v{VERSION}.pptx'
EXPECTED_IDS = {'F1', 'F2', 'F3', 'C1', 'C2', 'C3'}
TYPES = {'required', 'preferred', 'explicit'}
HOSTS = {'F1': 'nxp.wd3.myworkdayjobs.com', 'F2': 'jobs.renesas.com',
         'F3': 'jobs.nvidia.com', 'C1': 'www.chipown.com.cn',
         'C2': 'telink.zhiye.com', 'C3': 'www.sg-micro.com'}
COMPANY_TERMS = [('NXP', '恩智浦'), ('Renesas', '瑞萨'), ('NVIDIA', '英伟达'),
                 ('Chipown', '芯朋'), ('Telink', '泰凌'), ('SGMICRO', '圣邦')]


def nonempty(value):
    return isinstance(value, (str, list, dict)) and bool(value)


def xml_text(data):
    return '\n'.join(node.text or '' for node in ET.fromstring(data).iter()
                     if node.tag.rsplit('}', 1)[-1] == 't')


def office_check(path, kind, errors):
    details = {'file': path.relative_to(ROOT).as_posix(), 'checked': False}
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                errors.append(f'Corrupt Office member: {path.name}/{bad}')
                return details
            members = archive.namelist()
            if kind == 'word':
                text = xml_text(archive.read('word/document.xml'))
                if VERSION not in text:
                    errors.append('Latest Word body does not identify v1.1.0')
                details['page_count_verified'] = False
            else:
                slides = sorted(n for n in members if re.fullmatch(r'ppt/slides/slide\d+\.xml', n))
                notes = sorted(n for n in members if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', n))
                details['slides'] = len(slides)
                details['notes'] = len(notes)
                if len(slides) != 12:
                    errors.append(f'PPT must have 12 slides, got {len(slides)}')
                if len(notes) != len(slides):
                    errors.append('Every PPT slide needs speaker notes')
                note_texts = [xml_text(archive.read(n)) for n in notes]
                for n, note in zip(notes, note_texts):
                    if len(re.sub(r'\s', '', note)) < 60:
                        errors.append(f'PPT speaker note too short for a useful talk: {n}')
                text = '\n'.join(xml_text(archive.read(n)) for n in slides) + '\n' + '\n'.join(note_texts)
                details['speaker_notes_have_sources'] = sum(host in text for host in HOSTS.values())
                if details['speaker_notes_have_sources'] < 6:
                    errors.append('PPT slides/notes must preserve all 6 direct source URLs')
            for aliases in COMPANY_TERMS:
                if not any(term.casefold() in text.casefold() for term in aliases):
                    errors.append(f'{kind} does not mention enterprise sample {aliases[0]}')
            details['checked'] = True
            details['scope'] = 'ZIP/XML/text structure only; rendering must be separately inspected.'
    except (OSError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        errors.append(f'{kind} cannot be inspected: {exc}')
    return details


def validate_v11(require_artifacts=False):
    errors, samples = [], []
    for category in ['foreign', 'domestic']:
        path = ROOT / f'docs/research-{category}-jobs.json'
        try:
            part = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f'Cannot read {path.name}: {exc}')
            continue
        if not isinstance(part, list) or len(part) != 3:
            errors.append(f'{path.name} must contain three samples')
            continue
        for row in part:
            if row.get('category') != category:
                errors.append(f'{row.get("id")} category mismatch')
        samples.extend(part)
    ids = [row.get('id') for row in samples]
    if set(ids) != EXPECTED_IDS or len(ids) != 6:
        errors.append(f'Expected six distinct sample IDs {sorted(EXPECTED_IDS)}; got {ids}')
    type_counts = {key: 0 for key in TYPES}
    for row in samples:
        sid = row.get('id', '?')
        for key in ['company', 'title', 'location', 'career_stage', 'checked_date', 'url',
                    'status', 'requirements', 'teaching_mapping', 'limits', 'source_evidence']:
            if not nonempty(row.get(key)):
                errors.append(f'{sid} missing {key}')
        if 'posting_date' not in row:
            errors.append(f'{sid} must explicitly retain posting_date, using null when unknown')
        try:
            dt.date.fromisoformat(row.get('checked_date', ''))
        except (ValueError, TypeError):
            errors.append(f'{sid} checked_date must be YYYY-MM-DD')
        parsed = urlparse(row.get('url', ''))
        if parsed.scheme != 'https' or parsed.hostname != HOSTS.get(sid):
            errors.append(f'{sid} URL differs from audited official host; re-audit before changing')
        for item in row.get('requirements', []):
            typ = item.get('evidence_type')
            if typ not in TYPES:
                errors.append(f'{sid} invalid requirement type {typ}; use required/preferred/explicit')
            else:
                type_counts[typ] += 1
            if not item.get('skill') or not item.get('paraphrase'):
                errors.append(f'{sid} requirement lacks skill or source paraphrase')
        for item in row.get('teaching_mapping', []):
            if not all(item.get(key) for key in ['skill', 'learning_task', 'evidence']):
                errors.append(f'{sid} incomplete teaching mapping')
            if '教学建议' not in item.get('learning_task', ''):
                errors.append(f'{sid} learning task must be identified as teaching inference')
        status = row.get('status', '')
        stage = row.get('career_stage', '')
        if sid in {'F1', 'F3'} and not ('索引' in status and ('未核实' in status or '未确认' in status)):
            errors.append(f'{sid} dynamic-page/index-only status must retain uncertainty')
        if sid == 'F2' and '过期' not in status:
            errors.append('F2 historical Renesas sample must retain expired status')
        if sid == 'F3':
            formal_required = [item for item in row.get('requirements', [])
                               if item.get('evidence_type') == 'required'
                               and '形式验证' in item.get('skill', '')]
            if not any('SVA' in item.get('paraphrase', '') for item in formal_required):
                errors.append('F3 must preserve SVA context in the separately required formal-verification item')
        if sid == 'C3' and not ('社会招聘' in stage and '3年' in stage and '成长' in stage):
            errors.append('C3 senior sample must retain social recruiting, 3 years, growth-reference boundary')
    if not all(type_counts.values()):
        errors.append('Corpus must distinguish required skills, preferred skills and duties')

    combined_path = ROOT / 'skills/semiconductor-career-planner/references/company-examples.json'
    try:
        library = json.loads(combined_path.read_text(encoding='utf-8'))
        indexed = {row['id']: row for row in library}
        if set(indexed) != EXPECTED_IDS or len(library) != 6:
            errors.append('Packaged company library must preserve all six distinct samples')
        for original in samples:
            packaged = indexed.get(original['id'], {})
            if any(packaged.get(key) != value for key, value in original.items()):
                errors.append(f'Packaged {original["id"]} differs from reviewed source fields')
            if packaged.get('currently_open_verified') is not False:
                errors.append(f'Packaged {original["id"]} must retain unverified current application status')
            if not packaged.get('evidence_access') or not packaged.get('teaching_mapping_origin'):
                errors.append(f'Packaged {original["id"]} lacks access/inference boundary metadata')
    except (OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
        errors.append(f'Cannot verify packaged company evidence: {exc}')
    for rel in ['skills/semiconductor-career-planner/references/company-examples.md',
                'examples/company-to-plan.md']:
        if not (ROOT / rel).is_file():
            errors.append(f'Missing published company guide/case: {rel}')

    talk_result = {'checked': False}
    talk_path = ROOT / 'presentations/talk-content.json'
    try:
        talk = json.loads(talk_path.read_text(encoding='utf-8'))
        slides = talk['slides']
        seconds = sum(slide['seconds'] for slide in slides)
        if len(slides) != 12 or seconds != 600:
            errors.append(f'Talk must be 12 slides / 600 planned seconds; got {len(slides)} / {seconds}')
        if talk.get('version') != VERSION:
            errors.append(f'Talk source must identify version {VERSION}')
        if not all(slide.get('notes') and slide.get('sources') for slide in slides):
            errors.append('Every talk source slide must have narrative notes and source/boundary notes')
        budget = next(slide for slide in slides if slide['kind'] == 'budget')['table'][1:]
        numbers = [Decimal(re.search(r'\d+(?:\.\d+)?', row[1]).group(0)) for row in budget]
        task_sum = sum(numbers[:-2])
        scheduled, buffer = numbers[-2:]
        if task_sum != scheduled or scheduled != Decimal('9.6') or buffer != Decimal('2.4'):
            errors.append('Talk budget must add task rows to 9.6 h plus 2.4 h buffer')
        if scheduled + buffer != Decimal('12'):
            errors.append('Talk task budget and buffer must total 12 h')
        talk_result = {'checked': True, 'slides': len(slides), 'planned_seconds': seconds,
                       'task_rows_sum_hours': str(task_sum), 'scheduled_hours': str(scheduled),
                       'buffer_hours': str(buffer), 'total_hours': str(scheduled + buffer),
                       'scope': 'Planned timing and source-table arithmetic, not a live rehearsal.'}
    except (OSError, json.JSONDecodeError, KeyError, TypeError, StopIteration, AttributeError) as exc:
        errors.append(f'Cannot verify talk timing/budget source: {exc}')

    ref = ROOT / 'skills/semiconductor-career-planner/references'
    analog = (ref / 'roles-analog-process.md').read_text(encoding='utf-8')
    digital = (ref / 'roles-digital.md').read_text(encoding='utf-8')
    learning = (ref / 'learning-and-evidence.md').read_text(encoding='utf-8')
    for needle in ['P0：岗位基本门槛', '报告至少一个 nominal 通过而其他条件失败的实例',
                   '作品集必须有一个反直觉趋势', '一个失败 corner、设计改动']:
        if needle in analog:
            errors.append(f'Uncorrected audit issue in analog reference: {needle}')
    if '目标是一周到两周内跑通一个完整问题' in learning:
        errors.append('Minimum project duration must be budget-dependent or explicitly limited to a micro-task')
    if '至少有一个失败案例和一次有原因的修改' in learning:
        errors.append('Core learning project must accept truthful all-pass results and label teaching faults')
    current_teaching = '\n'.join(p.read_text(encoding='utf-8')
                                 for p in (ROOT / 'skills/semiconductor-career-planner').rglob('*')
                                 if p.suffix in {'.md', '.json'})
    for needle in ['修复至少两类真实错误', '至少一个真实拥塞 / 时序问题的修复',
                   '发现并修复的一项真实缺陷。', '一个失败设计的修正记录。',
                   '一个最有价值的失败：']:
        if needle in current_teaching:
            errors.append(f'Teaching material still mandates observed failure: {needle}')
    if '至少 5 个有效缺陷案例或明确标注的故障注入案例' in digital:
        errors.append('DV core count still conflicts with 3-class manual criterion')
    if 'ΔT=T_hot−T_amb' not in analog or 'P_in−P_out' not in analog:
        errors.append('Thermal acceptance must specify temperature-rise and power-balance definitions')
    manual_path = ROOT / 'docs/manual-content.json'
    try:
        manual = json.loads(manual_path.read_text(encoding='utf-8'))
        if manual.get('version') != VERSION:
            errors.append(f'manual-content.json version must be {VERSION}')
        combined = json.dumps(manual, ensure_ascii=False)
        for needle in ['每周十二至十五小时', '预计每周投入十二至十五小时',
                       '作品集需有一个反直觉结果', '网格加密后热点温度变化小于百分之三']:
            if needle in combined:
                errors.append(f'Uncorrected audit issue in manual: {needle}')
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f'Cannot inspect manual content: {exc}')

    artifacts = []
    for rel, kind in [(WORD_REL, 'word'), (PPT_REL, 'ppt')]:
        path = ROOT / rel
        if path.is_file():
            artifacts.append(office_check(path, kind, errors))
        else:
            artifacts.append({'file': rel, 'checked': False, 'status': 'not yet produced'})
            if require_artifacts:
                errors.append(f'Required final artifact missing: {rel}')
    return {'passed': not errors, 'samples': len(samples), 'required_plus_duties_counts': type_counts,
            'talk_source': talk_result,
            'artifacts_required': require_artifacts, 'artifacts': artifacts, 'errors': errors,
            'scope': 'Static schema and editorial regressions; official source truth and Office visual '
                     'quality require independent evidence. This script does not execute behavioral evaluations.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-artifacts', action='store_true')
    args = parser.parse_args()
    result = validate_v11(require_artifacts=args.require_artifacts)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)

