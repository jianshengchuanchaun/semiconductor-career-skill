# Role Selection Guide

This map of role tasks helps beginners choose a direction to test. Organizational boundaries, job titles, and qualifications vary by employer; it does not imply all companies recruit all these roles. Read the table, then expand only the relevant role reference.

| Track ID | Target role | Core daily tasks | What an introductory project should demonstrate | Main resource dependencies |
| --- | --- | --- | --- | --- |
| D1 | Digital IC front-end / RTL design | Turn specifications into synthesizable logic; handle protocols, timing, and architecture | Correct RTL, self-checking testbench, interpretation of synthesis results | RTL simulator, synthesis tool |
| D2 | Digital IC design verification / DV | Verification planning, stimulus, checking, coverage, and debugging | Find and explain bugs; explain coverage gaps | SV/verification environment, regression resources |
| D3 | Digital physical design and STA | Constraints, placement/routing, timing and physical closure | Correct constraints/timing analysis and reproducible experiments | PDK/libraries, implementation tools |
| D4 | Design for test / DFT | Scan, test modes, ATPG, test coverage | Understand fault models and verify test paths | DFT tools and test structures |
| D5 | FPGA development | Hardware interfaces, timing, synthesis/implementation, board debugging | Working module and board-level measurements | FPGA tools and development board |
| D6 | EDA software development | Algorithms, tool architecture, parsing/optimization, regression | Reliable software, complexity analysis, testing | C++/Python, algorithm foundations |
| A1 | Analog and mixed-signal IC design | Topologies, biasing, stability, noise, boundary validation | Specification-driven circuit analysis and simulation | Circuit simulator, legally available models |
| A2 | Analog layout design | Matching, parasitics, isolation, DRC/LVS, collaboration | Explain layout decisions with actual check reports | Layout tool, PDK/rules |
| A3 | Devices and TCAD | Modeling, meshing, calibration, parameter extraction, physical interpretation | Model/experiment consistency and error bounds | TCAD or educational models, data |
| A4 | Process engineering and integration | Process windows, experiments, yield, cross-step analysis | DOE/SPC, controlled variables, attribution | Process information, experimental/production data |
| A5 | Packaging and reliability | Thermal/mechanical/interconnect analysis, stress, failure | Test conditions, failure analysis, model boundaries | Test/analysis tools, sample data |
| A6 | Chip test and product engineering | Test programs, characterization, data analysis, yield diagnosis | Measurement credibility, test coverage, binning rationale | Instruments/ATE or authorized data |
| A7 | Applications engineering and FAE | Part selection, board validation, customer debugging | Circuit/system debugging and clear technical communication | Datasheets, evaluation boards/instruments |

Subspecialties matter: D3 physical design and dedicated STA may have different duties; A4 distinguishes individual-step process engineering (PE) from cross-process integration (PIE); A6 distinguishes test development, product engineering, and validation/characterization; A5 package design and reliability testing are different roles; A7 applications engineering differs from field support. Narrow the scope with real JDs after choosing a direction. RFIC, power devices, memory, CIS, advanced packaging, and other specialties can extend adjacent tracks; this version does not claim to cover every semiconductor role.

## Start with tolerance for the actual tasks

Analog: Are you willing to spend sustained time testing hypotheses about operating points, poles, noise, and trends?

Digital: Do you enjoy precisely expressing state machines, protocols, concurrency, and boundary behavior?

Verification: Will you deliberately construct failures, inspect logs, and explain why coverage is incomplete?

Physical implementation/layout: Will you repeatedly trade off spatial choices and constraints while maintaining rule and version discipline?

Devices/process: Do you enjoy physical explanations, experimental data, units, and controls, and can you accommodate equipment and scheduling limits?

EDA: Do you enjoy algorithms, software quality, and debugging large codebases, rather than only invoking tools?

FAE: Are you comfortable with communication, on-site problems, and possible travel, and explaining technical issues to people with different backgrounds?

These are exploration prompts, not a personality test or a career-screening verdict.

## Four-week exploration example

Assume 10 net hours/week: schedule 8 and reserve 2. Candidates are analog design and DV.

Week 1: shared profile/diagnosis 2h; minimal circuit-tool experiment 3h; minimal digital simulation 2h; review 1h.

Week 2: single-stage amplifier operating-point, gain, and swing experiments 6h; anomalies/interest record 1h; review 1h.

Week 3: self-checking FIFO or counter tests, including an injected boundary bug and diagnosis 6h; organize verification evidence 1h; review 1h.

Week 4: repeat the leading candidate task and explain orally 4h; read real JDs 2h; select the primary/alternative and plan the next cycle 2h.

If a tool is unavailable, begin with a legally usable open-source educational environment and record which employer workflows it does not cover. Do not require expensive boards or commercial licenses during exploration.

## Common mistaken conclusions

- “I heard this role pays well” is insufficient for choosing a track. Salary claims need a role, region, date, and source; do not promise compensation.
- “My supervisor's topic differs, so I must relearn everything” adds burden. First identify reusable research skills.
- “I built an open-source CPU, so I can do every digital role” ignores depth, verification, constraints, and differing duties.
- “Analog layout is just drawing” ignores matching, parasitics, and verification; “verification is just writing tests” ignores planning and coverage arguments.
- “Manufacturing roles do not need programming” overlooks data cleaning, automation, and statistics; programming still cannot replace process knowledge.
- “An ordinary university means only certain jobs are possible” lacks individual evidence. Discuss real JDs and addressable gaps.
