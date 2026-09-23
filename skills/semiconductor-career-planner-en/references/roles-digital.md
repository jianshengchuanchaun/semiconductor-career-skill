# Career tracks in digital IC, FPGA, and EDA

Author / brand: 我的模拟电路世界 (My Analog Circuit World). Content checked: 2026-09-22.

This is a role competency library. Read only the sections relevant to the student's selected direction; do not assign all six tracks at once. It describes typical responsibilities and training objectives for planning, not a promise about any company's current hiring requirements, vacancies, compensation, or hiring outcomes. Use real job descriptions (JDs) for the student's target location and graduation year. Without a JD, mark role-fit conclusions as **pending verification**.

Contents: 0 shared foundations and evidence standards; 1 digital-rtl; 2 digital-dv; 3 digital-pd-sta; 4 digital-dft; 5 fpga; 6 eda-development; 7 primary and adjacent tracks; 8 internship / graduate recruitment readiness; 9 evidence boundaries. These tracks correspond to D1–D6 in the role overview.

## 0. Assess every capability against the same standard

### 0.1 Levels and priorities

| Level | Capability definition | Acceptable evidence |
|---|---|---|
| L0 | No exposure, or unable to explain | Record the gap explicitly; a course title cannot substitute for evidence |
| L1 | Can explain the principles and solve basic problems | Independently drawn timing diagrams, hand calculations, oral explanations, and answers to follow-up questions |
| L2 | Can follow documentation to complete a minimal experiment and explain its results | Runnable scripts, inputs, versions, logs, and interpretation |
| L3 | Can independently complete a module / experiment, diagnose failures, and provide reproducible evidence | A complete record from specification to acceptance, including failure reproduction and fixes |
| L4 | Can evaluate trade-offs / optimize under constraints, with review | Controlled comparisons, consistent constraints, cost analysis, and another person's review; this does not mean senior-engineer status |

P0 means foundational capabilities to prioritize for the target role; P1 adds differentiation in applications; P2 broadens the direction. The target levels below are learning recommendations and must be adjusted against real JDs. A useful starting point for entry-level applications is core P0 skills at L2–L3, with at least one at L3; not everything needs to reach L4. Attending a course, finishing videos, copying code, or generating results with AI cannot independently establish a level.

### 0.2 The six roles work on different problems

| Track ID | Work object and central question | Primary evidence to deliver | Commonly confused boundary |
|---|---|---|---|
| digital-rtl | Microarchitecture and synthesizable RTL: how is a function implemented cycle by cycle? | Specification, RTL, constraints, verification records, synthesis results, and performance explanation | Writing FPGA examples does not automatically demonstrate ASIC front-end delivery skills |
| digital-dv | DUT behavior and risk: which errors remain undiscovered? | Verification plan, environment, checkers, coverage, and defect closure | DV is more than viewing waveforms or memorizing UVM class names |
| digital-pd-sta | Physical implementation and timing: how can placement, routing, and closure meet constraints? | SDC, PPA / timing reports, experiment records, and checklists | Producing GDS is not signoff; STA and P&R may be separate jobs |
| digital-dft | Manufacturing-test structures: how can faults be controlled, observed, and detected? | DFT architecture, scan / test constraints, fault and pattern reports | DFT differs from functional verification and ATE product testing |
| fpga | Programmable devices and board-level systems: how can hardware run reliably? | RTL, XDC / SDC, implementation reports, programming and board-test records | FPGA prototyping, algorithm acceleration, and board development have different emphases |
| eda-development | EDA software: how can circuits and constraints be processed correctly and efficiently? | C++ / Python code, regressions, algorithm explanations, benchmarks, and profiles | Invoking an EDA tool does not establish EDA algorithm-development ability |

### 0.3 Prerequisites shared by all digital tracks

Diagnose first, then fill gaps. Existing evidence can exempt the corresponding material. Allow approximately 6–10 weeks and 80–140 productive hours in total, usually alongside first-year graduate courses. Do not count these hours again in the specialist track.

1. **Digital circuits, 20–30 hours:** combinational / sequential logic, flip-flops, synchronous and asynchronous reset, counters, state machines, setup / hold. Acceptance: derive the next-cycle state from a waveform; identify latches, combinational loops, and priority logic.
2. **HDL and simulation, 20–35 hours:** Verilog / SystemVerilog fundamentals, blocking / nonblocking assignments, widths and signedness, parameterization, and synthesizability. Acceptance: independently write an enabled, resettable counter and a self-checking testbench; deliberately introduce and locate an off-by-one error.
3. **Linux / Git / automation, 15–25 hours:** directories and permissions, processes, text search, Git commits, Python file processing, and basic Make / shell. Acceptance: another person can rerun the experiment in a fresh directory using the README; failures return a nonzero exit status rather than merely printing “failed.”
4. **Timing and data interfaces, 15–25 hours:** clock period, latency versus throughput, ready/valid handshakes, buffering, and clock / reset domains. Acceptance: draw data-hold behavior and handshake events under backpressure; explain the different responsibilities of timing constraints and CDC structural checks.
5. **Engineering records, 10–25 hours:** specify before implementation, map tests to requirements, fix random seeds, and record tool versions. Acceptance: provide a “requirement → test → log → conclusion” table in which every conclusion points to a file.

Learning materials and exercises are in [resources-digital.md](resources-digital.md). Start with one foundation course, one tool reference, and the current project. Reading an entire bookshelf first is unnecessary.

### 0.4 Time, acceptance, and public-release boundaries

- The week estimates below assume the shared foundation is complete and 12–18 hours of tasks are actually scheduled each week. If net available time H is only 12 hours, schedule about 0.8H = 9.6 hours and extend the calendar. Hour ranges reflect different starting levels and project complexity; the upper bound need not fit the shortest duration. The three project tiers can build on one another. Do not add project hours a second time when they are already included in stage hours. Exercises already passed in the shared foundation may be shortened.
- Within the scheduled 0.8H, allocate approximately 25% to principles, 50% to implementation / experiments, 15% to review / explanation, and 10% to JD checks. Reserve the other 0.2H as buffer. If two consecutive weeks produce no runnable artifact, reduce task size or repair prerequisites.
- Every project should retain at least `spec.md`, `README.md`, source code, a run entry point, a version inventory, acceptance results, and `debug-notes.md`. Adapt filenames to repository conventions.
- Acceptance must state what was tested, what was not, and the conditions under which conclusions hold. A random-run count is not a quality guarantee. Coverage percentages need denominators, unreachable cases, exclusion reasons, and tool configuration.
- Public GitHub repositories should contain only self-authored / open-source material that may legally be published, plus permitted anonymized records. Laboratory PDKs, licensed models, commercial installers, company IP, internship data, and confidential layout / netlists must not be published merely to build a portfolio.
- Frequencies, data widths, test counts, and project sizes below are **proposed specifications**, not achieved results. Record the reason before changing a specification; do not hide failure by weakening constraints.

