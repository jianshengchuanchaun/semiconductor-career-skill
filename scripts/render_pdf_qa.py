from pathlib import Path
import json
import subprocess
import os
import shutil
import argparse
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / '.qa' / 'render'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--qa-dir',type=Path,default=QA)
    args=parser.parse_args()
    qa=args.qa_dir
    doc=PdfReader(qa/'handbook.pdf')
    records=[]
    for i,page in enumerate(doc.pages):
        text=page.extract_text()
        records.append({'page':i+1,'chars':len(text),'first_lines':text.splitlines()[:3],
                        'last_lines':text.splitlines()[-3:]})
    (qa/'page-map.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'pages':len(doc.pages),'page_map_file':str(qa/'page-map.json')},ensure_ascii=False))
    poppler = os.environ.get('CODEX_PDFTOPPM') or shutil.which('pdftoppm')
    if not poppler: raise RuntimeError('Set CODEX_PDFTOPPM to the authorized Poppler executable, or put pdftoppm on PATH.')
    subprocess.run([poppler, '-r', '120', '-png', str(qa/'handbook.pdf'), str(qa/'page')], check=True,
                   creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)

if __name__=='__main__':main()
