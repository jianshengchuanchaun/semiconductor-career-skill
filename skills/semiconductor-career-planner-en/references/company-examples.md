# Employer JD Examples: From Requirements to Learning Evidence

Edition: 1.2.0. Source snapshot checked on **2026-09-22**. The English translation date is not a new verification date. Load for employer comparisons, JD analysis, or teaching plans, not every routine weekly review. Field-level provenance, limitations, and task mappings are in [company-examples.json](company-examples.json).

“Domestic” in these examples means mainland-Chinese employers. All six samples concern roles in China and come from official company websites or official recruiting systems. They are neither a representative market sample nor a live vacancy list. Every `currently_open_verified` value is `false`: current application availability was not verified; this does not mean all roles are closed. F2 has explicit expiry evidence.

## Filter eligibility before decomposing skills

1. Compare the JD with the student's actual expected graduation date, enrollment status, degree, work experience, target region, and internship availability. Mark missing fields “unconfirmed”; skill similarity does not bypass mandatory conditions.
2. Keep **qualification requirements, advantages, job duties, and teaching inferences** separate. In this data, `required` means qualification requirement, `preferred` means preferred/advantage, and `explicit` means an explicitly stated fact such as a duty, not a mandatory qualification. Read `paraphrase` for context.
3. Duties may guide project selection; do not rewrite them as everything a first-year student must independently accomplish before starting. Preserve the strength of “familiar with”, “understand”, “preferred”, and “one/multiple”.
4. Record posting date, verification date, page readability, and recruiting status separately. An application link does not prove remaining places; readable indexed text does not prove the dynamic page or application flow works.
5. Compare similar role families and stages. Experienced-hire roles are growth references; expired roles are historical skill samples. A 2027 role does not imply a student enrolling in graduate school in 2026 graduates in 2027.

## Six-sample overview

| ID | Employer / role family | Region and stage | Evidence and appropriate use |
| --- | --- | --- | --- |
| F1 | NXP / analog design | Shanghai Jing'an; 2027 master's graduate recruitment | Official recruitment index; current application status unverified; skill teaching |
| F2 | Renesas / analog design | Tianjin Binhai; enrolled master's internship graduating in 2027 | Official body; **expired**; historical skill teaching |
| F3 | NVIDIA / ASIC design and verification | Shanghai; relevant enrolled bachelor's/master's internship | Official recruitment index; current application status unverified; skill teaching |
| C1 | Chipown / analog IC design | Wuxi/Suzhou/Shanghai; master's/doctoral graduate recruitment; cohort unstated in this role section | Official body; application availability unverified; duties-to-learning mapping |
| C2 | Telink / digital verification | Nanjing; 2027 relevant master's or higher graduate recruitment | Official recruiting-system body; application availability unverified; skill teaching |
| C3 | SGMICRO / analog IC design | Harbin/Shanghai/Shenzhen/Dalian/Chengdu/Suzhou/Beijing; experienced hire requiring 3+ years | Historical official body; **not a graduate-entry threshold**; long-term growth reference |

## F1 | NXP: Analog foundations and tools, with advantages listed separately