## 1. digital-rtl: digital IC front-end / RTL design

### 1.1 Fit and actual deliverables

This track suits students who enjoy decomposing problems into states, pipelines, datapaths, and protocols and repeatedly checking boundary conditions. Reasons to explore before committing include interest only in GUI operation, unwillingness to reason cycle by cycle, persistent avoidance of debugging, or reluctance to inspect width / reset issues after basic HDL exercises. These are exploration signals, not personality labels.

Two-week trial: spend 15–25 hours implementing an 8-bit, depth-4 synchronous FIFO with backpressure, then explain simultaneous read / write, empty / full boundaries, and reset behavior. Being able to connect a failing waveform back to the specification—and wanting to continue—is better fit evidence than simply “liking chips.”

Typical deliverables: module specification and microarchitecture diagram, port / register definitions, synthesizable RTL, basic assertions, self-test and collaborative DV issue records, synthesis scripts and constraint assumptions, preliminary PPA / timing interpretation, and release notes. Graduate applicants should first show one independently completed module before expanding into buses or processors.

### 1.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | Combinational / sequential logic, FSMs, blocking / nonblocking assignments, widths and signedness | L3 | Self-written parameterized module; explanation of synthesized registers / multiplexers; diagnosis and repair of two types of real defects or explicitly labeled teaching injections, recorded separately |
| P0 | Specification to microarchitecture: throughput, latency, buffering, arbitration | L3 | Timing and state / datapath diagrams, resource and cycle budgets, trade-off explanation |
| P0 | Self-checking simulation and basic assertions | L3 | Independent reference model, directed boundaries, random regressions, and automatic failure exit |
| P0 | Clocks / resets and CDC / RDC fundamentals | L2 | Separate solutions and assumptions for a single-bit level, a pulse, and multibit data; explanation that synchronizers do not guarantee zero risk |
| P0 | Synthesis, basic SDC, area, and critical paths | L2 | Actual synthesis logs, explanation of unintended-latch checks, clock and I/O constraints, and step-by-step timing-report interpretation |
| P0 | Linux, Git, basic Python / Tcl | L2 | One entry point to rerun regression, with results traceable to a code commit |
| P1 | One target interface, such as APB / AXI-Lite / AXI-Stream | L3 | Checks derived from the official protocol; waits, backpressure, errors / reset where applicable; no mixing of different protocol rules |
| P1 | Pipelining and PPA trade-offs; lint / equivalence concepts | L3 | Two versions compared under identical process / constraints / tool versions, including latency changes from added registers |
| P2 | Formal verification, low power / UPF, cache coherence, CPU / NPU architecture | L1–L2 | One JD-relevant topic and a bounded experiment; not all topics at once |

### 1.3 Dependencies and step-by-step path

Dependencies: digital timing → HDL → self-checking simulation → FIFO / pipeline → protocol module → synthesis and PPA. Learn CDC after obtaining correct single-clock behavior. Multicore / cache-coherence study cannot substitute for fundamentals.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–3, 35–50h | Counters, arbiters, FSMs; draw waveforms before RTL; a small runnable example each day | Derive 10 cycles by hand; no unexplained lint warnings |
| 2 | Weeks 4–7, 45–65h | Synchronous FIFO, reference queue, boundary tests; specify and test before implementation | FIFO still passes after parameter changes; reproduce a fix live |
| 3 | Weeks 8–12, 60–85h | Choose one protocol; implement register / streaming interfaces and error behavior | Acceptance table covers every protocol requirement, with evidence for waiting and reset |
| 4 | Weeks 13–18, 70–100h | Synthesis, clock / I/O constraints, critical-path diagnosis; compare pipelining or resource sharing | Area / latency / throughput comparison under consistent conditions; estimated frequency is not called measured silicon performance |
| 5 | Weeks 19–26, 90–125h | Integrate core project, small CDC experiment, independent review, interview explanation | Another person can reproduce it; explain specification, implementation, failures, trade-offs, and unfinished work in 15 minutes |

### 1.4 Three project tiers

**Minimal project: parameterized synchronous FIFO, 25–40 hours.** Proposed specification: `DATA_WIDTH=8/16`, `DEPTH=4/8/16`, one clock, explicit reset priority, full-write / empty-read behavior, and simultaneous read / write rules. Acceptance: for every configuration test empty, full, wraparound, concurrent reads / writes, and reset during operation; compare every transaction with a reference queue. Start with at least 10 fixed seeds and 1000 operations per seed, then add directed tests for newly identified risks. Diagnose sampling races, pointer wraparound, counter width, and specification ambiguity separately. Public evidence: specification, RTL, tests, seeds, concise logs, and a failure-to-fix diff. Passing random tests does not replace boundary testing.

**Core project: streaming data-processing module with register configuration, 90–150 hours.** Use a proposed 16-bit input and choose accumulation, saturating addition, or a simple FIR. Define the ready/valid stream interface precisely; choose either APB or AXI-Lite for configuration. Specify arithmetic widths, overflow policy, backpressure, frame boundaries, and when configuration takes effect. Acceptance: Python reference model, random stalls, discontinuous inputs, maximum / minimum values, interrupted configuration, and reset during operation; record unstalled throughput and latency; synthesize and explain the worst path. Diagnose sign extension, valid / data misalignment, consistency between configuration and in-flight transactions, and combinational ready loops. Public evidence: requirements traceability, architecture diagram, regression, synthesis scripts, and results under fixed conditions; do not publish restricted cell libraries.

**Advanced project: architectural trade-offs or a small subsystem, 100–180 hours.** Choose either a fully pipelined versus resource-shared implementation of the same computation, or an asynchronous FIFO added for dual-clock transfer. Acceptance: keep functionality and tests identical; report throughput, latency, register / cell area, and assumptions. For dual clocks, sweep multiple frequency ratios and phases and add structural / constraint review. Distinguish algorithmic equivalence, timing violations, and CDC protocol failures. Digital simulation cannot prove a metastability failure rate. Public evidence: comparison table, constraint review, counterexamples, and fixes. Claim “formal verification / CDC tool checks passed” only when those checks were actually performed.

