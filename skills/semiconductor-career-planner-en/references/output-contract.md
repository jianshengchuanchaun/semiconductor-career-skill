# Output Contract

## Structure of a first complete plan

Use this structure when enough information is available and the user requests a complete route. If program length or graduation month is unknown, prioritize 30-day exploration and unconfirmed long-term milestones. Use an explicitly assumed three-year route only for a requested long-term example. If net time is unknown, offer 20/45/90-minute options; do not invent a quantitative weekly budget.

1. **Target role and capability list:** State the primary track and alternative in one sentence; label undecided roles as candidates. Explain work and outputs through 5–8 core capabilities.
2. **Student profile and assumptions:** Separate known, unassessed, and unconfirmed information. State program length, graduation time, net weekly time, and resource limits.
3. **Role samples and skill gaps:** Give sources and retrieval dates, P0/P1/P2, current evidence, and target levels. Without a JD, label a general framework.
4. **Staged route:** Semester overview, 90-day targets, stage-gate acceptance, and links to graduation research.
5. **First 4 weeks:** Tasks, hours, input material, outputs, acceptance, and recovery per week; sum within budget.
6. **Three project tiers:** Minimal experiment, core project, optional advanced work; specifications, steps, validation, portfolio material, and interview follow-ups for each.
7. **Job-search preparation:** Internship/graduate-recruitment preparation windows, resume evidence, information channels, and adjacent alternative.
8. **Next step:** The next 60–90-minute action, at most 3 key answers needed from the student, and a review date or trigger.

For extensive content, provide the skill map and this week's execution plan first, then put the long-term route in files. Do not dump all 13 complete role routes in the first response. “Study analog circuits, digital circuits, and programming” without tasks is insufficient.

## Task card

Each card contains a task ID, corresponding role capability, prerequisites, precise resource chapter/topic, estimated time, concrete steps, deliverable file or oral output, acceptance method, debugging order if unsuccessful, and completion evidence. Prefer verifiable behavior such as “explain the gain change between two corners” over unqualified “master” or “be familiar with”.

## Skill-ledger columns

Skill ID | Role | Skill | Priority | Current level | Current evidence | Target level | Prerequisites | Task ID | Acceptance | Reassessment date.

Use “not yet assessed” for unknown levels and “not supplied” for missing sources. Preserve self-ratings in a separate field; do not treat them as verified evidence.

## Project acceptance report

Project name; educational specifications; conditions and units; version; input files; run steps; raw logs; results table; pass/fail; failure diagnosis; repeatability; personal contribution; confidentiality handling; untested conditions. Every “pass” needs actual output. Use “not yet run” when no run occurred.

## File outputs

Suggested directory:

```text
career-plan/
  profile.md
  career-plan.md
  skill-ledger.md
  weekly-plan.md
  project-spec.md
  evidence-index.md
  jd-matrix.md
  review-log.md
```

These names are not a platform-specific API. Read old files before updating, retaining dates and reasons for changes. Without file access, provide copyable text. Long-term tracking depends on these files or a student resubmitting a review; do not promise permanent cross-session memory, automatic reminders, or background execution.

## Minimal first-response example

“If analog IC design is your primary track, start with MOS/small signal, biasing, feedback stability, noise/mismatch, simulation methods, layout/post-layout awareness, and engineering explanation. Your introductory output is a reproducible single-stage amplifier; your core output is an amplifier module with specifications and boundary checks. First confirm your program/research, net weekly time, and authorized tools. Your present ability is not yet assessed. Today, start with three diagnostic questions about operating point and small-signal gain. After your answers, we can schedule week one.”

This is only an opening paragraph. Follow it with capability mapping and real diagnostic questions, for example:

| Capability | Work supported | Introductory output |
| --- | --- | --- |
| MOS and small signal | Select operating point and estimate gain | Hand-calculation versus DC/AC comparison |
| Feedback stability | Explain stability under loading | Loop definition and frequency-response analysis |
| Noise and mismatch | Identify precision limits | Noise/error budget under stated conditions |
| Simulation and debugging | Check specifications and locate failures | Reproducible test flow and anomaly record |
| Layout and engineering explanation | Explain parasitics and delivery boundaries | Layout-impact explanation and project evidence index |

Three diagnostic questions: How would changing a common-source stage's bias affect its operating point and gain? How could a larger load capacitance change the dominant pole? Which three items would you check first if simulated output clips? The student may answer only one initially.

Today's task card: spend 60 minutes drawing a common-source stage and hand-calculating its operating region and the direction of gain changes; save the circuit, parameter assumptions, and derivation. Pass by explaining the assumptions and predicted direction. If MOS operating regions are unclear, return to two basic region-condition exercises rather than forcing a tool run. This example need not be copied verbatim.
