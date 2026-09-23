# Resource Library B: Analog, Devices, Manufacturing, Packaging/Test, and Applications

Brand: 我的模拟电路世界. Source verification date: 2026-09-22.

Select resources only for the current role and skill gap. At each stage, use at most one main course, one official tool document, and one project; more resources do not mean learning is complete. The prerequisites, exercises, acceptance criteria, and time estimates below are this Skill's teaching plan, not promises made by the resource authors. Official pages may change; versions, licenses, and supported platforms must be checked on the actual download page. Do not seek cracked EDA, leak PDKs, or bypass licensing.

## R1. Device and Circuit Foundations: MIT OCW 6.012

- Source: [Microelectronic Devices and Circuits, Fall 2009](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/), an official MIT course. The cited verification confirmed coverage of microelectronic devices, junction/MOS physics, circuit models and analysis, with learning materials such as lecture notes and exercises.
- Relevant tracks: A1 analog and A3 devices; students in A2/A4 can select chapters for specific gaps.
- Prerequisites: calculus, basic circuits, and electric potential/field concepts. If KCL/KVL and RC transients are unfamiliar, study those course sections first.
- How to learn: initially select PN junctions, MOS, small-signal equivalent models, and amplifier sections. For each session, first draw the physical/equivalent model, independently solve one problem, then use simulation to check orders of magnitude. Allow 30–50 hours for targeted study.
- Acceptance: derive a bias point and small-signal gain without the solution; explain approximation conditions; retain three incorrect solutions and corrections. Watching videos or finishing notes does not establish L2.
- Limits: the course is older but its foundations are stable. It does not replace the target PDK, advanced-device topics, or current tool practice. Follow course-page licensing; do not redistribute the full notes as your own textbook.

## R2. Analog Applications Foundations: TI Precision Labs – Op Amps