### 1.5 Interview topics and common mistakes

Questions and acceptable answer directions: (1) Why are nonblocking assignments appropriate for sequential logic? Draw a counterexample. (2) Does four-cycle latency imply accepting data only every four cycles? (3) Which operation is accepted when a FIFO is full and read / write occur together? Follow the specification. (4) Why is synchronizing every bit of a multibit bus independently with two flip-flops unsafe? (5) How can an area change be attributed to architecture rather than different constraints? (6) Explain the hardest project bug and the missing test that allowed it.

Common mistakes: beginning with a large CPU and merely copying every module; treating `#delay` as synthesizable delay; disabling all warnings; accepting waveforms that merely “look right”; hiding real synchronous paths with false paths; claiming AXI mastery without independent-channel and backpressure handling.

Without commercial EDA: Verilator / cocotb can support functional experiments, Yosys can synthesize its supported syntax, and OpenSTA / OpenROAD can teach timing and implementation. State the SystemVerilog subset supported by the selected front end. These experiments do not establish completion of a company's commercial lint, CDC / RDC, formal-equivalence, low-power, or signoff flow. Official resources: D2, D3, D5, D6.

## 2. digital-dv: digital IC design verification

### 2.1 Fit and actual deliverables

This track suits students who enjoy finding counterexamples, building models, tracing causes, reading specifications, and understanding other people's code. Reasons to explore further before committing include pursuing “tests passed” without explaining coverage gaps, avoiding random-failure debugging, or assuming verification requires no digital-circuit knowledge. Two-week trial: take a FIFO with a known specification, leave the RTL unchanged initially, build boundary tests with an independent reference queue, then deliberately inject 3 bug types. Judge whether tests detect errors, not the testbench's line count.

Typical deliverables: verification plan; requirements-to-tests / coverage mapping; driver, monitor, scoreboard, and reference model; assertions; constrained stimulus; regression and coverage analysis; reproducible defect reports; module / subsystem verification closure records. UVM is a methodology and reuse framework; verification reasoning, protocol understanding, and debugging come first.

### 2.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | Digital circuits, RTL reading, cycle and concurrency semantics | L2–L3 | Timing diagram for an unfamiliar module; diagnosis of blocking / nonblocking and sampling errors |
| P0 | Verification planning, risk analysis, positive and negative scenarios | L3 | At least one checking method per requirement; explanation of uncovered risks |
| P0 | SystemVerilog verification basics or a runnable transitional environment | L3 | Separate transaction, driver, monitor, and scoreboard responsibilities; independent reference model |
| P0 | Automatic comparison, assertions, timeouts, reset handling | L3 | Errors fail automatically; hangs are detected; assertion firing and diagnosis evidence |
| P0 | Random regressions, coverage, defect closure | L3 | Seeds preserved, failures classified, coverage denominators explained, reproduction and closure criteria for defects |
| P0 | Linux / Git / Python and log analysis | L2 | One entry point for multiconfiguration regression; first causal error identified, not merely the last error line |
| P1 | UVM components, phases, sequences, TLM, factory / config | L2–L3 | Reusable agent executed on a supported simulator; DUT configuration changes do not require rewriting everything |
| P1 | SVA / formal verification, protocol / register models | L2–L3 | Assumptions distinguished from assertions; explicit conditions, depth, and counterexamples for proofs / bounded checks |
| P2 | SoC, low-power, mixed-signal, performance verification | L1–L2 | One JD-relevant topic; a terminology list is not mastery |

If the target JD explicitly requires SV/UVM, promote UVM from P1 to P0. Python / cocotb projects provide a verifiable starting point; they must not be renamed UVM projects on a résumé.

### 2.3 Dependencies and step-by-step path

Dependencies: RTL and timing → self-checking tests → transactions / scoreboard → coverage and randomness → UVM reuse → subsystem. Explain a lost transaction before studying complex factory overrides.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–3, 35–50h | Derive equivalence classes / boundaries from the specification; self-checking environment without UVM | Evidence of failure on known bugs and a pass on the correct version |
| 2 | Weeks 4–7, 45–65h | Separate driver / monitor / scoreboard; concurrency, timeout, reset cleanup | Passive monitor does not guess outputs from stimulus; handling of old transactions after reset is explicit |
| 3 | Weeks 8–12, 60–85h | SV classes / interfaces / random constraints, coverage, basic assertions | Coverage gaps produce new tests; current simulator limitations are known |
| 4 | Weeks 13–18, 70–100h | Port to UVM if suitable tools exist; otherwise finish component boundaries and interface documentation | Agent reusable in another configuration; unexecuted UVM code labeled unverified |
| 5 | Weeks 19–27, 100–145h | Core protocol DUT, fault injection, regression classification, verification report | Detect specification violations injected by a peer; complete 3 defect-closure stories |

### 2.4 Three project tiers

**Minimal project: adversarial FIFO testing, 25–45 hours.** Use an explicit single-clock FIFO specification and self-written RTL or an open-source module with its license acknowledged. Acceptance: empty / full, wraparound, continuous traffic, reset, and concurrent reads / writes. Inject at least three independent bug types—early full flag, read-data cycle misalignment, and pointer-wrap error—and record the check that catches each. Diagnose whether the reference model copies the DUT, whether sampling is correct, and whether the framework swallows exceptions. Public evidence: test plan, passing / faulty versions or patches, failure logs, and defect table.

**Core project: verify an APB register block or AXI-Lite slave, 90–160 hours.** Beginners choose one protocol. Specify address space, access permissions, waits / responses, byte enables where applicable, invalid addresses, and reset. Acceptance: transaction-based driver, passive monitor, independent register reference model, protocol assertions, and directed / random tests. Cover operation × address type × wait condition × reset interaction; explain unreachable cross-coverage bins. Distinguish DUT defects, environment races, model errors, and ambiguous specifications. Provide a minimal reproducer rather than an entire regression log. Public evidence: architecture, coverage definitions and actual results, and at least 3 types of reproducible failures or clearly labeled teaching fault injections; advanced practice may expand to 5 types. Record genuine defects separately from injections. Counts define practice scope; requirements coverage, independent checks, reproducibility, and fix verification remain the primary acceptance criteria.

