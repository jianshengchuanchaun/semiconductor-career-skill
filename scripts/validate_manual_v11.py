"""Check the v1.1 handbook structure and rendered page boundaries.

This supplements, and never replaces, inspection of every final page PNG.
"""
from pathlib import Path
import json
import zipfile
from lxml import etree
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
DOCX=ROOT/'docs/半导体研究生就业规划手册_我的模拟电路世界_v1.1.0.docx'
QA=ROOT/'.qa/word-v1.1'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r':'http://schemas.openxmlformats.org/package/2006/relationships'}

def main():
    source=json.loads((ROOT/'docs/manual-content.json').read_text(encoding='utf-8'))
    with zipfile.ZipFile(DOCX) as z:
        body=etree.fromstring(z.read('word/document.xml'))
        rels=etree.fromstring(z.read('word/_rels/document.xml.rels'))
        text=''.join(body.xpath('//w:t/text()',namespaces=NS))
        links=rels.xpath('//r:Relationship[contains(@Type,"hyperlink")]/@Target',namespaces=NS)
        link_elements=body.xpath('//w:hyperlink',namespaces=NS)
        titles=body.xpath('//w:p[w:pPr/w:pStyle[@w:val="Heading1"]]',namespaces=NS)
    pdf=PdfReader(QA/'handbook.pdf')
    checks={
        'source_version':source['version']=='1.1.0',
        'authored_pages':len(source['pages'])==32,
        'rendered_pages':len(pdf.pages)==32,
        'numbered_page_titles':len(titles)==31,
        'external_links':len(links)>=10 and len(link_elements)>=11,
        'source_and_evidence_labels':all(x in text for x in ['官方域名索引','页面明确已过期','3年及以上经验','教学故障注入','εP','εT','温升ΔT']),
        'thermal_bad_wording_removed':'热点温度变化小于百分之三' not in text,
        'v10_preserved':(ROOT/'docs/半导体研究生就业规划手册_我的模拟电路世界_v1.0.0.docx').exists(),
    }
    page_checks=[]
    for i,page in enumerate(pdf.pages):
        extracted=page.extract_text() or ''
        normalized=''.join(extracted.split())
        expected=''.join(source['pages'][i]['title'].split())
        found=expected in normalized
        page_checks.append({'page':i+1,'expected_title':source['pages'][i]['title'],'title_found':found,'chars':len(extracted)})
    checks['page_boundaries']=all(p['title_found'] for p in page_checks)
    report={'checks':checks,'pass':all(checks.values()),'hyperlink_count':len(link_elements),'unique_link_targets':links,'page_checks':page_checks,'visual_review':'Review every PNG separately; these checks do not detect clipping.'}
    (QA/'structure-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'pass':report['pass'],'checks':checks,'hyperlink_count':len(link_elements)},ensure_ascii=False))
    if not report['pass']:raise SystemExit(1)

if __name__=='__main__':main()
