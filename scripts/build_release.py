"""Build v1.1 adapters and source archive without Office deliverables.

Run --list-source for a read-only packaging manifest. Old releases remain untouched.
Word/PPT/PDF are separate attachments and are not required to build source.
"""
from pathlib import Path
import argparse
import hashlib
import json
import posixpath
import re
from urllib.parse import unquote
import zipfile
from validate_release import validate
from validate_v11_evidence import WORD_REL, PPT_REL

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'semiconductor-career-planner'
OUT = ROOT / 'release'
VERSION = '1.1.0'
NAME = 'semiconductor-career-planner'
STAMP = (2026, 9, 22, 0, 0, 0)
EXCLUDED_DIRS = {'.git', '.qa', '__pycache__', 'evaluation-workspace', 'career-plan',
                 'node_modules', '.venv', 'venv', 'tmp', 'temp'}
PLATFORM_NAMES = {f'{NAME}-{platform}-v{VERSION}.zip' for platform in ['codex', 'workbuddy']}
FINAL_OFFICE = {WORD_REL, PPT_REL}
EXCLUDED_DOCUMENT_EXTENSIONS = {'.doc', '.docx', '.docm', '.ppt', '.pptx', '.pptm', '.pdf'}
OPTIONAL_PDF = {Path(WORD_REL).with_suffix('.pdf').as_posix(),
                Path(PPT_REL).with_suffix('.pdf').as_posix()}


def include_source(rel):
    """Use explicit version and artifact boundaries rather than archive everything."""
    if EXCLUDED_DIRS.intersection(rel.parts):
        return False
    if rel.name.startswith(('~$', '.~')) or rel.suffix.lower() in {'.pyc', '.tmp', '.bak'}:
        return False
    if rel.name in {'.DS_Store', 'Thumbs.db'} or rel.name.startswith('SHA256SUMS'):
        return False
    if '-source-v' in rel.name or 'v1.0.0' in rel.name:
        return False
    if rel.parts[0] == 'release':
        return rel.name in PLATFORM_NAMES
    if rel.suffix.lower() in EXCLUDED_DOCUMENT_EXTENSIONS:
        return False
    if re.search(r'(?:^|[-_.])(candidate|draft|preview)(?:[-_.]|$)', rel.name, re.I):
        return False
    return True


def source_members(adapter_overrides=None):
    overrides = adapter_overrides or {}
    members = {}
    for p in sorted(ROOT.rglob('*')):
        if p.is_file():
            rel = p.relative_to(ROOT)
            if include_source(rel):
                members[rel.as_posix()] = overrides.get(rel.as_posix(), p)
    # First build has no current platform archives in release yet.
    members.update(overrides)
    return sorted(members.items())


def write_member(zf, name, data):
    info = zipfile.ZipInfo(name, date_time=STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zf.writestr(info, data)


def check_source_links(members):
    """Links must resolve inside the published source, not only in the work folder."""
    names = {rel for rel, _ in members}
    errors = []
    for rel, path in members:
        if path.suffix != '.md':
            continue
        for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if re.match(r'^(?:[a-z][a-z0-9+.-]*:|#)', dest, re.I):
                continue
            target = unquote(dest.strip('<>').split('#')[0])
            if not target:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), target))
            if resolved not in names and not any(n.startswith(resolved.rstrip('/') + '/') for n in names):
                errors.append(f'{rel} -> {dest}')
    if errors:
        raise RuntimeError('Unresolved links after source filtering: ' + '; '.join(errors))


def check_adapter(path, platform, files, core, body):
    with zipfile.ZipFile(path) as zf:
        if zf.testzip() is not None:
            raise RuntimeError(f'Corrupt archive {path.name}')
        prefix = f'{NAME}/' if platform == 'codex' else ''
        expected = {prefix + p.relative_to(SKILL).as_posix() for p in files} | {prefix + 'LICENSE'}
        if set(zf.namelist()) != expected:
            raise RuntimeError(f'Adapter file set drift: {platform}')
        actual = zf.read(prefix + 'SKILL.md').decode('utf-8')
        if actual.split('---', 2)[2] != body:
            raise RuntimeError(f'Adapter body drift: {platform}')
        if platform == 'codex' and actual != core:
            raise RuntimeError('Codex core bytes drift')
        if platform == 'workbuddy' and f'version: {VERSION}' not in actual:
            raise RuntimeError('WorkBuddy version mismatch')
        for p in files:
            rel = p.relative_to(SKILL).as_posix()
            if rel != 'SKILL.md' and zf.read(prefix + rel) != p.read_bytes():
                raise RuntimeError(f'Adapter reference bytes drift: {platform}/{rel}')