**Advanced project: subsystem verification using reusable agents, 100–180 hours.** Choose a dual-interface subsystem containing configuration, a FIFO, and a computation core. Use UVM agents / sequences / scoreboard when supported; otherwise retain a non-UVM implementation and document a migration plan. Acceptance: reuse across configurations, concurrent streams and backpressure, reset in operation, long-hang detection, coverage closure mapped to requirements, and assertions or bounded formal checks for critical invariants. Diagnose transaction-correlation IDs, queue lifetimes, reset races, stimulus legality, and overly strong assumptions. Public evidence: regression manifest, versions, coverage-exclusion review, and debugging recording. Python functional counters are not “complete SV covergroup coverage closure.”

### 2.5 Interview topics and common mistakes

Questions and answer directions: (1) Why should the monitor be independent of the driver? (2) What do code and functional coverage show, and why does 100% not prove absence of bugs? (3) Which versions / configurations are needed in addition to a random seed to reproduce a failure? (4) What does a UVM objection solve, and what happens if misused? (5) How should a scoreboard treat in-flight transactions at reset? (6) How can confusing assertions and assumptions produce a misleading proof? (7) Use a defect report to distinguish a root cause from a symptom.

Common mistakes: memorizing all of UVM before the first testbench; testing only legal continuous traffic; copying the DUT algorithm into the reference model; chasing percentages without requirement mapping; counting injected bugs as undisclosed real defects; treating a million random runs as a formal proof.

Without commercial EDA: cocotb plus a supported simulator can teach verification architecture, automated comparison, coverage planning, and regression. Verilator's class, assertion, and functional-coverage support changes with versions; test the needed features in a small experiment rather than declaring universal support or no support. UVM documentation and reference implementations are publicly available, but downloadability does not establish local executability. Without a compatible environment, record SV/UVM as L1 or clearly bounded partial L2 and seek authorized university access. Resources: D2, D3, D4.

## 3. digital-pd-sta: digital physical design / static timing analysis

### 3.1 Fit and actual deliverables

This track suits students who enjoy constraints, spatial relationships, quantitative experiments, and long-log analysis, and who want to understand standard cells, interconnect, clock trees, and tool decisions. Reasons to explore further include expecting an “automatic finish” button, avoiding the constraints behind timing reports, or believing physical design never requires RTL reading. Two-week trial: interpret one setup and one hold path in a small teaching design; modify a justified constraint, predict the effect, and check with a tool.

PD deliverables often include floorplanning, power planning, placement, CTS, routing, ECOs, checks, and handoff reports. STA emphasizes clock / I/O / exception constraints, modes and corners, timing-path review, violation diagnosis, and cross-team closure. Start with shared foundations and branch according to the JD; a first-year graduate student need not simultaneously reach the full depth of both roles.

### 3.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | Digital timing, setup / hold, skew / latency / uncertainty | L3 | Hand calculations agree with reports; signs and launch / capture edges explained |
| P0 | SDC: clocks, generated clocks, I/O, exceptions | L3 | Constraint rationale, unconstrained endpoints, justification and review of exceptions |
| P0 | Roles of Liberty / LEF / DEF / netlists / SPEF / SDC | L2 | Input-output dependency diagram; consistent units, corners, libraries, and netlists |
| P0 | Tcl, Linux, result extraction, configuration management | L3 | Automated summaries across configurations, traceable to commands and versions |
| P0 | P&R flow and common congestion / timing issues | L2–L3 | Small design completes the stated flow; stage logs and failure analysis; STA students may initially target L2 |
| P0 | Constraint completeness and evidence boundaries | L3 | No deletion of paths or arbitrary false paths to hide violations; explicit list of unperformed signoff checks |
| P1 | CTS, ECO, parasitic effects, MCMM concepts | L3 | Controlled comparisons identifying setup improvements that worsen hold or area |
| P1 | DRC / LVS, antenna, IR / EM concepts and report reading | L2 | Tool-internal, teaching-rule, and approved-signoff checks distinguished; actual checks listed |
| P2 | OCV / AOCV / POCV, SI, low-power multi-supply domains, advanced packaging | L1–L2 | JD-based selection; no fabricated numerical results without the necessary models |

### 3.3 Dependencies and step-by-step path

Dependencies: flip-flop timing and interconnect RC → libraries / constraints → single-path STA → multiple paths and constraint review → P&R / CTS → multiple scenarios / ECO. Positive WNS does not establish tapeout readiness.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–4, 45–65h | Hand-calculated paths, Liberty / SDC, OpenSTA examples | Explain one complete setup and hold path; check units |
| 2 | Weeks 5–8, 45–65h | Clocks, I/O, generated clocks, unconstrained paths, justified exceptions | Another person reviews constraints; detect deliberately omitted clocks / ports |
| 3 | Weeks 9–14, 70–100h | Small-design P&R on a public platform; per-stage area / congestion / timing | Explain changes across CTS and estimated versus extracted parasitics |
| 4 | Weeks 15–21, 85–120h | PD: floorplan / density / CTS; STA: multiscenario reports / ECO | At least one explained optimization against a baseline; review actual failures, or separately labeled teaching injections if no real failure occurred |
| 5 | Weeks 22–30, 110–155h | Consolidate core project, review unusual paths, evidence package, interviews | Traceable inputs, constraints, logs, results; itemized signoff boundaries |

### 3.4 Three project tiers

**Minimal project: timing-path experiment notebook, 30–45 hours.** Use a public library and self-written small netlists with 10–100 registers. Create long combinational paths, short paths, and a controlled divided-clock example. Acceptance: explain hand/tool differences; show how missing constraints cause misjudgment; reanalyze after justified clock / I/O constraints. Diagnose time units, libraries, clock-object matches, and netlist connections before algorithms / RC. Public evidence: tiny netlists, SDC, hand calculations, complete path reports, and constraint review.

**Core project: a complete learning cycle from RTL to placement and routing, 100–170 hours.** Start with a teaching module around 1,000–10,000 cells, adjusted to machine capacity. Fix the public process platform, library corner, tool version, frequency target, and area limit. Acceptance: record synthesis, floorplan, place, CTS, and route results; list setup / hold, unconstrained paths, internal DRC, and the layout checks actually completed. Record actual congestion / timing conclusions. Preserve fixes when problems occur; if everything passes, a separately labeled teaching injection may be added, but do not require the original design to fail. Diagnose the first anomalous stage: floorplan / density, long wires, clock constraints, macro / pin placement, and available cells. Do not only alter the final stage. Public evidence: configuration, scripts, stage reports, critical-path diagrams, and before / after comparisons. Whether GDS may be published depends on source-library licenses.