- Role: [2027 Campus - Analog Design Engineer, R-10064704](https://nxp.wd3.myworkdayjobs.com/en-US/careers/job/XMLNAME-2027-Campus---Analog-Design-Engineer_R-10064704). [Alternate official language path for the same role](https://nxp.wd3.myworkdayjobs.com/fr-FR/careers/job/Shanghai-JingAn/XMLNAME-2027-Campus---Analog-Design-Engineer_R-10064704).
- Date/access: exact posting date unavailable; only a relative date appeared. Checked 2026-09-22. Official index readable; direct dynamic-body extraction limited; current applications unverified.
- Source requirements: relevant master's graduate in 2027; CMOS analog, device/process/layout foundations; SPICE/EDA and Cadence experience; analytical ability and English/Mandarin collaboration.
- Source advantages: analog internship/research/tape-out, low-power precision analog, and post-silicon measurement. **Do not rewrite this as “tape-out required”.**
- Teaching inference: start with common-source hand calculations and simulation, then an op-amp or LDO project with clear specifications. Accept netlists, test conditions, discrepancy explanations, and personal contribution; attach DRC/LVS/post-layout evidence only if a real layout flow was completed.

## F2 | Renesas: Specifications and reviews, a historical internship sample

- Role: [Intern- Analog Design (Graduating from Year 2027)](https://jobs.renesas.com/job/intern-analog-design-graduating-from-year-2027-in-tianjin-china-jid-4127).
- Date/access: readable official body, **explicitly expired**. No separate exact posting date; a date in the requisition ID does not substitute for it. Checked 2026-09-22.
- Eligibility: full-time enrolled master's student in electronics/analog, graduating in 2027 and not before April 2027; Tianjin Binhai; 4 consecutive months, 5 days/week.
- Requirements/advantages: basic analog circuits, simulation tools such as SPICE/MATLAB, analysis/debugging, and communication; prior laboratory testing is an advantage. Duties include specifications, collaboration on post-layout simulation, and design reviews supported by results.
- Teaching inference: write 3–5 test specifications for an amplifier, perform one educational fault-injection/fix exercise, and present specification → test → conclusion. **Do not add the expired sample to an application list.**

## F3 | NVIDIA: Design/verification foundations and layered methodology preparation

- Role: [ASIC Design and Verification Intern, SOC - 2027, JR2024860](https://jobs.nvidia.com/careers/job/893397572374?domain=nvidia.com&hl=en).
- Date/access: posting date unavailable. Official recruitment index checked 2026-09-22; dynamic-body extraction limited; current applications unverified. The title contains 2027; do not infer a strict graduation-month condition absent from the body.
- Source requirements: relevant enrolled bachelor's/master's degree; digital logic, front-end ASIC flow, clocks/resets, Verilog/SV, formal verification, Linux/EDA, debugging, and English communication.
- Advantages/preferences: the language bullet lists UVM/SVA/coverage knowledge as a plus. **A separate formal-verification requirement asks for familiarity with concepts/tools and gives property specification/SVA, equivalence checking, and formal property verification as examples. The first bullet does not make assertion foundations dispensable.** Scripting or C/C++ experience is preferred; do not make every listed language mandatory.
- Teaching inference: use a synchronous FIFO for RTL, self-checking tests, boundaries, failure seeds, and regression scripts, then add assertions/coverage in stages. State project scope; do not claim commercial SoC signoff experience.

## C1 | Chipown: Duties guide projects but do not fill missing qualifications

- Role: [模拟IC设计工程师（校招） / Analog IC Design Engineer (Graduate Recruitment)](https://www.chipown.com.cn/cn/jobxylist/213.html). The English title is a translation of the official Chinese title.
- Date/access: displayed date 2026-07-31; checked 2026-09-22. Official body readable with an application entry; current vacancies/application availability unverified.
- Known conditions: Wuxi/Suzhou/Shanghai; master's/doctoral graduate recruitment. This role section does not list a graduating cohort or years of experience.
- Explicit duties: design/simulation, layout collaboration, test collaboration, and design documentation. **This section does not separately specify tool brands, English, or advantages; do not fill them from experience.** The 2028 cohort and one-year internship conditions for another role on the same page do not belong to this role.
- Teaching inference: add a specification-to-test index, layout constraints, and a test plan to a small-module simulation report. Label conceptual assignments, simulation, and measurement separately.

## C2 | Telink: Separate DV graduate qualifications from preferred experience

- Role: [2027校招-数字验证工程师（南京） / 2027 Graduate Recruitment – Digital Verification Engineer (Nanjing)](https://telink.zhiye.com/zpdetail/190837585). English title is a translation. Official authority entry: [company campus recruitment](https://www.telink-semi.com/campus-recruitment).
- Date/access: posting date not displayed; checked 2026-09-22. Official recruiting-system body readable with an application entry; live places/application availability unverified.
- Qualifications: relevant master's or higher, digital foundations, Verilog/SV, C/C++, understanding of UVM/OVM, at least one listed scripting language, verification documentation, CET-6 or above, and technical English reading/writing.
- Preferences: relevant verification research, UVM/OVM/assertions, tape-out verification, or FPGA testing experience. Regression and coverage closure also appear as duties.
- Teaching inference: add a reference model, regression summary, coverage-gap explanation, and English bug report to the FIFO core project. Check eligibility independently. Do not generalize this role's CET-6 condition to every employer.

## C3 | SGMICRO: Experienced hire with 3+ years, for growth direction only

- Role: [模拟集成电路设计工程师 / Analog IC Design Engineer](https://www.sg-micro.com/cn/society/job/2). English title is a translation.
- Date/access: displayed date 2024-04-18, not identified as initial posting or update; checked 2026-09-22. Official body readable; current application availability unverified.
- Conditions/requirements: relevant microelectronics/IC master's or higher, **3+ years of experience**, analog modules, device/process/control knowledge, and EDA/layout tools. No tool brand named.
- Teaching inference: use for post-graduation growth goals; first-year students may take foundational learning inspiration. **Exclude it from common graduate-entry P0 counts, do not recommend it as graduate recruitment, and never replace 3 years of work experience with a course project.**

## Output format for turning examples into plans

Explain the basis of each assignment with this mapping:

| Source statement/fact | Type | Student's current evidence | Learning task (teaching recommendation) | Output and acceptance | Still unknown |
| --- | --- | --- | --- | --- | --- |
| Explicit skill, qualification, or duty with ID/link | required / preferred / duties / eligibility | File, result, or not yet assessed | Based on the capability gap | Reproducible evidence and pass criterion | Eligibility, tool, or status gaps |

F1, F2, and C1 can illustrate analog learning directions, but keep graduate recruitment separate from internships. F3 and C2 can illustrate design/verification training, but do not attribute internship-versus-graduate differences to nationality or ownership of all employers. C3 is an experienced-role reference only.

Machine fields: `evidence_access` identifies an official body or official search index; `recruitment_status` records what this check supports; `currently_open_verified=false` means live application availability is unconfirmed. Keep `requirements` separate from `teaching_mapping`; every teaching mapping is original educational design for this project. Original Chinese research records remain in repository `docs/research-foreign-jobs.*` and `docs/research-domestic-jobs.*`. The installable package contains all independently readable case fields and does not depend on those repository files.

For debugging records, retain the actual conclusion within frozen specifications; an all-pass result may meet acceptance normally. If practice is needed, set up separately labeled educational fault injection. Keep real defects and injected faults separate. Do not invent errors to fill a case or label a deliberate injection as a real product defect.
