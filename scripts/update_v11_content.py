"""One-time v1.1 editorial migration. v1.0 source archive is retained."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
def replace_file(rel, pairs):
    p=ROOT/rel;s=p.read_text(encoding='utf-8')
    for old,new in pairs:
        if old not in s: raise ValueError(f'Expected text missing in {rel}: {old[:50]}')
        s=s.replace(old,new)
    p.write_text(s,encoding='utf-8')

replace_file('skills/semiconductor-career-planner/references/roles-analog-process.md',[
 ('作品集至少有补偿前后对比、一个失败 corner、设计改动与回归结果。','作品集包含补偿前后对比、真实失败或单独标记的教学故障注入，以及设计改动与回归。原规格矩阵全部通过也如实保留，不强求某个工艺角失败。'),
 ('作品集必须有一个反直觉趋势及检验过程。','作品集应包含一个关键趋势的假设、检验和替代解释；若出现反直觉结果，再记录核查过程，不强求得到异常趋势。'),
 ('教学验收为能量平衡误差 <2%、网格加密后热点温度变化 <3%，','稳态教学验收定义为能量平衡误差 |P_in−P_out|/max(|P_in|, ε_P)<2%，网格差异用温升ΔT=T_hot−T_amb计算：|ΔT_fine−ΔT_coarse|/max(|ΔT_fine|, ε_T)<3%；项目前冻结ε_P、ε_T及接近零时的绝对容差，并记录绝对温差(K)。瞬态需另计储能，不能套稳态平衡式。'),
])

p=ROOT/'docs/manual-analog-pages.json';data=json.loads(p.read_text(encoding='utf-8'))
budget='路线周期按实际任务工时估算。净时间每周十二小时，只排九点六小时任务并重排日历；设备等待另计。'
for page in data:
    for block in page['blocks']:
        if 'text' not in block:continue
        s=block['text']
        s=re.sub(r'预计每周投入十二至十五小时，基础与核心项目约四个月，再按实际进度调整。',budget,s)
        s=re.sub(r'每周十二至十五小时，[^。]*。',budget,s)
        s=s.replace('作品集需有一个反直觉结果及其核查过程，不能只交漂亮云图。','作品集应解释一个关键趋势的假设和检验；若出现反直觉结果再核查，不强求异常。')
        s=s.replace('至少展示一次失败工况、原因、修改和回归结果；任何未达到的目标都如实保留。','优先展示真实失败与修复；若全部通过，可另做明确标记的故障注入。任何未达到的目标都如实保留。')
        s=s.replace('以能量平衡误差小于百分之二、网格加密后热点温度变化小于百分之三作为教学目标。','稳态能量平衡误差以输入功率为分母，目标小于百分之二；网格差异比较相对环境的温升，目标小于百分之三。接近零时改用预先冻结的绝对容差，并保存绝对温差。')
        block['text']=s
    # Calendar labels are illustrative stages, not promises at a fixed net H.
    for block in page['blocks']:
        if block.get('type')=='bullets':
            block['items']=[s.replace('第一个月','基础阶段').replace('第二个月','模块阶段').replace('第三至第四个月','核心项目阶段').replace('第三至第五个月','核心项目阶段') for s in block['items']]
p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

p=ROOT/'docs/manual-digital-pages.json';data=json.loads(p.read_text(encoding='utf-8'))
for page in data:
    for block in page['blocks']:
        if 'text' in block:
            block['text']=block['text'].replace('至少保留三个可复现错误及其修复验证','至少保留三类可复现失败或标明的教学故障注入及其修复验证')
p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied v1.1 editorial corrections; review thermal wording and version migration separately.')