**Advanced project: controlled three-factor PPA / timing experiment, 100–180 hours.** Select three factors from density, clock period, RTL pipelining, placement seed, and CTS settings; state controlled variables for each experiment. The STA branch may instead review multimode / multicorner constraints for the same design. Acceptance: at least 6 reproducible configurations; compare area, critical paths, WNS / TNS, hold, and runtime; report failed configurations. State whether RC is estimated or extracted and whether comparisons are valid. Exclude unintended changes in versions, libraries, constraints, randomness, and report stages; do not cherry-pick the best run. Public evidence: experiment matrix, raw summaries, aggregation script, trade-offs, and remaining signoff gaps.

### 3.5 Interview topics and common mistakes

Questions and answer directions: (1) Why does reducing frequency usually not fix hold? (2) How can positive skew affect setup and hold differently? (3) What design justification is needed for false paths and multicycle paths? (4) How do ideal-clock and propagated-clock reports differ? (5) Why is acceptable WNS insufficient with unconstrained paths? (6) Why can density affect area, congestion, and timing together? (7) After an ECO improves worst setup, what else must be checked?

Common mistakes: confusing LEF with GDS; checking only WNS and ignoring hold, TNS, path coverage, and other checks; arbitrary multicycle exceptions; comparing the “advancement” of different PDKs from uncontrolled results; calling tutorial GDS “tapeout / signoff complete.”

Without commercial EDA: OpenSTA teaches netlists, Liberty, SDC, SPEF, and reports; OpenROAD Flow Scripts supports implementation experiments on public platforms. Describe actual tools, rules, corners, and input models. **Open source does not inherently preclude tapeout, and commercial software does not automatically establish signoff. Without the full flow accepted by the target foundry / company, this training project cannot claim commercial signoff results.** Itemize missing SI, OCV, EM / IR, physical verification, reliability, and multiscenario checks. Resources: D6, D7.

## 4. digital-dft: design for test (DFT)

### 4.1 Fit and actual deliverables

DFT here means Design for Test, not density functional theory. It suits students interested in coordinating design, verification, physical design, and testing, and in fault models, structural constraints, and systematic diagnosis. Reasons to explore further include wanting only functional RTL work, no interest in clock / reset or manufacturing tests, or equating a working scan shift with completed ATPG.

Two-week trial: build a handwritten scan chain with 8–16 flip-flops, run shift and capture separately, inject a stuck-at fault, and explain its activation and observation. Choose this track after clearly distinguishing functional correctness from detectability of a particular fault class.

Typical deliverables: test modes / architecture, scan insertion and chain reports, test-clock / reset / enable constraints, DFT-rule issue closure, ATPG and fault classifications, pattern verification, and handoff to physical-design and test teams. Compression, MBIST, JTAG / IJTAG, and at-speed testing are separate topics chosen by JD. DFT engineers work closely with product / ATE test engineers but have different responsibilities.

### 4.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | Digital logic, clocks / resets, scan shift / capture | L3 | Scan waveforms, mode-switch tests, functional-mode regression |
| P0 | Controllability / observability and stuck-at fault model | L3 | Hand-derived detecting vectors for small circuits; explanation of undetectable faults |
| P0 | Scan-chain structure and basic DFT rules | L2–L3 | Chain length / connection checks; diagnosis of uncontrollable clocks, resets, or unknown-value sources |
| P0 | ATPG, fault simulation, fault-coverage denominators | L2 | Actual or teaching fault lists, classifications, detection matrix; no confusion with functional coverage |
| P0 | Basic STA, test timing constraints, pattern verification | L2 | Separate shift / capture constraints and modes; explicit statement of whether timing analysis was actually run |
| P0 | Tcl / Python / Linux, logs and reports | L2–L3 | Automated chain / fault summaries traceable to inputs and individual checks |
| P1 | Transition faults, at-speed / OCC, X management | L2 | Bounded experiments when resources exist; clearly labeled theoretical reasoning otherwise |
| P1 | MBIST, JTAG / IJTAG, or scan compression | L2–L3 | One complete small project; other topics may remain L1 |
| P2 | Hierarchical DFT, test power, diagnosis / yield, advanced-package testing | L1–L2 | Reading and cases for the target sector / company; no expectation that a teaching project covers all topics |

### 4.3 Dependencies and step-by-step path

Dependencies: flip-flops / clocks / resets → scan structure → fault models → fault simulation / ATPG → test timing → compression / MBIST topic. Without an authorized commercial DFT environment, explicitly assess the route as “theory and teaching experiments can proceed; engineering-toolchain evidence remains missing.” Do not hide resource limitations.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–4, 45–65h | Scan cells, shift / capture, chains, switching to functional mode | Explain chain states cycle by cycle; functional mode remains correct |
| 2 | Weeks 5–8, 45–65h | Stuck-at faults in small combinational circuits; exhaustive fault simulation | Independently compute detection matrix; distinguish collapsed / uncollapsed denominators |
| 3 | Weeks 9–14, 70–100h | Scan insertion or bounded teaching substitute, chain checks, test constraints | State rules / modes actually executed; diagnose one structural issue type |
| 4 | Weeks 15–21, 85–120h | ATPG / pattern verification with suitable tools; teaching ATPG with explicit gaps otherwise | Traceable coverage and fault classes; teaching results not called product coverage |
| 5 | Weeks 22–30, 110–155h | MBIST / JTAG topic, role alignment, defect and handoff reports | Complete one topic; explain handoffs with RTL / PD / ATE |

### 4.4 Three project tiers

**Minimal project: handwritten scan chain and fault activation, 25–45 hours.** Proposed 8–16 bits and one test clock; define `scan_enable`, `scan_in`, `scan_out`, reset policy, and shift / capture timing. Acceptance: matching shifted-in / shifted-out data, different initial states, mode changes, and bounded functional-equivalence tests; explain why one input vector alone cannot observe a particular fault. Diagnose scan bit order, sampling edge, enable-switch timing, and active asynchronous reset. Public evidence: schematic, waveforms, tests, explanations. Handwritten scan is not “scan insertion with industrial tools.”

