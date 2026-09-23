# v1.2 bilingual validation / 双语版本验证

Edition date: **2026-09-23**. The translation does not refresh the platform, learning-resource, or employer-source verification date of **2026-09-22**.

## Scope

This release adds an independently installable English skill and bilingual documentation/download choices. Chinese Office deliverables and historical behavior records retain their original language and version.

## Completed checks

| Check | Observed result | Meaning and limit |
| --- | --- | --- |
| Language inventories | 21 skill files per edition, 13 routes, 9 templates | Each language is independently installable; matching inventory alone is not a translation-quality score |
| Role/resource translation review | 13 routes, 39 project tiers, 29 resource cards; hours, numerical ranges, thermal formulas, acceptance and evidence boundaries compared | Two independent cross-reviews covered the analog/industry and digital libraries; no fresh EDA experiments or external-source checks |
| Employer JSON | 6 cases, 29 requirement rows, 21 teaching mappings; schema, IDs, URL sets, source dates, status enums, booleans and required/preferred/duties categories preserved | Employer facts retain their source scope and verification date |
| Shared workflow/templates | Core workflow, 80/20 time budgeting, question batching, language choice, company boundaries and nine templates compared | Translation review; not a measured learning outcome |
| Four platform packages | Exact file inventories, ZIP CRC, skill body and supporting-file equality within each language | Platform-specific frontmatter and ZIP layout differ intentionally; client import untested |
| Source filtering | No Word/PPT/PDF deliverables, `.qa/`, private study folders or old release binaries | Existing Office content sources and historical QA remain with their original version |
| Isolated rebuild | Source unpacked into a fresh private directory without Office files; all five archives rebuilt byte-identically | Confirms source packaging does not depend on the separately held Office deliverables |

Two terminology/evidence issues found in the cross-review were fixed: the DFT behavioral model cannot establish coverage of actual physical memory defects, and TCAD calibration explicitly means model calibration against measured data. Two English teaching tasks were adapted to the user's chosen working language; this is teaching localization, not a change to the companies' stated English/Mandarin or CET-6 requirements.

## English forward-use smoke test

The [saved prompt and review assertions](../evals/bilingual-v1.2.json) describe a student graduating in June 2029, targeting DV in Germany/the Netherlands, with six hours/week and no commercial EDA. A separate model read the English skill and produced the [saved response](../evals/bilingual-v1.2-response.md). An independent reviewer checked the response against the skill and employer evidence.

The response begins with a DV capability map, keeps the Chinese recruiting snapshots separate from European applications, handles graduation/cohort and experienced-hire restrictions, schedules 288 task minutes plus 72 buffer minutes, and includes the 60-minute action within that budget. It distinguishes the two NVIDIA SVA contexts, unexecuted RTL from Python-model evidence, and educational injections from real defects. FIFO time is explicitly extended beyond four weeks when necessary.

The JSON translation was finalized after the first model read; the model then read it and reconciled the response before saving the published version. Only local file-link paths are normalized for the repository copy. The transcript is a planning response, not evidence that a student completed an experiment. One scenario does not establish a pass rate, and it does not exercise actual Codex/WorkBuddy import.

For reproduction, use Python 3.10+ and run `python scripts/validate_release.py`, followed by `python scripts/build_release.py`. The former checks structures and evidence categories; it does **not** execute the forward-use model case. Historical v1.1 checks remain separately labeled in [the earlier QA](QA-v1.1.md).

## Boundaries

- Source/ZIP checks and a model reading local skill files do not prove installation or invocation in either desktop client. Real Codex and WorkBuddy import acceptance remains uncompleted.
- The six employer cases retain their original regions, career stages and dates; no case is represented as a currently verified vacancy. No external recruiting pages were freshly rechecked for this translation.
- No English Word or PowerPoint was produced. Word/PPT/PDF deliverables remain outside the source package and repository.
- Numeric/link parity is evidence about preservation, not a certified translation-quality score or a claim that a student's projects have passed.
