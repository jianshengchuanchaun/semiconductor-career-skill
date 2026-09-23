"""Check operational inventory and evidence parity; not a translation-quality score."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
VERSION='1.2.0'
NAMES={'zh':'semiconductor-career-planner','en':'semiconductor-career-planner-en'}

def inventory(folder):
    return {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and p.suffix in {'.md','.json'}}

def urls(text):
    return set(re.findall(r'https?://[^\s<>\]\)"\x60]+',text))

def schema(value):
    if isinstance(value,dict):
        return {key:schema(item) for key,item in value.items()}
    if isinstance(value,list):
        return [schema(item) for item in value]
    return type(value).__name__

def validate_bilingual():
    errors=[]
    roots={lang:ROOT/'skills'/name for lang,name in NAMES.items()}
    inventories={lang:inventory(folder) for lang,folder in roots.items()}
    if inventories['zh']!=inventories['en']:
        errors.append('Language file inventories differ: '+str(sorted(inventories['zh']^inventories['en'])))
    summaries={}
    for lang,folder in roots.items():
        core=folder/'SKILL.md'
        if not core.exists():
            errors.append(f'{lang}: missing entrypoint');continue
        text=core.read_text(encoding='utf-8')
        for pattern,label in [(rf'^name: {NAMES[lang]}$', 'skill name'),(rf'^  version: {VERSION}$','version'),(rf'^  language: {"zh-CN" if lang=="zh" else "en"}$','language')]:
            if not re.search(pattern,text,re.M):errors.append(f'{lang}: wrong {label}')
        if len(text.splitlines())>=500:errors.append(f'{lang}: oversized entrypoint')
        for rel in re.findall(r'\x60((?:references|templates)/[^\x60]+\.(?:md|json))\x60',text):
            if not (folder/rel).is_file():errors.append(f'{lang}: broken reference {rel}')
        try:
            analog=(folder/'references/roles-analog-process.md').read_text(encoding='utf-8')
            digital=(folder/'references/roles-digital.md').read_text(encoding='utf-8')
            counts=[len(re.findall(r'^## A[1-7]\.',analog,re.M)),len(re.findall(r'^## [1-6]\. ',digital,re.M))]
            if counts!=[7,6]:errors.append(f'{lang}: expected 7 analog/industry and 6 digital routes, found {counts}')
            templates=len(list((folder/'templates').glob('*.md')))
            if templates!=9:errors.append(f'{lang}: expected 9 templates, found {templates}')
            summaries[lang]={'files':len(inventories[lang]),'routes':sum(counts),'templates':templates,'skill_name':NAMES[lang]}
        except OSError as exc:errors.append(str(exc))
    for rel in inventories['zh']&inventories['en']:
        if rel.startswith('references/') and rel.endswith('.md'):
            zh=(roots['zh']/rel).read_text(encoding='utf-8')
            en=(roots['en']/rel).read_text(encoding='utf-8')
            if urls(zh)!=urls(en):errors.append(f'External URLs differ in {rel}: {sorted(urls(zh)^urls(en))}')
    try:
        zh=json.loads((roots['zh']/'references/company-examples.json').read_text(encoding='utf-8'))
        en=json.loads((roots['en']/'references/company-examples.json').read_text(encoding='utf-8'))
        if not isinstance(zh,list) or not isinstance(en,list):
            raise ValueError('Company datasets must be arrays')
        if len(zh)!=6 or len(en)!=6:errors.append('Each edition must contain 6 companies')
        en_by_id={row['id']:row for row in en}
        if set(en_by_id)!={row['id'] for row in zh} or len(en_by_id)!=len(en):
            errors.append('Company IDs must be unique and identical')
        for row in zh:
            other=en_by_id.get(row['id'])
            if other is None:errors.append(f'Missing company {row["id"]}');continue
            if schema(row)!=schema(other):errors.append(f'{row["id"]}: JSON keys, types or array lengths changed')
            for key in ['id','category','checked_date','url','currently_open_verified','evidence_access','recruitment_status','alternate_official_urls']:
                if key in row and row[key]!=other.get(key):errors.append(f'{row["id"]}: invariant {key} changed')
            if [x['evidence_type'] for x in row['requirements']]!=[x['evidence_type'] for x in other['requirements']]:
                errors.append(f'{row["id"]}: required/preferred/duties classification changed')
            if len(row['teaching_mapping'])!=len(other['teaching_mapping']):errors.append(f'{row["id"]}: teaching mapping count changed')
            if other.get('currently_open_verified') is not False:errors.append(f'{row["id"]}: open status must stay unverified')
            for key in ['company','title','location','career_stage','status','limits','source_evidence','posting_date']:
                if key not in other:errors.append(f'{row["id"]}: missing {key}')
    except (OSError,ValueError,KeyError,TypeError) as exc:errors.append('Company parity: '+str(exc))
    return {'passed':not errors,'version':VERSION,'editions':summaries,'errors':errors,'scope':'Inventory, naming, source URLs and categorical facts only. Semantic translation and client behavior need separate review.'}

if __name__=='__main__':
    result=validate_bilingual();print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['passed'] else 1)