**Core project: teaching ATPG / fault simulation for small netlists, 90–150 hours.** Start with combinational circuits of at most 8 primary inputs and 20–100 gates, using the **single stuck-at fault model** with explicit fault sites. Exhaustively enumerate inputs in Python, compare good / faulty outputs, and greedily select tests; then study the combinational core exercised by scan capture. Acceptance: cross-check at least two hand-solvable examples; distinguish detected, undetected, and proven redundant faults; report original / collapsed fault counts, test-set size, runtime. Diagnose wrong injection sites, fanout branch versus stem confusion, contamination between parallel fault states, and “not found” incorrectly classified as “undetectable.” Public evidence: self-written netlists, algorithm, detection matrix, boundaries. This demonstrates principles and software implementation, not industrial ATPG, transition-fault, compression, or ATE-pattern delivery experience.

**Advanced project: teaching MBIST or a complete DFT exercise in an authorized toolchain, 100–180 hours.** Choose A or B. A: implement a 32×8-bit SRAM behavioral model and a teaching March-style sequence controller. Specify the exact operation sequence and detectable fault model; inject an explicit subset of stuck-at, specified transition, and coupling faults. B: with supervisor approval and authorized tools, run scan insertion, DRC, ATPG, pattern simulation, and test-mode timing review on a small module. Acceptance for A: demonstrate detection of every claimed injected fault and explain that a behavioral model represents only the declared abstract fault models and does not establish coverage of actual physical memory defects. For B: retain actual tools and permitted reports with consistent classifications, modes, and denominators. Diagnose address traversal, read / write timing, expected-value updates, and whether the model actually represents the fault in A; X sources, mode constraints, chain connections, and clock / reset controllability in B. Public evidence: publishable code, algorithm / mode descriptions, anonymized results. Under an NDA, publish only approved abstract method descriptions.

### 4.5 Interview topics and common mistakes

Questions and answer directions: (1) Why does scan improve controllability and observability? (2) What do shift and capture do? (3) Why must fault coverage and test coverage be checked against the selected tool's definitions? (4) How do undetectable and undetected faults differ? (5) Why can asynchronous reset disrupt testing? (6) Why are transition faults not simply stuck-at faults? (7) How does increasing scan-chain count affect test time, pins, power, and routing?

Common mistakes: treating DFT as a niche shortcut based on memorizing terminology; claiming fault coverage from functional tests; calling exhaustive teaching ATPG industrial ATPG without size limits; claiming 100% after deleting difficult faults; assuming every March sequence detects every memory fault.

Without commercial EDA: handwritten scan, fault simulators, teaching ATPG, and MBIST are possible. OpenROAD's DFT module supports some scan-flow practice, but documented limitations and the pinned version must be checked. It is not a complete commercial ATPG / compression / MBIST / test-signoff suite. Synopsys TestMAX materials identify the scope of industrial flows; a product page provides neither free authorization, a tutorial, nor personal hands-on evidence. Resources: D8, D9.

## 5. fpga: FPGA design / system development / prototyping

### 5.1 Identify the type of FPGA role first

| Subtrack | Main object | Additional skills beyond shared RTL | Most useful application evidence |
|---|---|---|---|
| Boards / industrial control / acquisition | Peripheral interfaces, clocks, board stability | I/O electrical standards, board schematics, UART / SPI and other interfaces, instruments | Extended board tests, interface timing, error statistics, diagnosis records |
| Algorithm acceleration / communications / imaging | Algorithms mapped to fixed-point parallel hardware | Numerical error, DSP / BRAM resources, throughput / bandwidth budgets | Software reference model; error / resource / throughput comparison |
| ASIC prototyping | Mapping an ASIC subsystem to FPGA | ASIC / FPGA differences, clock / memory replacement, software loading, partitioning | Adaptation checklist, functional regression, prototype limitations, debug records |

This track suits students who want logic to run on real hardware and are willing to read board documentation and debug systems. Reasons to explore further include wanting simulation only and avoiding clocks, pins, power, or IP-interface documentation. The two-week trial can begin with simulated UART transmit / receive and fault tests; with a board, program it and record actual serial communication. An expensive board is not an entry requirement.

Typical deliverables: module / system specifications, RTL, IP configuration inventory, XDC / SDC and pin constraints, synthesis / implementation results, bitstream, board tests, integrated logic-analyzer captures, and resource / performance / stability reports. A blinking LED establishes only a minimal programming path, not system-design ability.

### 5.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | RTL, FSMs, handshakes, reset, CDC fundamentals | L3 | Self-checking module regression; cross-domain stability and reset-release explanation |
| P0 | LUT / FF / BRAM / DSP / clock resources | L2 | Predicted versus synthesized resources; why BRAM was or was not inferred |
| P0 | Clock / I/O / pin constraints and implementation timing | L3 | Constraint review, actual implementation reports, unconstrained-path explanation; synthesis alone is insufficient |
| P0 | One board-level interface and hardware debugging | L3; initially L2 without a board | Same specification in simulation and board tests; failed data traced to timing / pins |
| P0 | Python / C, Git, automated builds and tests | L2 | Host-driven tests, automatic checking, error logs, rebuild instructions |
| P1 | Fixed-point arithmetic and DSP / imaging / communications topic | L2–L3 | Error model, saturation / truncation, pipelines, bandwidth budget; promote priority for the chosen subtrack |
| P1 | SoC FPGA, DMA, DDR / high-speed interface integration | L2 | Platform-specific system budget and tests; vendor-IP work separated from personal work |
| P2 | HLS, PCIe, high-speed transceivers, partial reconfiguration | L1–L2 | One JD-relevant topic; a successful HLS run does not establish efficient hardware |

### 5.3 Dependencies and step-by-step path

Dependencies: RTL / self-checking → device resources and constraints → small interface → complete board exercise → multiple modules / algorithm → high-speed / system work. Without a board, retain the board-level skill gap; simulation cannot fill it as L3.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–3, 35–50h | Device structure, synthesis / implementation, simulated UART or SPI | Explain clock / baud relationship; self-checks detect bad frames |
| 2 | Weeks 4–7, 45–65h | XDC / SDC, pins, voltage standards, clocks, reset / CDC | Review constraints before programming; no unexplained critical warnings |
| 3 | Weeks 8–12, 60–85h | Board interface, host scripts, ILA / equivalent debugging | Reproduce and diagnose a board issue; suspend this rating without a board |
| 4 | Weeks 13–19, 85–120h | Integrate datapath, FIFO, fixed-point algorithm or acquisition interface | Budgets and actual results for function, throughput, error, resources |
| 5 | Weeks 20–27, 95–135h | Stability, boundaries, resource / frequency trade-offs, presentation | Separate simulation / board evidence; reconstruct the environment from documentation after power-off |

### 5.4 Three project tiers

