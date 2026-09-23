# Role Library B: Analog, Devices, Manufacturing, Packaging/Test, and Applications

Brand: 我的模拟电路世界. Edition: 1.2.0. Source verification date: 2026-09-22.

This library supports planning. The agent should read only the student's selected primary track and one adjacent backup track; do not assign all seven tracks to one person. Every numerical project target is an **illustrative educational acceptance criterion designed for this Skill**, not a universal hiring standard or a process-performance guarantee. Freeze specifications only after confirming equipment, models, budget, degree length, and supervisor-assigned work. Actual requirements depend on the specific team's current job description (JD), recruitment cycle, and location.

Contents: 0 Shared standards; A1 Analog/mixed-signal; A2 Analog layout; A3 Devices/TCAD; A4 Process/manufacturing; A5 Packaging/reliability; A6 Test/product; A7 Applications/FAE; 8 Personal planning; 9 Sources and limitations.

## 0. Reading rules and shared evidence standards

### 0.1 Priorities and proficiency levels

- P0: foundational capabilities to develop first in this track; P1: differentiating capabilities; P2: extensions. For an entry-level search, bring P0 capabilities to L2–L3, produce L3 evidence in at least one area, and then develop P1. These are learning targets, not identical requirements at every employer. Record explicit employer requirements and preferred qualifications separately.
- L0: no exposure or unable to explain; L1: can explain principles and solve basic exercises; L2: can follow documentation to complete a minimal experiment and explain its results; L3: can independently complete a module or experiment, diagnose faults, and submit reproducible evidence; L4: can make or optimize trade-offs under constraints and have the work reviewed. L4 does not mean senior engineer.
- Table levels are stage targets. Determine the student's current level from a diagnostic exercise, project files, logs, or a live demonstration, never merely from having attended a course or used a tool.
- Week estimates assume 12–15 hours of actual scheduled tasks per week, excluding normal classes, supervisor-directed research, and equipment waiting time. An individual plan should still schedule only about 80% of net available time H, leaving 20% as a buffer: if H is 12 hours, schedule about 9.6 hours of tasks and extend the calendar. Stages are sequential. Project time is already included in stage training and must not be added twice; equipment waiting time is not free. With only 6–8 hours per week, reduce concurrent tasks first and reschedule using observed progress.

### 0.2 Keep circuit and hardware evidence at distinct levels

| Evidence level | What it can establish | What it cannot establish on its own |
|---|---|---|
| Analytical/behavioral simulation | Equations, topology, control logic, and trends hold within the model used | Performance in a production process; completed transistor-level IC design |
| PDK transistor-level simulation | Performance for the stated model version, corner, voltage, temperature, and testbench | Completed layout, passed LVS/DRC, or successful tape-out |
| Layout verification and post-layout simulation | DRC, LVS, PEX, and post-layout results for the specified layout/schematic, rules, and extraction configuration | Production signoff, qualified reliability, or passing physical measurements |
| Physical measurements | Measured results for specified samples, equipment, calibration/settings, environment, and procedures | Guaranteed performance under untested conditions, production yield, or lifetime |

