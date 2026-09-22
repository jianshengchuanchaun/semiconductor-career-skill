from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'evaluation-workspace/iteration-1'

def main():
    data=json.loads((ROOT/'evals/evals.json').read_text(encoding='utf-8'))
    for case in data['evals']:
        d=BASE/f'eval-{case["id"]}-{case["name"]}'
        d.mkdir(parents=True,exist_ok=True)
        meta={'eval_id':case['id'],'eval_name':case['name'],'prompt':case['prompt'],'assertions':case['assertions']}
        (d/'eval_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
        src=d/'with_skill/outputs/response.md'
        if src.exists():
            content=src.read_text(encoding='utf-8')
            header='> 以下为发布前虚构情境的模型生成示例，尚未由学生执行，不代表实际工程结果或录用效果。\n\n'
            if case['id']==3:
                header+='> 编辑补注：示例中的输入幅度减半与稳态窗口比较，应先确认已有工程是对应的瞬态分析；若只有AC曲线，应按AC激励与频率响应定义设计复测。原始评测答复和评分保持不变。\n\n'
            (ROOT/'examples'/f'{case["id"]}-{case["name"]}.md').write_text(header+content,encoding='utf-8')
    print('Prepared metadata and three labeled examples. Timing/token metrics are unavailable.')

if __name__=='__main__':main()