**Minimal project: UART loopback with detectable errors, 25–45 hours.** Proposed 8N1, 115200 baud; fill in the real board's system clock. Simulation should allow baud deviation, reset, and invalid start / stop conditions. Acceptance: self-check received / transmitted data and boundaries; with a board, run host tests and record actual byte and error counts. Diagnose clock frequency, divider rounding, sampling points, pins, I/O voltage standards, and TX/RX wiring. Public evidence: RTL, tests, constraints, implementation report, board logs with time / configuration. A boardless version must include “simulation” in its project title.

**Core project: configurable acquisition / streaming-processing platform, 90–160 hours.** Proposed path: UART or SPI input → FIFO → 16-bit computation core → output. Start with a data generator instead of an expensive ADC and explicitly identify it as a simulated data source. Specify system clock, peak input rate, buffer depth, output bandwidth, drop policy, and statistics registers. Acceptance: software reference, bursts and backpressure, extended testing, reset during operation, full-load resources and implementation timing. If planning a 30-minute stability test, report the actual duration and traffic rather than simply declaring reliability. Diagnose underestimated buffering due to average versus peak rates, flow-control misalignment, clock domains, host serial buffers, and fixed-point overflow. Public evidence: system diagram, bandwidth budget, scripts, implementation reports, raw board-error counts, video, known limitations.

**Advanced project: fixed-point FIR / small image operator / ASIC prototype, 100–180 hours.** Choose one for depth. For algorithms, fix samples and reference precision, then compare two widths or parallelism levels. For prototyping, choose a clearly licensed small module and document adaptation of ASIC clock gating, memories, resets, and FPGA resources. Acceptance: error, throughput, latency, DSP / BRAM / LUT usage, and implementation timing for identical inputs. With a board, record measured throughput; estimates are not measurements. Diagnose bandwidth bottlenecks, quantization, RAM read latency, IP parameters, and clock relationships. Public evidence: controlled comparisons, adaptation table, runnable demonstration. Identify self-written work when using vendor IP; the IP core itself is not a personal achievement.

### 5.5 Interview topics and common mistakes

Questions and answer directions: (1) Why does an HDL array not necessarily become BRAM? (2) What bottleneck could keep throughput unchanged despite higher frequency? (3) Why might CDC errors pass simulation but appear intermittently on a board? (4) What should be checked first when internal logic works but UART data is garbled? (5) Why can an ILA change resources and timing? (6) How does narrower fixed-point width affect error and resources? (7) Which ASIC behaviors can an FPGA prototype validate, and which physical properties cannot it establish?

Common mistakes: connecting ready-made IP without original interface specifications / tests; video-only demonstrations without source, versions, or logs; presenting synthesis frequency estimates as board performance; declaring CDC correct after setting every crossing to false path; buying costly high-speed boards not yet needed.

Without commercial EDA / a board: complete RTL and tests with open simulation first. Free vendor-tool editions, device support, and additional IP licensing vary by version; check the exact device and license before installation, without promising free support for every board. AMD constraint / debug guides support learning; open FPGA tools cover only their explicitly supported devices and functions. Without board tests, label conclusions simulation / implementation, not “board validation complete.” Resources: D10, D11, D12.

## 6. eda-development: EDA software / algorithm development

### 6.1 Fit and actual deliverables

This track suits students willing to study C++, algorithms, data structures, circuit models, and engineering scale. If using tools to deliver chips is more appealing, prioritize design or physical design. If generic software is appealing but circuit study is not, complete a two-week exploration before choosing. EDA roles include front-end compilation / synthesis, simulation, formal verification, STA, placement / routing, device simulation, and CAD flows. Do not assign all specialties to one student.

Two-week trial: represent a timing DAG in Python or C++, compute its longest path and report the critical path; add cycle detection, invalid inputs, and minimal counterexamples. Continue if questions about correctness, speed, and memory remain interesting.

Typical deliverables: algorithm / data-structure implementation, interfaces and input models, regressions, reproducible bugs, performance / memory profiles, benchmark designs, code review, documentation. Papers or competitions can strengthen communication, but students must identify their implementation, actual tests, and improvement costs.

### 6.2 Skill targets

| Priority | Skill | Suggested target | Concrete acceptance evidence |
|---|---|---|---|
| P0 | C++, memory / lifetimes, STL, build / debugging | L3 | Self-written medium-sized module, debugger / sanitizer diagnosis, reproducible build |
| P0 | Data structures / algorithms, graph traversal, complexity | L3 | Hand calculation and small exhaustive checks; worst-case complexity and input assumptions |
| P0 | Digital circuits and the selected EDA stage | L2 | Explain circuit objects and semantics; correct algorithms must also use correct circuit models |
| P0 | Testing, regression, logs, Git, Linux | L3 | Minimal failing case and regression protection for each fix; runnable in a fresh environment |
| P0 | Python / Tcl and report / data processing | L2 | Automated benchmarks, aggregation, failure classification |
| P0 | Profiling and comparable experiments | L3 | CPU / memory profiles; fixed inputs, versions, hardware, threads; not just the single fastest run |
| P1 | One specialty: STA / synthesis / simulation / formal / P&R | L3 | Small algorithm module or open-source extension connecting mathematical assumptions to circuit results |
| P1 | Large-codebase reading, review, open-source collaboration | L2–L3 | Actual call path; independent patch / issue draft; public submissions follow project procedure |
| P2 | SAT / SMT, numerical optimization, parallel computing, compiler IR, ML for EDA | L1–L2 | One specialty-relevant topic; correct baseline before complex methods |

### 6.3 Dependencies and step-by-step path

Dependencies: C++ / data structures → circuit representation → correctness tests → baseline algorithm → profiling → optimization → real open-source module. At programming L0, add 8–12 weeks and 100–160 hours beyond the shared foundation. This is not a promise to enter EDA after a few weeks of Python.

| Stage | Weeks / hours | What to learn and practice | Exit criterion |
|---|---|---|---|
| 1 | Weeks 1–5, 60–90h | Small C++ programs, containers, RAII, CMake, debugger, tests | Explain object lifetimes, locate bounds / dangling-reference errors, build without guessing dependencies |
| 2 | Weeks 6–10, 60–90h | Graphs, topological order, path algorithms, netlist representation | Hand / exhaustive small-graph checks agree; cycles and invalid inputs explicitly rejected |
| 3 | Weeks 11–17, 85–125h | Choose one EDA topic, read interfaces / call paths, implement minimal core project | Supported models and unsupported scenarios explicit; reproducible function |
| 4 | Weeks 18–25, 95–145h | Benchmarks, differential testing, profiling, correctness-preserving optimization | Correctness / error checks plus runtime / memory costs |
| 5 | Weeks 26–34, 110–160h | Integrate with open source or extend input scope, review, interview preparation | Reviewable patch, minimized failures, independently repeatable performance findings |

