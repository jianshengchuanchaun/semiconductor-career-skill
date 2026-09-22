"""Aggregate only observed assertion outcomes; do not invent timing or token metrics."""
from pathlib import Path
import json
import statistics

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'evaluation-workspace/iteration-1'

def main():
    spec=json.loads((ROOT/'evals/evals.json').read_text(encoding='utf-8'))
    runs=[]
    summary={}
    for config in ['with_skill','without_skill']:
        rates=[]
        for case in spec['evals']:
            d=BASE/f'eval-{case["id"]}-{case["name"]}'/config
            grade=json.loads((d/'grading.json').read_text(encoding='utf-8'))
            s=grade['summary'];rates.append(s['pass_rate'])
            runs.append({'eval_id':case['id'],'eval_name':case['name'],'configuration':config,
                         'run_number':1,'result':s,'expectations':grade['expectations'],
                         'notes':['One output per scenario and condition; no client import test.']})
        summary[config]={'pass_rate':{'mean':statistics.mean(rates),'stddev':statistics.stdev(rates),
                                      'min':min(rates),'max':max(rates)}}
    delta=summary['with_skill']['pass_rate']['mean']-summary['without_skill']['pass_rate']['mean']
    summary['delta']={'pass_rate':f'{delta:+.2f}'}
    data={'metadata':{'skill_name':spec['skill_name'],'timestamp':'2026-09-22','evals_run':[1,2,3],
                      'runs_per_configuration':1,'replications_per_scenario':1,
                      'metric_scope':'Descriptive assertion results only; no timing or token measurements.'},
          'runs':runs,'run_summary':summary,'notes':[
              'Three scenarios, one response per condition. This is a smoke check, not a statistically powered efficacy study.',
              'Standard deviation describes differences between these scenarios, not repeated-run stability.',
              'Time, token counts and client end-to-end compatibility were not measured.'
          ]}
    (ROOT/'evals/benchmark.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (BASE/'benchmark.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    rows=['# 情境冒烟检查结果','','每个情境每个条件仅1次。以下是输出要求的检查计数，不能解释为就业效果或统计显著提升。','',
          '| 情境 | 带Skill | 普通助手 |','| --- | --- | --- |']
    for case in spec['evals']:
        selected=[r for r in runs if r['eval_id']==case['id']]
        cells=[f'{r["result"]["passed"]}/{r["result"]["total"]}' for r in selected]
        rows.append(f'| {case["name"]} | {cells[0]} | {cells[1]} |')
    rows+=['','未取得可比的耗时、token或客户端实测数据。评分理由与证据见benchmark.json；完整输出和评分可在review.html查看。']
    (ROOT/'evals/benchmark.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    print(json.dumps({'runs':len(runs),'summary':summary},ensure_ascii=False))

if __name__=='__main__':main()