- Sources: [official TI op-amp course](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html) and [Stability Introduction](https://www.ti.com/video/4080235259001). The cited verification confirmed short videos and quizzes/exercises, with op-amp bandwidth knowledge expected before introductory stability material.
- Relevant tracks: feedback/noise supplements for A1, A6 test, and A7 applications. It emphasizes op-amp applications and measurements; it cannot independently establish transistor-level IC design ability.
- Prerequisites: ideal op-amps, RC circuits, and Bode plots. Study input/output range → bandwidth → stability → noise rather than jumping to the most complex topics.
- Exercise: change load capacitance at the same closed-loop gain and predict the response; add compensation and compare; prepare an input-error budget and integrate noise, recording whether the model includes the relevant noise sources.
- Acceptance: an error/noise budget with units, frequency band, and sources; a set of unstable/before-and-after-improvement simulations; an explanation of the phase-margin measurement method. Allow 20–35 hours; completing the entire site is unnecessary.

## R3. Accessible SPICE: Choose ngspice or LTspice First

- Sources: [official ngspice tutorial](https://ngspice.sourceforge.io/ngspice-tutorial.html), [official ngspice documentation](https://ngspice.sourceforge.io/docs.html), and [official Analog Devices LTspice page](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html). Entry points were verified on 2026-09-22. ngspice documentation and tutorial examples may use different versions; consult the manual for the installed version.
- Relevant tracks: A1, A6, A7. ngspice supports netlist/script practice; LTspice can simulate supported device macromodels and circuits. Test syntax/model compatibility between simulators; do not assume interchangeability.
- Prerequisites: circuits, device models, and basic text-file operations.
- Exercise: one minimal netlist each for DC/AC/transient; sweep three parameter combinations and export raw data; deliberately create and diagnose a floating node and incorrect stimulus. Allow 10–20 hours for foundations, then consult documentation during projects.
- Acceptance: rerun from a clean directory; record version, model source, inputs, logs, and measurement commands; hand-calculate one result. Without a PDK, label MOS/macromodel simulations at the principles/applications evidence level.
- Licensing: check tool and model licenses separately. A free tool does not make every downloadable model redistributable.

## R4. Open-Source PDK Learning Entry Point: SkyWater SKY130

- Sources: [official SkyWater PDK project documentation](https://skywater-pdk.readthedocs.io/en/main/) and [official project repository](https://github.com/google/skywater-pdk). The page explicitly labels the open release an experimental preview/alpha and advises against production use. This limitation was still present on the pages verified on 2026-09-22.
- Relevant tracks: legitimate PDK practice for A1 and layout rules/device recognition for A2.
- Prerequisites: MOS, process layers, SPICE, and willingness to maintain matched tool versions/environments. Installation is not mandatory during the first week; start with R3 if appropriate.
- Exercise: select one valid device and check pins/model/rated conditions; inspect five specific design rules; run a small circuit. Before layout, confirm that current tools, rules, device extraction, and models actually match.
- Acceptance: list PDK commit/version, device name, model corner, rule configuration, test circuit, and reproducible run. Downgrade the claimed evidence level truthfully when LVS/PEX support is missing.
- Limits: public documentation does not guarantee that arbitrary download combinations work; some official verification subpages still contain TODOs. Passing an open educational flow does not establish production signoff or proficiency in a company's advanced process. Do not bundle PDK files with your Skill.

## R5. Layout Verification Responsibilities and Tool Entry Points

- Sources: [official Cadence: What are DRC and LVS in Physical Verification?](https://support1.cadence.com/public/docs/content/20514747.html), [official Magic site](https://opencircuitdesign.com/magic/), and [official Netgen site](https://opencircuitdesign.com/netgen/). The Cadence page supports the independent responsibilities of DRC/LVS. Magic/Netgen entry points were reachable, but page-body extraction was limited in the cited check; this does not establish verified installation instructions, current versions, or compatibility with every PDK.
- Relevant tracks: A2 and the post-layout stage of A1. For commercial flows, prefer documentation matching the university's legally licensed environment and PDK manual; do not apply an online rule deck for an unknown process.
- Prerequisites: circuit connectivity, device dimensions, and process layers. First identify exactly which schematic/netlist is compared with which layout.
- Exercise: complete DRC and LVS for a current mirror; deliberately add a short/open/parameter error, rerun, and repair it; back-annotate one critical net's parasitics if an extraction flow is available.
- Acceptance: retain the checker, commands/settings, input versions, rules, reports, and final conclusion for every run. Record schematic check, Spectre execution, DRC, and LVS as four independent statuses. Allow 20–40 hours initially; difficulty depends on environment maturity.
- Limits: no LVS pass without a checker report; no foundry-signoff claim without the official matching flow.

## R6. TCAD Tool Responsibilities: Official Synopsys Overview

- Sources: [TCAD overview](https://www.synopsys.com/manufacturing/tcad.html), [Sentaurus Process](https://www.synopsys.com/manufacturing/tcad/process-simulation/sentaurus-process.html), and [Sentaurus Device](https://www.synopsys.com/manufacturing/tcad/device-simulation/sentaurus-device.html). The cited check confirmed that Process models process steps/structural evolution, while Device models electrical, thermal, optical, and other device responses. Available features/models still depend on license and version.
- Relevant tracks: A3 and process–device relationships in A4.
- Prerequisites: semiconductor physics, PN/MOS, electric fields/carrier transport, and unit checking.
- How to learn: use product pages to establish scope, not as complete tutorials. With a legal university license, start from local official introductory examples: PN junction → MOS → mesh/step size → parameter extraction. Retain the sources of the matching official version documentation. Allow 20–40 hours for the first explainable benchmark.
- Acceptance: explain where the structure comes from, which models are enabled, how boundaries are set, and why the solution converges; compare three mesh levels. Launching Workbench, finding an executable, or successfully querying a license does not mean the deck ran correctly.
- Limits: do not recommend leaked installation packages, licenses, or process decks. A tool's ability to describe a device does not mean its defaults are calibrated to the target process.

## R7. Without Commercial TCAD: DEVSIM

- Source: [official DEVSIM site](https://devsim.org/). The cited check confirmed a semiconductor-device numerical-simulation project entry point and documentation links.
- Relevant tracks: equations, discretization, and device benchmarks in A3; it does not replace all commercial TCAD models/process modules.
- Prerequisites: PN junctions, Poisson/continuity equations, Python, and numerical-convergence concepts. If these are weak, first practice an analytical PN junction.
- Exercise: start from a simple device example supported by current official documentation and change only one physical quantity. Compare analytical limits and three mesh levels, recording solver failures. Check installation against actual system documentation; do not promise direct Windows compatibility for arbitrary versions.
- Acceptance: complete input/model definitions, version, mesh, logs, and explanations; declare whether real-data calibration exists. Allow 25–45 hours for a first benchmark.

## R8. Statistics, DOE, SPC, and Reliability: NIST/SEMATECH e-Handbook

- Sources: [official NIST handbook](https://www.itl.nist.gov/div898/handbook/) and [process-capability explanation](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm). The cited check confirmed measurement, experimental-design, process-control, and reliability content. Process-capability interpretation assumes a stable process and appropriate distributional assumptions.
- Relevant tracks: A4, A5, A6, and fitting/measurement-uncertainty supplements for A3.
- Prerequisites: mean/variance, probability, and basic Python. Select one topic for the current project; reading the entire handbook is unnecessary.
- Exercise: create control charts and stratified analysis from sourced data; design a 2³ DOE; or analyze censored lifetime data. List assumptions first, calculate metrics second, and inspect model diagnostics last. Allow 15–25 hours per topic.
- Acceptance: separate control limits from specification limits; state sample-independence/distribution assumptions; label synthetic data; do not combine drifting data into one Cpk; report uncertainty with lifetime conclusions.

## R9. Process and Manufacturing Responsibilities: Official TSMC Role Page

- Source: [2025 Campus Recruitment — Explore Our Roles](https://www.tsmc.com/static/english/careers/campus_recruitment_2025/index.html). The 2026-09-22 check could still read PIE, PE, EE, and advanced-packaging role descriptions. This is a 2025 campaign page, not evidence of current recruiting status.
- Relevant tracks: role selection in A4 and understanding packaging duties in A5.
- Prerequisites: no additional technical prerequisites, but record personal preferences, location, and experimental resources.
- Exercise: rewrite PIE cross-module/product issues and PE module-variation control separately as “inputs—actions—deliverables”; compare them with three current official JDs in the target region. Allow 2–3 hours for the first comparison.
- Acceptance: explain the chosen role, how a project supports it, and three current gaps. Without current JDs, label the result “generic profile awaiting calibration.”

## R10. Packaging and Thermal Analysis: Official TI Packaging Resources

- Source: [SMT & packaging application notes](https://www.ti.com/design-development/packaging/smt-application-notes.html). The cited check confirmed an entry listing IC Package Thermal Metrics and packaging/assembly resources. Search results identified documents such as SPRA953D (2024 revision), but direct PDF retrieval failed in that check. Therefore, **do not cite specific formulas/clauses from it that were not verified page by page**. When studying, open the current document through this entry and record its revision.
- Relevant tracks: A5 and board-level thermal analysis in A7.
- Prerequisites: heat flow, power, steady-state temperature rise, and units.
- Exercise: compare the definitions and conditions of θJA, θJC, and ψJT. Perform parameter sensitivity for the same device under two PCB/boundary configurations; do not directly transfer package-table values between scenarios.
- Acceptance: every parameter has a source, unit, boundary conditions, and applicability explanation; complete a reproducible thermal RC exercise. Allow 8–15 hours initially. Actual junction-temperature validation needs an appropriate measurement chain.

## R11. Reliability Evidence Entry Points: TI Quality & Reliability

- Sources: [quality/reliability overview](https://www.ti.com/quality-reliability/overview.html), [official FAQs](https://www.ti.com/quality-reliability/faqs.html), and [General quality guidelines](https://www.ti.com/quality-reliability/quality/guidelines.html). The cited verification confirmed explanations of device quality/reliability and qualification frameworks; these pages do not replace a specific device's qualification report or the full standard text.
- Relevant tracks: A5, A6.
- Prerequisites: failure mechanisms, samples, and statistics; first identify the mechanism to be verified.
- Exercise: select a public product and inspect its public qualification information. Tabulate “device/package/conditions/basis/missing information,” then design a mechanism-driven verification plan.
- Acceptance: distinguish design verification, qualification, production monitoring, and customer field failures. Mark unavailable public information as missing. Allow 6–12 hours.
- Limits: verify JESD, AEC, and other standards' versions, clauses, sample counts, stresses, and usage rights against current official texts separately. Do not fabricate a “pass under the latest standard.”

## R12. Instrument Automation: Official PyVISA Documentation

- Source: [Communicating with your instrument](https://pyvisa.readthedocs.io/en/latest/introduction/communication.html). The cited check confirmed resource opening, communication settings, and troubleshooting guidance. Use documentation matching the local library version.
- Relevant tracks: A6, A7.
- Prerequisites: Python functions/exceptions/files, instrument operation, and laboratory rules.
- Exercise: first write a mock that permits injected errors. Then use a laboratory-authorized instrument to read identification and a known quantity, configuring timeouts and terminators. Follow each instrument model's manual for SCPI commands; do not assume complete uniformity.
- Acceptance: complete device ID, communication parameters, command logs, timestamps, units, and raw data. Disconnection and timeouts must produce explicit failures. Review commands that change output/range before connecting hardware. Allow 8–15 hours for software foundations; actual equipment validation is additional.
- Limits: PyVISA is a communication tool, not proof of calibration, measurement correctness, or compatibility. Mock output is not physical measurement.

## R13. ADC Testing: Official Analog Devices Technical Resources

- Sources: [INL/DNL Measurements for High-Speed ADCs](https://www.analog.com/en/resources/technical-articles/inldnl-measurements-for-types-of-highspeed-adcs.html) and [System Applications Guide — Section 16: Techniques for Verifying High Speed ADC Performance](https://www.analog.com/media/en/training-seminars/design-handbooks/system-applications-guide/Section16.pdf). The cited page/PDF-summary verification confirmed static/dynamic ADC testing content. The material is older; basic methods remain useful, but specific equipment/product recommendations need fresh verification.
- Relevant tracks: A6 and the acquisition specialization in A7.
- Prerequisites: quantization, sampling, FFT, noise/distortion, and basic statistics.
- Exercise: first validate analysis scripts using a known ideal quantizer/synthetic sine wave; then process actual board data, recording sampling, input, window, frequency bins, source quality, and clipping/overflow.
- Acceptance: state the reference definitions for INL/DNL and the conditions of the SINAD→ENOB conversion; provide raw samples and scripts; distinguish possible contributions from the ADC, source, clock, and acquisition chain. Allow 15–25 hours.
- Limits: nominal ADC bit count is not measured ENOB. Without a valid dynamic-test chain, report only supported static results.

## R14. Applications/FAE Work Context: Official TI Introduction

- Source: [A day in the life: TI Field Applications Engineer](https://www.ti.com/video/6351499567112), an official video entry verified on 2026-09-22.
- Relevant tracks: A7 role exploration. Use it to understand customer/technical collaboration, not to infer every company's duties, pay, travel, or working hours.
- Prerequisites: prepare a small circuit you completed and understand its specifications/limitations.
- Exercise: explain the same project in two versions: verification evidence for engineers and constraints/trade-offs for product colleagues. Simulate an unclear customer issue, asking answerable clarifying questions before proposing a solution.
- Acceptance: a 5-minute explanation that covers requirements, solution, evidence, limitations, and next steps. Do not invent real customer cases or automatically send external email. Allow 2–4 hours of exploration, then integrate communication practice into projects.

## Resource Use and Update Protocol

1. Recommend only resources directly tied to this week's deliverable. State which part to read, what to do, how to pass, and the expected effective study hours.
2. If a link fails, first seek a current entry from the same institution; do not silently substitute an unknown download site. Reachability only establishes an entry point. Installation, login, licensing, and execution still require local verification.
3. Recheck JDs whenever creating an application plan. Foundational courses can be reused; tool versions/licenses, standard clauses, and hardware prices require verification for the current task. Without browsing, label “not verified online” and ask the student for materials or use existing legal documentation.
4. Cite only necessary conclusions and links; do not reproduce entire textbooks, courses, standards, or commercial manuals. Student projects should retain author, title, version/date, and relevant pages/sections.
5. This file does not verify that installation commands were executed, commercial licenses are available, a PDK supports production signoff, physical samples meet measurements, or an employer is currently hiring. Project numbers and hours are educational planning suggestions; recheck feasibility for each individual plan.