### 6.4 Three project tiers

**Minimal project: teaching timing-graph analyzer, 30–50 hours.** Define and publish a DAG input format with nodes, edges, and nonnegative fixed delays. Support multiple sources, topological sorting, latest arrival times, and a critical path. Explicitly exclude nonlinear Liberty delay, clocks, setup / hold, parasitics, and exceptions. Acceptance: hand-solved graphs, random small DAGs checked exhaustively, cycle detection, disconnected nodes, duplicate edges, and empty input; deterministic, traceable output. Diagnose topological order, initialization / unreachable values, floating-point comparisons, parsing. Public evidence: input format, algorithm, tests, limitations. Name it “teaching longest-path / simplified STA,” not a complete STA engine.

**Core project: simplified incremental timing or placement optimizer, 100–180 hours.** Choose A or B. A: incrementally update timing after changing a few edge delays; compare every node against full recomputation. B: implement teaching placement for a fixed small netlist in a rectangular region, with explicit wirelength estimation and nonoverlap / boundary / fixed-cell constraints. State that B does not include real routability or signoff. Acceptance: at least three sizes, multiple fixed inputs / seeds, correctness before speed comparisons, all failures retained, build type / threads / machine recorded. Diagnose dirty-node propagation, change direction, and cache invalidation for A; objective / legalization, randomness, and stop conditions for B. Public evidence: baseline, optimized implementation, data generator, results, and profiling plots, not only a speedup table.

**Advanced project: improve a real open-source EDA module, 120–220 hours.** Choose a narrow bug, diagnostic improvement, test, or performance problem in OpenROAD / Yosys / Verilator / another clearly licensed project. Read contribution guidance and the current implementation first; avoid meaningless formatting changes merely to obtain a PR. Acceptance: pinned commit, minimal reproducer, original failure / fixed success, relevant regression, and model / API compatibility explanation. Performance work must check output correctness and report distributions. Diagnose actual execution paths, separate configuration / build / dependency problems, and check whether another stage overwrites the result. Public evidence: reviewable patch, tests, benchmarks, change description. Until maintainers merge it, say “submitted / prepared a patch,” not “officially adopted.”

### 6.5 Interview topics and common mistakes

Questions and answer directions: (1) Why does the graph algorithm have its stated time / space complexity? (2) How does topological sorting detect cycles? (3) What bugs can pointer lifetimes and container reallocation cause? (4) How is incremental output checked against full recomputation? (5) Why fix build type and thread count in performance comparisons? (6) What misleading conclusions arise from tiny datasets? (7) Which actual call path executes your change, and how was that confirmed? (8) Which semantic and performance changes arise when moving a Python prototype to C++?

Common mistakes: generic algorithm exercises without circuit understanding; papers without runnable baselines; calling any use of machine learning “intelligent EDA”; reporting a single best speed; ignoring memory or correctness during optimization; treating README edits as core-tool development experience.

Without commercial EDA: much training can use public software, compilers, tests, and graph algorithms. OpenROAD / Yosys provide real engineering code. Preserve license and contribution requirements; an external patch may require a CLA. Reading a real tool's source does not mean a student's implementation covers all its models, and one simplified algorithm does not establish industrial-scale capability. Resources: D5, D6, D13, D14.

## 7. Choosing a primary and an adjacent track

Compare two-week exploration evidence, courses, laboratory resources, and real JDs in the target location. Do not substitute “higher salary / supposedly easier” for fit. Prefer one primary track and one adjacent track:

| Primary | Reasonable adjacent track | Reusable material | Role-specific depth to retain |
|---|---|---|---|
| RTL | DV or FPGA | RTL, protocols, self-checking, timing | Microarchitecture and synthesizable implementation trade-offs |
| DV | RTL | Protocols, module understanding, assertions | Independent models, coverage, defect closure, verification reuse |
| PD / STA | RTL or EDA scripting | Digital timing, synthesis, Tcl | Constraint review, physical / timing closure |
| DFT | DV or STA | Mode verification, timing, scripts | Fault models, scan / ATPG, manufacturing-test reasoning |
| FPGA | RTL or DSP algorithms | HDL, pipelines, verification | Device resources, board debugging, actual system evidence |
| EDA development | STA / P&R / synthesis specialty | Circuits and data structures | Software correctness, algorithms, performance, engineering scale |

Review every 6–8 weeks: have exit criteria been met, have JDs become clearer, do resource gaps block core evidence, can the thesis reuse this work, and should the primary track change? A change should follow completed exploration and documented obstacles, not one difficult bug.

## 8. Checkable readiness for internship / graduate applications

These are this Skill's training checks, not universal employer hiring thresholds:

1. Obtain real target JDs and map each requirement to “evidence available / gap to fill / not applicable / resources unavailable for now.”
2. Complete at least one core project at L3: independently explain the design, diagnose failures, and let another person reproduce it. Use another small project to fill a skill gap left by the main project.
3. State conditions for every résumé result, such as “with a public teaching library at the specified corner and constraints” or “measured on this board model.” All numbers come from logs; leave unmeasured items blank.
4. Explain the project for 10–15 minutes without reading AI output and solve a new small problem using the same core skill. Do not conceal AI-assisted work as wholly independent work.
5. Include debugging, trade-off, and collaboration / review records. Separate real defects from teaching injections and honestly record when no real failure occurred. A small, complete project is stronger than a large one that cannot be explained.
6. Explicitly list remaining resource gaps: for example “UVM reading and partial experiments only,” “FPGA not board-tested,” or “commercial signoff not performed.” Plan opportunities to obtain missing evidence; never rewrite gaps as completed work.

## 9. Evidence boundaries of this file

Course ordering, hour budgets, project specifications, and acceptance thresholds are educational planning recommendations, not a company's universal hiring standard. Official tool material is used to check scope, inputs / outputs, and limitations. This file is not a local vacancy, salary, admission-probability, or comprehensive employer-sampling survey. Resource links, check dates, and tasks are in [resources-digital.md](resources-digital.md). Read the student's JDs, baseline, and resources before reprioritizing this guidance for an individual plan.