**A successful Spectre/ngspice run or error-free Check and Save is not an LVS pass.** LVS requires a dedicated checker, the compared layout and schematic/netlist, rule version, full report, and final matching conclusion. DRC, ERC, antenna rules, EM/IR, and PEX are separate checks. If a report includes waivers, say “with approved waivers,” not “zero errors.” Do not claim foundry signoff without the actual authorized signoff flow. See the [official Cadence explanation](https://support1.cadence.com/public/docs/content/20514747.html) for the distinction between circuit simulation and physical verification.

Every project must retain: `spec.md`, source/license notes, environment and versions, runnable inputs, raw results, metric-extraction methods, a pass/fail matrix, analysis of genuine failures or explicitly labeled educational fault experiments (record an all-pass result truthfully too), individual contributions, and a reproduction entry point. Publish only material you have permission to disclose; do not leak PDKs, models, rule files, or supervisor/company data through GitHub. Follow laboratory access and operating procedures when using equipment; without access, use simulation or public-data branches.

## A1. Analog / Mixed-Signal IC Design

### Target roles and fit

Target roles: analog IC design engineer and mixed-signal design engineer. Later specializations include power management, data converters, clocks/PLLs, interfaces, or sensor front ends. Do not select all specializations. During the first graduate year, use one OTA/comparator project to assess whether you enjoy sustained analysis, parameter tuning, operating-point debugging, and specification trade-offs.

Typical deliverables: module specifications, architecture and error/noise budgets, transistor schematics, testbenches, PVT/statistical verification matrices, layout constraints, post-layout reports, and test plans. This track suits students willing to calculate by hand, iterate, and investigate currents, voltages, and physical mechanisms. If your main interest is PCB design, first try the applications track; if you prefer spatial structures and interconnects, try analog layout. Lack of commercial EDA does not prevent starting, but clearly identify the evidence level you have actually completed.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | MOS operating regions, gm/ro, body effect, parasitic capacitance; L2–L3 | Hand-calculate a bias point; sweep ID–VG/ID–VD; explain deviations from the model; include units |
| P0 | Small-signal analysis, differential pairs, current mirrors, feedback, and compensation; L3 | Derive a simplified gain/pole model from the circuit, then cross-check against AC and transient analysis |
| P0 | DC/AC/transient/noise simulation and log reading; L3 | Independently build a testbench and diagnose a floating-node, bias, convergence, or measurement-window error |
| P0 | Specification decomposition and PVT verification; L2–L3 | Map every metric to stimulus, measurement formula, conditions, and pass/fail; retain failing corners |
| P1 | Mismatch, Monte Carlo, input noise, PSRR/CMRR; L2–L3 | Distinguish process variation from mismatch; document model support, seeds/sample counts, and statistical uncertainty |
| P1 | Layout feasibility and parasitic back-annotation; L2 | Complete a constraint handoff with a layout partner; compare pre/post results and explain their causes |
| P1 | Python/scripted batch processing; L3 | Automatically generate a metric table and manually cross-check three randomly selected points |
| P2 | One specialization such as ADC/PLL/LDO/SerDes; L2, with optimization goals potentially at L4 | One independent submodule with a system budget and at least two trade-off alternatives |

### Prerequisites and learning sequence

Dependency chain: circuit analysis and complex-number/Laplace basics → MOS and biasing → small-signal analysis → feedback/stability → noise and mismatch → metric-driven design → layout constraints/post-layout simulation. If prerequisites are missing, cover the first two stages before trying PLL design; memorized conclusions are no substitute.

1. Weeks 1–3: hand calculations and simulations for MOS devices, current mirrors, and common-source stages. Submit only three plots and their derivations each week. Acceptance: predict the direction of change after altering a load/bias, then simulate.
2. Weeks 4–7: differential pairs, a single-stage OTA, and unity-gain feedback. Separate open-loop gain, closed-loop bandwidth, slew rate, and stability. Acceptance: explain why large-signal and small-signal responses differ.
3. Weeks 8–15: complete the core project; freeze an updated specification table and failure list every two weeks. Establish nominal behavior before expanding corners, avoiding blind parameter sweeps that conceal structural errors.
4. Weeks 16–23: deepen either statistical verification or post-layout simulation; do both only if resources allow. Acceptance: explain the actual differences obtained under different conditions and prioritize genuine failure reviews. If every condition in the original specification range passes, record that truthfully. A separate, explicitly labeled educational fault injection or boundary exploration is allowed; do not present it as a genuine failing process corner.
5. Weeks 24–28: align with one specialization and prepare a 10-minute design explanation plus a live reproduction task. In a three-year degree, deepen the research topic into an advanced project during year two; in a two-year degree, prioritize a complete core-project delivery.

### Three project tiers

**Minimal project: five-transistor OTA or single-stage differential amplifier (2–3 weeks).** Select a legally available model, keep VDD within its rated range, and fix one bias and load first. Educational targets: DC gain ≥30 dB, functioning negative feedback, and a documented input range without output clipping. Submit four evidence categories: operating points, hand calculations, AC analysis, and small-signal steps. Within the hand calculation's valid approximation region, target a gain-estimate/simulation difference ≤30%; explain larger differences instead of deleting them. Diagnose in this order: supplies/body connections → branch currents/saturation → common-mode/output range → measurement nodes/stimulus → model/numerical settings. One gain-curve screenshot is not a complete pass.

**Core project: two-stage compensated OTA (6–8 weeks).** A feasible example specification, using a PDK with suitable 1.8 V devices: VDD=1.8 V, CL=2 pF, nominal gain ≥60 dB, UGB ≥5 MHz, phase margin ≥60°, and quiescent power ≤1 mW. Redefine the specifications first if the actual devices are unsuitable. Budget gm/current/capacitance before building open-loop and closed-loop testbenches. Define the loop-break point and preserve bias; do not read phase margin directly from closed-loop phase. Freeze supply range, temperature range, and available PDK corners, then verify each requirement. Mark only executed conditions as passed. Educational acceptance: nominal specifications met, verification matrix 100% completed, and a cause or next action for every failure. Count “all corners meet specifications” separately from “corner checks completed.” Include before/after compensation comparisons, genuine failures or separately labeled educational fault injection, design changes, and regression results. Retain an all-pass original specification matrix truthfully; no particular corner is required to fail.

**Advanced project: choose one branch (8–12 weeks or longer).** ① OTA layout—DRC/LVS—PEX—post-layout simulation; predefine an educational budget such as UGB degradation ≤20% and PM ≥55°, and explain parasitics that exceed it. ② Behavioral budgeting for an approximately 8-bit, 1 MS/s SAR ADC plus a comparator/CDAC submodule; report behavioral simulation and transistor implementation separately. ③ LDO stability and transients for explicit load, capacitance, and ESR ranges. Report PPA/noise/accuracy trade-offs and retain genuine failures. Without statistical models, perform parameter-sensitivity analysis and do not label it “process-mismatch Monte Carlo yield.” Without physical hardware, do not write “successful chip testing.”

### Interviews, pitfalls, and resource-limited alternatives

Practice: sketch signal and bias paths without slides; explain the cost of increasing gm; explain long large-signal recovery despite AC stability; give a 5-minute root-cause account of a genuine failure or clearly labeled educational fault, stating truthfully if the original tests all passed; explain a measurement expression live. Common pitfalls: replacing design work with book lists, testing only typical conditions, equating disappearance of an error message with circuit correctness, or copying a circuit without a specification budget.

Without commercial tools: use ngspice or LTspice for principles. Op-amp macromodels alone support only board-level/behavioral conclusions. A legally available open-source PDK can support exercises in its specified flow, but does not establish experience in a target employer's advanced node. Without tape-out, write “completed PDK simulation/post-layout simulation” and demonstrate capability through diagnosis, reproducible packages, and budgets. Suggested resources: R1, R2, R3, R4, R5.

## A2. Analog Layout

### Target roles and fit

Target roles: analog layout design engineer and custom layout engineer, potentially covering analog, mixed-signal, and custom memory cells. Deliverables: hierarchical layout; implemented matching/isolation/routing constraints; DRC/LVS reports; parasitic extraction; ECO and version records. This suits students who value detail, enjoy spatial organization, and repeatedly check circuit connectivity and geometry. Layout is more than connecting wires, and visual symmetry is not proof of electrical matching.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | MOS/resistor/capacitor layout structures, body connections, and net recognition; L2 | Map schematic instances, parameters, ports, and layout devices one by one |
| P0 | Reading layer, spacing, enclosure, density, and related rules; L2–L3 | Explain five kinds of actual DRC errors; record rule IDs, coordinates, and before/after fixes |
| P0 | Current-mirror/differential-pair matching, fingering, and dummies; L2–L3 | Device-splitting table, centroid positions, orientations/environments, and routing strategy |
| P0 | DRC and LVS; L3 | Separate reports for the same final version; deliberately introduce and then diagnose an open, short, or parameter mismatch |
| P1 | PEX, sensitive nodes, shielding/isolation, and parasitic budgets; L2–L3 | Critical-net R/C ranking, pre/post simulation differences, and ECO evidence |
| P1 | Awareness of supply paths and reliability rules; L2 | Justify routing using process rules and current constraints; do not invent allowable current density from experience |
| P2 | SKILL/Tcl/Python automation and hierarchical reuse; L2, with constraint optimization potentially at L4 | Generation/checking scripts and manual spot checks; compare area and critical-parasitic trade-offs |

### Prerequisites and learning sequence

Dependency chain: schematics/device terminals → process layers and valid devices → basic DRC/LVS → matching/placement → module layout → PEX/ECO.

1. Weeks 1–3: lay out a transistor, inverter, and resistor; read rules; create a version manifest for every run. Acceptance: locate the schematic instance corresponding to an LVS-extracted device.
2. Weeks 4–6: current mirrors and differential pairs; write constraints before drawing. For each matching arrangement, explain the gradients it addresses and the problems it does not solve.
3. Weeks 7–13: core OTA layout. Start with floorplan, pins, supplies/body connections, then critical devices, critical nets, other nets, and finally requirements such as density.
4. Weeks 14–20: PEX and ECO; compare critical parasitics and performance; turn two fixes into case studies. Advanced-node experience requires an authorized environment and cannot be gained by modifying images.

### Three project tiers

**Minimal project: 1:1 current mirror + matched differential pair (2–3 weeks).** Specify device dimensions, branch ratios, ports, wells/taps, and dummy connections; map 100% of target devices. Quantitative acceptance: zero unaddressed DRC violations under the selected rules and a matching LVS result. Measure the difference in the two critical routes' lengths/extracted R/C; freeze an educational target such as ≤10% beforehand. Explain unmet targets through loads and constraints; visual symmetry alone is insufficient. Diagnose: pin labels → body/supply global nets → opens/shorts → finger/multiplicity parameters → extracted device types. Include a connectivity mapping table and reports before/after fault injection.

**Core project: independently lay out a five-transistor or two-stage OTA (6–8 weeks).** Use a frozen transistor-level schematic and list constraints for differential inputs, mirror nodes, compensation nodes, and supplies. Estimate the area ceiling from total device area and legal spacing; do not impose unrelated advanced-node numbers. Acceptance: clear final DRC/LVS status and usable PEX back-annotation. Compare gain/UGB/PM/power with the same testbench, listing every pre/post difference and budget outcome. Capacitance-only extraction is not full RC post-layout simulation. Portfolio: floorplan, sensitive-net annotations, final layout, report summaries with traceable run IDs, and explanations of two ECOs.

**Advanced project: analog submodule with isolation and hierarchical interfaces (8–12 weeks).** Choose a comparator, bias network, or op-amp; add boundary, pin, shield, guard-ring, and reuse requirements. Check available ERC/antenna/density rules using the actual PDK. Quantitative acceptance: reduce area or critical parasitics relative to a baseline while retaining DRC/LVS and key electrical performance; for example, choose one improvement target ≥10%. Disclose changes in other metrics. An unmet improvement target can still support a valid trade-off analysis; do not hide regressions. Have another student or supervisor reproduce the check from the same inputs.

### Interviews, pitfalls, and resource-limited alternatives

Practice: explain common-centroid assumptions and limitations; explain electrical asymmetry despite geometric symmetry; trace an LVS parameter mismatch layer by layer; distinguish a guard ring from signal shielding; identify the source of post-PEX slowdown. Pitfalls: submitting only colored layout screenshots, deleting a rule waiver and calling it a fix, equating DRC clean with LVS clean, or treating an educational rule deck as production signoff.

Without Virtuoso, try a compatible Magic/Netgen flow for a legally available open-source PDK, verifying that tools and rules really match. Drawing/viewing in KLayout without device extraction and LVS configuration does not establish a complete flow. If rules/extraction are missing, submit geometric/connectivity exercises and retain the corresponding L1–L2 level; do not fabricate reports. Suggested resources: R4, R5.

## A3. Devices / TCAD / Device Modeling

### Target roles and fit

Target roles: device engineer, TCAD engineer, and device-modeling engineer. Use each JD to distinguish device development, process modeling, and compact-model extraction. Deliverables: structure/mesh/physical-model inputs, solver/convergence records, I–V/C–V and parameter extraction, model calibration/validation, sensitivity analysis, and design recommendations. This suits students interested in physical mechanisms, mathematics, and data, with a willingness to check units and numerical convergence. Producing a single contour plot is insufficient evidence.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | Band diagrams, carrier statistics, PN junctions, MOS, and drift-diffusion; L2 | Explain two bias states using bands and boundary conditions; estimate orders of magnitude |
| P0 | Mesh, boundaries/contacts, materials, and physical-model selection; L2–L3 | Table justifying enabled models; convergence comparison for at least three mesh levels |
| P0 | DC sweeps, solver convergence, and anomaly diagnosis; L3 | Raw logs, bias sweeps, failed points, and retry strategy; do not erase failures |
| P0 | Python data cleaning and Vth/SS/DIBL extraction; L2–L3 | Formulas, intervals, units, methodological consistency, and manual cross-checks |
| P1 | Model calibration against measured data, parameter identifiability, and held-out validation; L2–L3 | Separate fitting/validation conditions; residuals, error definitions, and uncertainty |
| P1 | Process—structure—electrical-property links; L2 | A causal hypothesis and counterexample for a changed structural/process parameter |
| P2 | One of power devices, memory, irradiation, quantum transport, or compact models; L2, with constrained research potentially at L4 | Model selection, sensitivity, and extrapolation boundaries for one question |

### Prerequisites and learning sequence

Dependency chain: semiconductor physics → analytical PN/MOS approximations → numerics and units → TCAD benchmark → extraction and convergence → data calibration. Generating structures with process simulation and obtaining electrical properties with device simulation are different tasks. The [official Synopsys TCAD overview](https://www.synopsys.com/manufacturing/tcad.html) verifies tool scope; it is not a free-license portal.

1. Weeks 1–4: hand-calculate PN junctions and MOS capacitors; create a unit table; practice logarithmic plots and derivative-based extraction.
2. Weeks 5–8: reproduce a PN junction/MOS device from official examples before complex heterojunctions; test sensitivity to mesh, bias steps, and initial conditions.
3. Weeks 9–16: core MOS project with short-channel metrics and trend explanations. Prioritize reproducible curves and extraction over attractive contour plots.
4. Weeks 17–24: calibrate if legally usable measurements are available. Otherwise perform parameter sensitivity and analytical/numerical cross-checks, explicitly stating that the model is uncalibrated.
5. Weeks 25–30: choose a device type aligned with the target JD and prepare a 10-minute demonstration explaining why a parameter change changes a metric.

### Three project tiers

**Minimal project: one-dimensional PN junction (2–3 weeks).** Freeze material, doping, temperature, contacts, and sweep range; first estimate built-in potential/depletion width. Acceptance: equilibrium potential and low-bias analytical-approximation trends agree. In the approximation's valid region, choose depletion width or potential as the comparison metric and target a relative difference ≤10%; target <2% change in a key metric across three mesh levels. Distinguish analytical assumptions, boundaries, and numerical issues when explaining deviations. Evidence: input deck, mesh, logs, I–V, analytical comparison, and unit checks.

**Core project: two-dimensional MOSFET parameters and short-channel effects (6–8 weeks).** Freeze structure and models. Use at least three gate lengths, two drain biases, and two temperatures, all within model validity, giving at least 12 ID–VG data sets. Apply consistent Vth/SS/DIBL extraction definitions. Acceptance: trace every result to an input combination; target <3% key-metric change after mesh refinement. Compare DIBL using the same extraction method; do not fit SS over arbitrary intervals. Diagnose: length/concentration units → contacts/boundaries → initial conditions and steps → mesh → model applicability. Never tune solver tolerances alone to make a nonphysical solution “pass.” Include a hypothesis, test, and alternative explanation for one key trend. If a counterintuitive result occurs, document its investigation; an anomalous trend is not required.

**Advanced project: measurement calibration and held-out-condition prediction (8–12 weeks).** Use your own measurements or licensed public data; first record source, temperature, device dimensions, and error. Select a small number of physically meaningful parameters instead of freely fitting everything at once. Freeze educational targets such as log-ID RMSE ≤0.15 decade and Vth deviation ≤30 mV. Evaluate only in an explicit current range and above the measurement noise floor; values below that floor are not accurate observations. Hold out a VDS/temperature/dimension group for validation and report fitting and validation errors separately. Without measurements, synthetic data may validate the calibration program, but the title must say “synthetic benchmark”; do not claim calibration of an actual process.

### Interviews, pitfalls, and resource-limited alternatives

Practice: why a finer mesh does not always mean greater physical accuracy; how to choose mobility/recombination/quantum corrections; why Vth differs between extraction methods; why a good fit can extrapolate poorly; the respective duties of process and device simulators. Pitfalls: treating default parameters as a real process, calling a 2D section an exact 3D result, transcribing data from a paper image without disclosing extraction error, or letting AI alter a deck without understanding the models.

Without a Sentaurus/Silvaco license: use [official DEVSIM resources](https://devsim.org/) or write one-dimensional equations for numerical-device practice, stating model/dimensional scope. This can establish physics and numerical capabilities, not commercial full-flow proficiency. Without experimental equipment, use clearly licensed public curves and record source/extraction error; without real data, retain a “not yet calibrated” field. Suggested resources: R1, R6, R7.

## A4. Process Integration / Unit-Process Engineering / Manufacturing

### Target roles and fit

Distinguish target roles at minimum: a **PIE (Process Integration Engineer)** addresses cross-module flows, device electrical properties, yield, and collaborative troubleshooting; a **PE (Process Engineer)** typically focuses on the process window, variation, and excursions in a particular module such as lithography, etch, thin films, diffusion, or CMP. An equipment engineer (EE) has different equipment-maintenance/efficiency duties. Abbreviations vary by employer; read the responsibilities. See the [official TSMC role descriptions](https://www.tsmc.com/static/english/careers/campus_recruitment_2025/index.html) for this distinction. That page describes roles and does not establish local vacancies in 2026.

Deliverables: process/key-parameter maps, split/DOE plans, SPC and metrology analysis, excursion isolation/root-cause verification, before/after improvement data, and change records. This suits students who respect practical constraints, enjoy data and experiments, and work across teams. Verify cleanroom, on-call, shift, and location requirements for each JD and let the student assess them; do not portray every role as having a fixed schedule.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | Main CMOS process sequence and key modules; L2 | Draw evolving cross-sections and identify electrical metrics a process change may affect |
| P0 | Statistics, distributions, confidence intervals, correlation, and causation; L2–L3 | Analysis retaining time/equipment/lot fields; do not treat repeated points in one lot as independent samples |
| P0 | SPC and the distinction between control/specification limits; L2–L3 | Check stability before discussing capability; retain and classify anomalies |
| P0 | DOE and problem decomposition; L2–L3 | Explicit factors, responses, randomization/blocking, replication, and confirmation experiments |
| P0 | Measurement error, data lineage, and laboratory EHS awareness; L2 | Measurement procedures and instrument/sample records; no unauthorized equipment operation |
| P1 | PIE: cross-module electrical/yield relationships, L3; PE: a module's process window, L3 | Hypothesis—evidence—exclusion—confirmation chain identifying personal responsibility |
| P1 | Python/SQL and lot/wafer/site analysis; L2–L3 | Rerunnable cleaning/plots with an audit trail for missing/anomalous-data handling |
| P2 | FDC, APC, defect-map classification, or TCAD process linkage; L2, with confirmed improvement potentially at L4 | Comparison against a simple baseline, cross-lot validation, and prevention of data leakage |

### Prerequisites and learning sequence

Dependency chain: process/metrology → data structures/statistics → SPC → DOE → module experiments/cross-module diagnosis. PIE students with weak device physics need MOS foundations; PE students should add materials, chemistry, plasma, or thermal-process knowledge according to their module.

1. Weeks 1–3: draw a CMOS flow, select one module, and map inputs—outputs—measurements—common failure relationships.
2. Weeks 4–7: statistics and Python; create a data dictionary and clean data before plotting; complete a measurement-repeatability exercise.
3. Weeks 8–12: SPC and minimal excursion localization; label statistical anomalies separately from out-of-spec results.
4. Weeks 13–20: core DOE project. Add cross-module electrical relationships for PIE or a process window for PE. If experiments are unavailable, explicitly identify public/synthetic teaching data.
5. Weeks 21–26: condense the project into an issue record and improvement report; seek a connection to authorized group experiments or an internship. A personal-computer simulation must not be presented as production experience.

### Three project tiers

**Minimal project: process-variation diagnosis (2–3 weeks).** Use 100–300 public or clearly labeled self-generated records containing date, lot, equipment, measurement, and units. Specification: detect predefined mean drift/variance changes; retain a blind test set when anomaly labels are unknown. Acceptance: traceable cleaning rules, explanations for three anomaly categories, and control limits from an appropriate baseline. Where synthetic labels exist, report precision/recall rather than only attractive plots. Diagnose: units/duplicate records → measurement changes → lot mixing → time sequence → process hypotheses. Portfolio: data dictionary, anomaly list, and one-page analysis.

**Core project: single-module 2³ factorial experiment + confirmation (6–8 weeks).** An educational example uses film thickness/etch depth as the response, with three factors and eight combinations. Choose replicates and center points according to resources/noise; copying one simulation does not create experimental replicates. Acceptance: explain main effects/interactions, inspect residuals, document randomization/blocking, and use at least three confirmation points excluded from fitting. An example target is confirmation-point error ≤10%, but define an appropriate response dimension and scale before starting. If it fails, investigate confounding, drift, the measurement system, and model form. Without equipment, call it a DOE analysis exercise. Hazardous chemical/process recipes may only be executed under laboratory procedures; this Skill does not provide directly executable hazardous recipes.

**Advanced project: PIE yield-problem resolution or PE process window (8–12 weeks).** PIE: relate a worsening electrical distribution to two process hypotheses, separate product/equipment/lot effects, and design an experiment that distinguishes the hypotheses. PE: identify a window for two competing responses. Quantitative acceptance: consistent baseline/improvement definitions, independent confirmation lots or an explicitly simulated holdout set, and reported effect size/uncertainty. Do not describe a defective fraction changing from 10%→8% as a “2% yield improvement” without specifying percentage points. Production claims require real data, actual execution, authorized disclosure, and review; if any are missing, describe the result as educational analysis.

### Interviews, pitfalls, and resource-limited alternatives

Practice: what high Cp but low Cpk means; why not to report Cpk directly for an unstable process; why the strongest correlation may not be the root cause; how to distinguish measurement drift from process drift; division of work between PIE and PE. Pitfalls: deleting every outlier, using specification limits as control limits, averaging mixed equipment populations, or equating machine-learning accuracy with yield improvement.

Without fab access: make process understanding, statistical scripts, and DOE designs reviewable, then pursue real metrology experience through course laboratories/shared university facilities. Do not promise equipment access or bypass admission requirements. Public/synthetic data can demonstrate analysis, not equipment tuning or process-introduction experience. Suggested resources: R8, R9, R6.

## A5. Packaging / Reliability / Failure Analysis

### Target roles and fit

These are related role families, not topics to learn all at once. Package design concerns structures and electrical/thermal/mechanical interaction; packaging process engineering concerns assembly flow and yield; reliability concerns failure mechanisms, stress tests, and lifetime evidence; failure analysis (FA) concerns localization and root-cause evidence. Choose one primary role first, then develop adjacent knowledge. Deliverables include models/boundary conditions, package concepts, test matrices, failure records, statistics, and conclusions; FA additionally requires sample traceability, localization evidence, and exclusion of alternative hypotheses.

This suits students with materials, mechanical, thermal, or device foundations who value cross-checking. Circuit students can enter through thermal/electrical parasitics; materials students through interfaces/stress/failure mechanisms. Running finite-element analysis is not reliability certification.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | Package structures, materials, interconnects, and process basics; L2 | One-page cross-section showing structure/materials/key interfaces and three risk hypotheses |
| P0 | Track foundations: conduction/stress/electrical parasitics or failure mechanisms; L2–L3 | Analytical order-of-magnitude checks against simulation/experiments, with boundary conditions |
| P0 | Experimental design, sample/failure definitions, and traceable records; L2–L3 | Criteria frozen before testing; complete sample IDs, stresses, and failure times |
| P0 | Uncertainty, censored data, and lifetime-inference limits; L2 | Distinguish not-yet-failed samples from unknown failure times; zero failures do not imply infinite life |
| P1 | Finite-element or thermal RC models and mesh independence; L3 | Three mesh/discretization levels, energy/unit checks, and sensitivity analysis |
| P1 | Reliability plans/FMEA/FA evidence chains; L2–L3 | Stress—failure mechanism—measurement—criterion mapping; exclude at least two alternative causes |
| P2 | SI/PI, electrothermal coupling, advanced packaging, or acceleration models; L2, with optimization potentially at L4 | One coupled problem with explicit parameter sources/applicability and reviewed trade-offs |

### Prerequisites and learning sequence

Dependency chain: structures/materials → basic physics/metrology → models/assumptions → verifiable experiments → reliability statistics or structural optimization.

1. Weeks 1–3: understand one package cross-section and assembly flow, such as QFN/BGA, and select the primary track.
2. Weeks 4–7: thermal RC/thermal-resistance or stress foundations, with analytical/numerical comparisons. Reliability students also study probability and censoring.
3. Weeks 8–15: core project. Freeze boundaries, material parameters, and verifiable quantities before adding complexity that cannot be checked.
4. Weeks 16–23: structural improvements/sensitivity or a reliability-verification plan; conduct prescribed tests when university equipment is available.
5. Weeks 24–28: write one failure case as hypotheses, evidence, missing evidence, and follow-up experiments; prepare an engineering presentation.

### Three project tiers

**Minimal project: thermal-path and dimensional audit (2–3 weeks).** Select a package/board scenario from public device information and calculate power and simplified temperature rise. Specify ambient temperature, heat-removal boundaries, and PCB conditions. Acceptance: target <5% difference between hand calculations and a thermal RC numerical solution using the same assumptions. Explain the different uses of θJA and ψJT; do not treat datasheet θJA as a constant for every PCB. Evidence consists of the model, parameter sources, and applicability, not a claim that physical junction temperature was verified. See the [TI packaging application-resource entry point](https://www.ti.com/design-development/packaging/smt-application-notes.html).

**Core project: package/board thermal model or reliability-data analysis (choose one, 6–8 weeks).** Thermal branch: fix one structure, two powers, three heat-removal conditions, and three mesh levels. Define steady-state educational acceptance as energy-balance error |P_in−P_out|/max(|P_in|, ε_P)<2%. Calculate mesh differences using temperature rise ΔT=T_hot−T_amb: |ΔT_fine−ΔT_coarse|/max(|ΔT_fine|, ε_T)<3%. Freeze ε_P, ε_T, and near-zero absolute tolerances before the project, and record the absolute temperature difference (K). Transients require a separate stored-energy term; do not apply the steady-state balance equation. If temperature measurements exist, report sensor error/contact effects and deviations; case temperature cannot simply be called junction temperature. Statistics branch: use sourced data with censoring indicators, labeling synthetic data as such; compare a nonparametric survival curve with a chosen distribution model. Acceptance: correct censoring treatment, reproducible parameters/confidence intervals, checks on held-out conditions, and explicit inference limits for zero-failure samples. Diagnose inputs/units/boundaries/censoring before debating physical mechanisms.

**Advanced project: structural improvement + reliability-verification plan (8–12 weeks).** Choose an educational target: peak temperature-rise reduction ≥10% at the same power/boundaries, or a reduction in a defined stress-concentration metric. Also report area, material, and manufacturability costs. The reliability track may instead produce a mechanism-driven verification plan specifying stress, monitoring, decisions, sample-selection basis, resources, and evidence gaps for each item. Without actual execution, do not claim passed HTOL/temperature cycling/HAST/AEC certification. Without the current standard text, do not invent duration, temperature, or sample count. High-temperature/high-pressure/high-humidity testing and destructive analysis require qualified facilities and supervision.

### Interviews, pitfalls, and resource-limited alternatives

Practice: whether thermal-table values can be directly reused; why finer meshes do not fix incorrect boundaries; mechanism assumptions needed for Arrhenius extrapolation; what zero failures establish; how to connect visible cracks with electrical failures through evidence. Pitfalls: colored contours without material sources, equating finite-element convergence with physical validation, treating correlated failure sites as root causes, or claiming product reliability from synthetic lifetime data.

Without commercial finite-element tools, train methods using inspectable thermal RC/analytical models or legally licensed solvers. Without acoustic microscopy/SEM/thermal chambers/stress equipment, reconstruct evidence from public cases and design experiments, retaining unverified fields. Recheck standard clauses, versions, and permissions each time; general webpages are only entry points. Suggested resources: R8, R10, R11.

## A6. Test / Product / Characterization and Validation

### Target roles and fit

Distinguish target roles: test engineers focus on test programs, coverage, test time, and hardware; product engineers focus on product introduction, yield, binning, and cross-functional resolution; characterization/validation engineers focus on device specifications, boundaries, and anomalies under operating conditions. Responsibilities often overlap; follow the specific JD. Deliverables: test plans, limits/units, automation programs, fixtures/connection diagrams, raw data, calibration/uncertainty notes, and yield/anomaly analysis.

This suits students who enjoy hands-on work, scripting, diagnosis, and checking data credibility. Either analog or digital backgrounds can fit, but a simulation testbench is not ATE experience, and connecting an oscilloscope is not complete characterization.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | Read datasheets and convert specifications into test items; L2–L3 | Stimulus, range, sampling, limits, units, environment, and exception action for every item |
| P0 | Supply/oscilloscope/DMM/signal-source basics and wiring; L2 | Actual equipment/probe settings; understanding of grounds, input impedance, and bandwidth limits |
| P0 | Python/data processing/instrument communication; L3 | Repeatable sweep, saved data, and timeout/error handling |
| P0 | Error, repeatability, pass/fail, and boundaries; L2–L3 | Manual/automated result comparisons and checks for units, missing values, and saturation |
| P1 | Characterization of one device class: ADC/DAC/power/digital interface; L3 | Complete raw static/dynamic-metric data under specified conditions |
| P1 | Yield/binning, anomaly localization, and test time; L2–L3 | Baseline/optimized results; time comparison without degraded coverage or accuracy |
| P2 | ATE platforms, correlation, multisite, and DFT interfaces; L2, with trade-offs potentially at L4 | Claim specific ATE practical experience only with actual access/course-platform records |

### Prerequisites and learning sequence

Dependency chain: circuits/datasheets → manual measurement → error/range/units → automation → coverage/statistics → product-issue resolution. Digital ATE requires timing, patterns, and basic DFT; analog testing requires sampling/FFT/noise.

1. Weeks 1–3: choose an accessible low-voltage evaluation board/device; document five key specifications; complete one manual measurement and error estimate first.
2. Weeks 4–6: Python/instrument communication; test with mocks before real equipment. Do not automatically send unverified commands that could change voltage/output.
3. Weeks 7–14: core project covering normal operation, boundaries, communication failures, and data anomalies.
4. Weeks 15–21: measurement correlation, repeatability, and test-time optimization; distinguish DUT, fixture, instrument, and script faults.
5. Weeks 22–26: write a product-issue record and prepare a 10-minute “from incorrect data to root cause” demonstration; add ATE or device topics according to the JD.

### Three project tiers

**Minimal project: automated DC sweep (2–3 weeks).** Choose a laboratory-approved low-voltage device and first freeze supply/current-limit/input ranges, or train on mock instruments using the same interface. Specification: 10 setpoints × 3 repeats; record time, device ID, setpoint, readback, units, and status. Acceptance: 30 traceable results, manual spot checks at three points, and error within a predefined instrument/system budget. Disconnection/timeouts must permit safe exit and an explicit incomplete status. Label mock results as simulated data. Portfolio: wiring diagram, operating procedure, raw CSV, and fault demonstration.

**Core project: characterize one ADC/power IC (6–8 weeks).** ADC example: use an existing approximately 12-bit evaluation board; measure DC transfer and repeatability, and SINAD/ENOB only when equipment supports valid measurements. Record sampling rate, input frequency/amplitude, window/coherent-sampling settings, sample count, and source purity. Acceptance: first validate static/dynamic scripts with known synthetic signals, then report metrics/error bounds for measurements; use at least 3 input conditions and ≥3 repeats per condition. If the source/acquisition chain is inadequate, submit static tests only; do not invent ENOB. The power branch may use load regulation/efficiency/startup as three metrics, with load range governed by laboratory procedures. Diagnose wiring/supplies → ranges/sampling → data format/clock → fixture → DUT.

**Advanced project: correlation and test efficiency (6–10 weeks).** Measure the same DUT through two paths or manual/automated flows, freezing limits and samples. Quantify bias, repeatability, boundary misclassification, and test time. An educational target may be total execution-time reduction ≥20%, requiring unchanged effective coverage, result deviations within budget, and traceable failures. Without real ATE, call it bench-automation optimization. Without multiple samples, do not claim population-yield conclusions. Include before/after comparisons with identical inputs, failure bins, and retest rules.

### Interviews, pitfalls, and resource-limited alternatives

Practice: first checks for low measured ENOB; separating DUT noise from source noise; range effects on error; whether test limits equal datasheet specifications; why higher yield after retest might reflect selection bias. Pitfalls: ignoring probe loading, automatically discarding failures, treating exception-free code as trustworthy measurement, or inferring production distributions from one device.

Without equipment: develop software-verification evidence through instrument mocks, data formats/FFT/limit decisions, and anomaly injection; then seek university shared equipment or internships rather than buying expensive instruments first. Without ATE access, retain bench/software capabilities and never fabricate platform experience. Suggested resources: R3, R8, R12, R13.

## A7. Applications Engineering / FAE

### Target roles and fit

Target roles: applications engineer (AE), field applications engineer (FAE), and technical-support/solutions engineer. AE often emphasizes product applications, evaluation boards, and reference designs; FAE often emphasizes customer requirement clarification, system component selection, field issues, and feedback. Actual divisions vary by company. See the [official TI FAE introduction](https://www.ti.com/video/6351499567112). Deliverables: requirements/constraints, component comparisons, error/power budgets, schematics/BOMs, validation results, problem-reproduction packages, and customer-facing technical explanations.

This suits students who enjoy communication, connect system problems to device details, and explain limitations clearly. Communication means accurately understanding requirements, narrowing problems through evidence, and advancing validation, not simply talking well. Check travel requirements/frequency for each job; FAE is not universally equivalent to sales, and AE is not universally IC design.

### Skills, levels, and evidence

| Priority | Skill and target | Inspectable evidence |
|---|---|---|
| P0 | Analog/digital interfaces, datasheet reading, and selection; L2–L3 | Compare two candidate devices under consistent conditions; distinguish typical/max values from absolute maximum ratings |
| P0 | Requirement clarification and budgeting; L3 | Convert “high accuracy/fast” into testable range, bandwidth, error, supply, cost, and other constraints |
| P0 | Simulation, board debugging, and measurement; L2–L3 | One minimal reproduction with raw waveforms, connections, settings, and hypothesis elimination |
| P0 | Technical writing/presentations and cross-team communication; L3 | One-page application note, 5-minute demonstration, and issue record separating facts/hypotheses/to-be-confirmed items |
| P1 | PCB return paths, decoupling, protection, and stability/EMI basics; L2–L3 | Design checklist and evidence of two actual fixes |
| P1 | One system class: power/sensors/acquisition/motors/interfaces; L3 | End-to-end project from requirements to a verifiable design, beyond assembling modules |
| P2 | Firmware, scripts, industry contexts, and English meetings; L2, with trade-offs potentially at L4 | Customer-style change request, English email draft, and automated demonstration; do not send to real customers without authorization |

### Prerequisites and learning sequence

Dependency chain: circuit fundamentals → datasheets/error budgets → SPICE → schematics/measurements → minimal reproduction → solution comparison/communication. Let system problems guide learning instead of memorizing hundreds of part numbers first.

1. Weeks 1–3: choose a low-voltage sensing/acquisition scenario; write requirements and compare two devices; identify the conditions under which guaranteed values apply.
2. Weeks 4–7: op-amp input/output ranges, bandwidth, noise, and stability. Change the circuit after each learning unit and record how one poor component choice was exposed.
3. Weeks 8–15: core front-end project; simulate first, then validate using existing boards/equipment; write operating instructions.
4. Weeks 16–21: two fault cases and one improvement proposal; practice explaining the same result to engineers and nontechnical colleagues.
5. Weeks 22–26: select a power/interface/sensor specialization according to the JD; simulate customer clarification and technical meetings, using datasheets/issue records for technical-English practice.

### Three project tiers

**Minimal project: op-amp selection and gain circuit (2–3 weeks).** Example specification: amplify 0–100 mV to approximately 0–2 V using an available low-voltage supply. First assess single-supply input/output ranges and bias. Compare two devices with complete public data; calculate offset, bias-current effects, resistor error, bandwidth, and output swing. Acceptance: complete requirements/candidate comparison; educational nominal DC gain-error target ≤1%; list untested temperature drift/device distributions as gaps. Use legally available manufacturer macromodels or declare an ideal model. Diagnose common-mode/output swing, supplies, and model pins before changing resistors.

**Core project: sensor front end + acquisition validation (6–8 weeks).** Example: 0–100 mV input, nominal gain 20, 0–2 V output, and an initial 10 kHz target bandwidth, revised for available ADC sampling rate and load. Add design explanations for anti-alias filtering, supply decoupling, and simple input protection. Acceptance: repeated measurements at at least 5 DC points and 3 frequency points; compare gain/bandwidth/noise/output range to budgets and attach a cause or next experiment to every excess. State the resolvable range when source/instruments limit measurements; do not report noise below equipment capability. Portfolio: BOM, datasheet sources, separate simulation/measurement columns, one fault reproduction, and a one-page application note.

**Advanced project: simulated customer changes and fault support (4–8 weeks).** Add two constraints to the core project, such as driving a long cable, input DC offset, or supply variation. Clarify conditions before proposing two alternatives, and compare accuracy/stability/power/cost and validation effort. Quantitative acceptance: at least two candidates, testable key requirements, and two minimal fault reproductions. After a 5-minute demonstration, another student should reproduce at least one test using the instructions. Without actual EMC testing, do not claim passed EMC certification. BOM prices require the actual lookup date and purchase quantity; leave fields blank when data are unavailable.

### Interviews, pitfalls, and resource-limited alternatives

Practice: conditions to clarify when a customer reports “too much noise”; why typical values alone cannot support recommendations; retaining the original problem before changing the circuit; separating probe artifacts from actual oscilloscope ringing; explaining trade-offs when requirements cannot all be met. Pitfalls: only listing brands/part numbers, immediately blaming the customer, guaranteeing operation without tests, or treating absolute maximum ratings as normal operating conditions.

Without PCBs/instruments: first complete requirements, budgets, licensed macromodel simulations, and fault injection, then seek existing university boards. These demonstrate selection/analysis, not hands-on hardware debugging. Without customer experience: use public cases or simulated requests and label the educational scenario; do not invent company/customer stories. Suggested resources: R2, R3, R12, R14.

## 8. Turning these seven tracks into an individual plan

1. Begin with a 2-week exploration, allocating only 3–4 hours to a small task for each candidate track. Also check the supervisor's topic, available tools, and actual JDs. Retain at most two candidates.
2. Select one primary track and record role keywords, current P0 levels, and evidence gaps to L2/L3. Reuse foundations/projects for an adjacent backup, for example analog→layout/applications, devices→PIE, or test→applications. Do not promise a cost-free transition.
3. Complete a minimal project, then one core project. Do not stack three long courses before passing the project. Resources and remaining job-search time determine whether to add an advanced project.
4. Review weekly using “this week's metrics—inputs and versions—raw results—failure diagnosis—next week's smallest action.” Every 4 weeks, have another person review proficiency against evidence.
5. In applications, describe projects as “what I did, under what conditions, with what results, where the evidence is, and what remains missing.” Do not overstate tool proficiency, claim an entire public tutorial as original work, or describe synthetic data as production data.

## 9. Sources and limitations of this file

Role organization, time estimates, skill targets, and project acceptance plans are this Skill's educational design. Official links verify courses, tool scope, and responsibility boundaries; they do not replace current JDs from target employers. The source access date is 2026-09-22; see [Resource Library B](resources-analog-process.md). Local vacancies, salaries, admission/hiring rates, visas, and academic screening rules for specific employers were not verified in this file; check them separately when generating an individual job-search strategy.