def old_release_hashes():
    files = list(OUT.glob('*v1.0.0*'))
    old_word = ROOT / 'docs/半导体研究生就业规划手册_我的模拟电路世界_v1.0.0.docx'
    if old_word.is_file():
        files.append(old_word)
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list-source', action='store_true', help='Print manifest only; do not build.')
    args = parser.parse_args()
    if args.list_source:
        entries = [rel for rel, _ in source_members()]
        print(json.dumps({'version': VERSION, 'source_files': entries,
                          'planned_adapters': sorted('release/' + n for n in PLATFORM_NAMES)},
                         ensure_ascii=False, indent=2))
        return
    check = validate(require_artifacts=False)
    if not check['passed']:
        raise SystemExit(json.dumps(check, ensure_ascii=False, indent=2))
    preserved = old_release_hashes()
    OUT.mkdir(exist_ok=True)
    stage = ROOT / '.qa' / f'release-stage-v{VERSION}'
    stage.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SKILL.rglob('*') if p.is_file()
                   and not EXCLUDED_DIRS.intersection(p.relative_to(SKILL).parts)
                   and not p.name.startswith('~$') and p.suffix != '.pyc')
    core = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    body = core.split('---', 2)[2]
    zh = '面向半导体研究生的岗位能力规划，先明确技能，再诊断、拆解学习与项目、验收和求职复盘。'
    en = 'Plan semiconductor graduate careers from target job skills through diagnosis, learning tasks, projects, evidence and recruiting preparation.'
    wb = '\n'.join(['---', f'name: {NAME}', f'description: {json.dumps(zh, ensure_ascii=False)}',
                    f'description_zh: {json.dumps(zh, ensure_ascii=False)}',
                    f'description_en: {json.dumps(en)}', f'version: {VERSION}',
                    'author: 我的模拟电路世界', '---']) + body
    staged = []
    overrides = {}
    for platform in ['codex', 'workbuddy']:
        path = stage / f'{NAME}-{platform}-v{VERSION}.zip'
        with zipfile.ZipFile(path, 'w') as zf:
            for p in files:
                rel = p.relative_to(SKILL).as_posix()
                name = f'{NAME}/{rel}' if platform == 'codex' else rel
                data = wb.encode('utf-8') if platform == 'workbuddy' and rel == 'SKILL.md' else p.read_bytes()
                write_member(zf, name, data)
            license_name = f'{NAME}/LICENSE' if platform == 'codex' else 'LICENSE'
            write_member(zf, license_name, (ROOT / 'LICENSE').read_bytes())
        check_adapter(path, platform, files, core, body)
        staged.append(path)
        overrides['release/' + path.name] = path
    members = source_members(overrides)
    member_names = {rel for rel, _ in members}
    required = set(overrides) | {
        'docs/research-foreign-jobs.json', 'docs/research-domestic-jobs.json',
        'docs/research-foreign-jobs.md', 'docs/research-domestic-jobs.md',
        'presentations/talk-content.json', 'scripts/build_release.py',
        'scripts/validate_v11_evidence.py'}
    if not required <= member_names:
        raise RuntimeError(f'Source missing required deliverables: {sorted(required - member_names)}')
    check_source_links(members)
    source = stage / f'{NAME}-source-v{VERSION}.zip'
    with zipfile.ZipFile(source, 'w') as zf:
        for rel, p in members:
            write_member(zf, f'semiconductor-career-skill/{rel}', p.read_bytes())
    with zipfile.ZipFile(source) as zf:
        if zf.testzip() is not None:
            raise RuntimeError('Corrupt source archive')
        if len(zf.namelist()) != len(set(zf.namelist())):
            raise RuntimeError('Duplicate source archive members')
        if any(not include_source(Path(n).relative_to('semiconductor-career-skill'))
               for n in zf.namelist()):
            raise RuntimeError('Source archive contains excluded files')
    staged.append(source)
    for path in staged:
        path.replace(OUT / path.name)
    deliverables = [OUT / p.name for p in staged]
    deliverables += [ROOT / rel for rel in sorted(FINAL_OFFICE) if (ROOT / rel).is_file()]
    deliverables += [ROOT / rel for rel in sorted(OPTIONAL_PDF) if (ROOT / rel).is_file()]
    checksums = [f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}'
                 for p in sorted(deliverables)]
    sums = OUT / f'SHA256SUMS-v{VERSION}.txt'
    sums.write_text('\n'.join(checksums) + '\n', encoding='utf-8')
    after = old_release_hashes()
    if preserved != after:
        raise RuntimeError('Old v1.0 artifact hashes changed')
    result = {'version': VERSION, 'archives': [p.name for p in staged], 'skill_files': len(files),
              'adapter_body_equal': True, 'adapter_references_byte_equal': True,
              'source_files': len(members), 'source_crc_passed': True,
              'source_office_or_pdf_files': 0,
              'old_v1_0_artifacts_preserved': len(preserved), 'checksums': sums.name,
              'scope': 'Source and adapter archive checks; Office/PDF deliverables are excluded from source and only hashed separately when present. Client import and visual QA remain separate.'}
    (ROOT / '.qa' / f'release-v{VERSION}-report.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

