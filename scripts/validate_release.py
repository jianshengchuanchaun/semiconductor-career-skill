"""Structural checks; these do not validate clients or engineering results."""
from pathlib import Path
import argparse
import json
import re
from urllib.parse import unquote
from validate_v11_evidence import validate_v11

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'semiconductor-career-planner'
VERSION = '1.1.0'
SKIP_DIRS = {'.qa', 'evaluation-workspace', '.git', '__pycache__', 'career-plan'}


def validate(require_artifacts=False):
    errors = []
    required = ['README.md', 'LICENSE', 'docs/INSTALL.md', 'docs/platform-sources.md',
                'docs/BILIBILI.md', 'docs/RELEASE.md', 'evals/evals.json',
                'docs/research-foreign-jobs.json', 'docs/research-foreign-jobs.md',
                'docs/research-domestic-jobs.json', 'docs/research-domestic-jobs.md',
                'docs/QA-v1.1.md']
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append(f'Missing {rel}')
    for rel in ['SKILL.md', 'references/planning-method.md', 'references/output-contract.md',
                'references/role-selection.md', 'references/roles-digital.md',
                'references/resources-digital.md', 'references/roles-analog-process.md',
                'references/resources-analog-process.md', 'references/learning-and-evidence.md',
                'references/review-and-recruiting.md']:
        if not (SKILL / rel).is_file():
            errors.append(f'Missing skill file {rel}')
    entry_path = SKILL / 'SKILL.md'
    entry = entry_path.read_text(encoding='utf-8') if entry_path.is_file() else ''
    if not entry.startswith('---\n'):
        errors.append('Missing YAML frontmatter')
    for key in ['name', 'description']:
        if not re.search(rf'^{key}:\s+\S', entry, re.M):
            errors.append(f'Missing {key}')
    if not re.search(rf'^\s+version:\s*{re.escape(VERSION)}\s*$', entry, re.M):
        errors.append(f'Core metadata version must be {VERSION}')
    if len(entry.splitlines()) >= 500:
        errors.append('Core exceeds progressive disclosure line budget')
    for rel in re.findall(r'\x60((?:references|templates)/[^\x60]+\.md)\x60', entry):
        if not (SKILL / rel).is_file():
            errors.append(f'Broken core reference {rel}')
    md_count = 0
    for p in ROOT.rglob('*.md'):
        if SKIP_DIRS.intersection(p.relative_to(ROOT).parts):
            continue
        md_count += 1
        content = p.read_text(encoding='utf-8')
        if '\ufffd' in content:
            errors.append(f'Replacement character in {p.relative_to(ROOT)}')
        for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'^(?:[a-z][a-z0-9+.-]*:|#)', dest, re.I):
                continue
            target = unquote(dest.strip('<>').split('#')[0])
            if target and not (p.parent / target).exists():
                errors.append(f'Broken relative link {p.relative_to(ROOT)} -> {dest}')
    eval_path = ROOT / 'evals/evals.json'
    data = json.loads(eval_path.read_text(encoding='utf-8')) if eval_path.is_file() else {'evals': []}
    if len(data['evals']) < 3:
        errors.append('Need three behavioral cases')
    for case in data['evals']:
        if not case.get('assertions'):
            errors.append(f'No assertions in eval {case.get("id")}')
    analog = (SKILL / 'references/roles-analog-process.md').read_text(encoding='utf-8')
    digital = (SKILL / 'references/roles-digital.md').read_text(encoding='utf-8')
    if len(re.findall(r'^## A[1-7]\.', analog, re.M)) != 7:
        errors.append('Analog route count != 7')
    if len(re.findall(r'^## [1-6]\. ', digital, re.M)) != 6:
        errors.append('Digital route count != 6')
    templates = list((SKILL / 'templates').glob('*.md'))
    if len(templates) != 9:
        errors.append(f'Template count {len(templates)} != 9')
    v11 = validate_v11(require_artifacts=require_artifacts)
    errors.extend(v11['errors'])
    return {'passed': not errors, 'version': VERSION, 'markdown_files': md_count,
            'role_routes': 13, 'templates': len(templates), 'eval_cases': len(data['evals']),
            'core_lines': len(entry.splitlines()), 'v11': v11, 'errors': errors,
            'scope': 'Files, references, evidence schema and optional Office structure. '
                     'No fresh source browsing, client import, student experiment or visual approval.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-artifacts', action='store_true',
                        help='Require latest Word and 12-slide PPTX, including speaker notes.')
    args = parser.parse_args()
    result = validate(require_artifacts=args.require_artifacts)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)

