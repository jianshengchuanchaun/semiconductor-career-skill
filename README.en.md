# Semiconductor Graduate Career Planner Skill

[简体中文](README.md) | **English**

**我的模拟电路世界 (My Analog Circuit World) · v1.2.0**

[GitHub repository](https://github.com/jianshengchuanchaun/semiconductor-career-skill)

A job-oriented learning workflow for students entering a semiconductor, microelectronics, or related graduate program. **Start with the skills a target role requires, diagnose your current abilities, and build an achievable sequence of learning tasks, projects, evidence, and recruiting preparation.**

## Choose your language and platform

| Edition | Codex package | WorkBuddy package | Skill to invoke |
| --- | --- | --- | --- |
| English | [Download](release/semiconductor-career-planner-en-codex-v1.2.0.zip) | [Download](release/semiconductor-career-planner-en-workbuddy-v1.2.0.zip) | `semiconductor-career-planner-en` |
| 简体中文 | [下载](release/semiconductor-career-planner-zh-codex-v1.2.0.zip) | [下载](release/semiconductor-career-planner-zh-workbuddy-v1.2.0.zip) | `semiconductor-career-planner` |

Choose one edition to start. Each package includes its own instructions, role guides, resources, employer examples, and templates. The English edition is a complete translation of the operational skill, not just an English landing page. The two skill names are distinct, so both can be installed if needed; explicitly select one to avoid competing plans. An explicit request for another response language overrides the edition's default.

Read the [English installation guide](docs/INSTALL.en.md) or [中文安装说明](docs/INSTALL.md). Package formats follow the official documentation reviewed on **2026-09-22**; actual import and conversations in both clients have **not** been tested. This project is not platform certification and does not guarantee employment.

## Start your first plan

```text
Use the semiconductor-career-planner-en skill.
I am entering a semiconductor graduate program and expect to graduate in three years.
I have 12 hours per week available for career preparation and prefer IC design,
but I have not chosen a specific role.
First explain the skills needed for the candidate roles, then diagnose my starting point.
Help me select one main role and one adjacent alternative.
Break the plan into semesters, 90 days, the first four weeks, and my next task.
For each task, specify what to learn, what to do, estimated time, output, and acceptance criteria.
Ask about my research, graduation requirements, location, and available tools.
Do not assume I have commercial EDA access.
```

Where Codex supports the skill selector, use `$semiconductor-career-planner-en`. In WorkBuddy, enable the imported skill and name it in your request. If installation is unavailable, the installation guide provides a file-reading fallback without claiming that import succeeded.

## What the skill provides

- A role capability map with P0 foundations, P1 differentiators, and P2 extensions, tied to observable L0–L4 evidence levels.
- A gap analysis that considers research obligations, graduation requirements, prior work, available time, authorized software, and equipment.
- A semester overview, a provisional 90-day roadmap, four weeks of tasks, and a next 60–90-minute action.
- Three project levels for each route: a minimum experiment, a core project, and optional advanced work, with specifications, checks, debugging guidance, and interview questions.
- Weekly review, a skill ledger, evidence indexing, job-description matching, and interview or role-change preparation.
- Six employer examples that separate qualifications, preferred experience, duties, and the project's own teaching suggestions.

## Thirteen role routes

| IC design and engineering | Manufacturing and related work |
| --- | --- |
| Analog and mixed-signal IC design | Device engineering and TCAD |
| Analog layout | Process engineering and integration |
| Digital RTL design | Packaging and reliability |
| Digital design verification | IC test and product engineering |
| Physical design and static timing analysis | Applications engineering and FAE |
| Design for test | |
| FPGA development | |
| EDA software development | |

IC design is the main emphasis. A student normally follows one main route and one adjacent alternative. RFIC, image sensors, power devices, memory, and other specializations require further analysis of the specific target job descriptions.

## Employer examples and their limits

The translated examples remain **China-region recruiting samples**, checked on **2026-09-22**. Translating the skill does not turn them into a global labor-market survey or refresh their hiring status. Ask about the student's target country or region and collect locally relevant, comparable job descriptions before making application recommendations.

| Examples | What to preserve when using them |
| --- | --- |
| NXP, Renesas, Chipown: analog roles | The Renesas posting is expired. Chipown primarily lists duties, which must not become invented entry requirements. |
| NVIDIA and Telink: design/verification | One is an internship and the other a campus role. Preserve the stated strength of language and methodology requirements and the distinction between required and preferred experience. |
| SGMICRO: experienced analog design | The posting requires at least three years of experience. Use it as a growth reference, not a new-graduate threshold. |

NXP and NVIDIA were checked through text indexed from official recruiting domains; direct extraction of their dynamic pages was limited. The other samples were read from official pages. **No sample is marked as verified currently open.** Unknown posting dates stay unknown. The learning tasks are original teaching suggestions, not company interview questions or hiring standards. See the [English case guide](skills/semiconductor-career-planner-en/references/company-examples.md) and [structured evidence](skills/semiconductor-career-planner-en/references/company-examples.json).

## Learning and evidence principles

Explain the target role's skills before asking diagnostic questions. Do not assume all new graduate students start at the same level. Schedule about 80% of net available time and leave about 20% as buffer; adjust estimates using actual effort. Prioritize work that also helps the student's research and graduation obligations.

Record what the student actually did. Watching a lecture, reproducing a tutorial, independently debugging a module, and explaining trade-offs support different levels of evidence. A project whose defined tests all pass can be reported honestly; separately label deliberately injected teaching faults.

Distinguish educational simulation, authorized PDK simulation, DRC, LVS, post-layout analysis, tapeout, and physical measurements. One does not establish another. When commercial tools are unavailable, provide a lawful teaching route and state which industrial skills it cannot demonstrate.

## Repository layout

```text
skills/semiconductor-career-planner/       Chinese skill, references, and templates
skills/semiconductor-career-planner-en/    English skill, references, and templates
docs/                                    Installation, evidence, and release guidance
examples/                                Requests and worked examples
evals/                                   Evaluation cases and saved results
presentations/                           Chinese talk source and speaker script
scripts/                                 Validation, packaging, and document generation
release/                                 Four language/platform skill packages
```

**Source archives exclude Word, PowerPoint, and PDF deliverables.** The separately produced 32-page handbook and 12-slide talk are currently in Chinese. This bilingual release translates the skill and user-facing installation guides; it does not claim that English Office documents were produced. Details: [separate document files](docs/DOWNLOADS.en.md).

Normal use does not require running build scripts. Maintainers with Python 3.10+ can run:

```bash
python scripts/validate_release.py
python scripts/build_release.py
```

The skill itself does not bundle EDA tools, a live recruiting database, internet access, or background reminders. These depend on the host and the user's available resources. See [release guidance](docs/RELEASE.en.md) and [bilingual validation scope](docs/QA-v1.2.md).

## Follow-up requests

- “I have only six hours a week. Reduce this to one feasible learning route.”
- “Compare these three graduate job descriptions and connect their requirements to my project evidence.”
- “I graduate in 2029. Filter out incompatible recruiting cohorts before suggesting applications.”
- “I have no commercial EDA access. Give me an experiment I can complete with authorized teaching tools.”
- “Review this week's files against the acceptance criteria and revise next week's tasks.”
- “Run a mock interview, asking one question and following up on my answer.”
- “I want to move from device engineering into analog design. Identify transferable skills and missing prerequisites.”

## Author and contributions

Author and Bilibili brand: **我的模拟电路世界**. “My Analog Circuit World” is an English gloss of the existing name. License: [MIT](LICENSE). Third-party courses, tools, PDKs, and recruiting pages retain their own terms; this repository supplies links and original planning material.

Use GitHub Issues for source corrections, role additions, client compatibility findings, and actual learning feedback. Report the language edition and version. Do not include private student details, unauthorized PDKs, or confidential lab/company material. The [original contribution guide](CONTRIBUTING.md) is in Chinese; English issues are welcome.

Edition updated: **2026-09-23**. Employer and platform evidence retains its recorded verification date; a translation date is not a new verification date.
