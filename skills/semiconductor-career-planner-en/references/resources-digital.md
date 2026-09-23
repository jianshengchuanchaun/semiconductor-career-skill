# Digital-track resources: a focused set of learning and practice entry points

Author / brand: 我的模拟电路世界 (My Analog Circuit World). Resources checked: 2026-09-22.

This file supports [roles-digital.md](roles-digital.md). Choose one primary track. At each stage, open only the resources needed for foundational explanation, the current tool, and the current project; collecting links is not learning. Publicly readable pages do not imply that commercial software, IP, boards, or cloud resources are free. Tasks and hour recommendations are designed by this Skill, not official requirements of the resource authors' courses.

## 1. Minimal resource combinations by track

| Track | Use only these to start | Add when the project reaches that stage |
|---|---|---|
| RTL | D1 digital foundations, D2 simulation, D3 self-checking | D5 synthesis, D6 timing |
| DV | Timing foundations in D1, D2, D3 | D4 UVM; first confirm simulator feature support |
| PD / STA | D6 timing, D7 implementation flow | D5 synthesis; separate STA and PD depth according to the JD |
| DFT | Shared digital foundations, D8 scan, D9 industrial-flow scope | Self-written fault-simulation exercise; commercial-tool evidence through authorized university resources |
| FPGA | D1, D2, D10 constraints | D11 on-board debugging, D12 official device / tool scope checks |
| EDA development | D15 algorithms, one self-written small project | D13 real engineering code, a module from D5 / D6; D14 only for a compiler specialty |

Common acceptance after using a resource: explain the main concept without consulting it, write a small experiment, deliberately change one condition and predict the outcome, and record failure causes. Following a tutorial without independent understanding earns at most partial L2, not independent L3.

## 2. Resource cards

### D1. MIT 6.004: foundations of digital circuits and computation structures

- Official source: [MIT OpenCourseWare — Computation Structures, Spring 2017](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/). Checked: 2026-09-22.
- Suitable for: shared RTL, DV, FPGA, and DFT foundations; digital-circuit gaps for PD / EDA students.
- Prerequisites: high-school algebra, binary numbers, basic logic, and some English reading. Beginners should start with digital abstraction, then combinational logic, sequential logic, and FSMs.
- Read first: units on combinational logic, sequential logic, FSMs, performance metrics, and pipelining. Completing the entire computer-architecture course at the outset is unnecessary.
- Task: draw a counter / FIFO's state changes and key timing; calculate latency and throughput by hand. Create a problem with identical functionality but different pipelines and explain the trade-offs.
- Acceptance: distinguish combinational logic from state, clock period from operation latency, and latency from throughput. Basic answers include derivations, not just final values.
- Access / boundaries: public course materials are readable; historical laboratory environments and campus services are not guaranteed to remain available. Use the principles and exercises without copying obsolete installation instructions blindly. Respect the material's license; do not copy the full lecture collection into this repository.

### D2. Verilator: simulation, lint, and supported features

- Official source: [Verilator User's Guide](https://verilator.org/guide/latest/); feature boundaries in [Input Languages](https://verilator.org/guide/latest/languages.html). Checked: 2026-09-22.
- Suitable for: introductory RTL / DV / FPGA work and an EDA simulation specialty.
- Prerequisites: small Verilog / SystemVerilog modules, clock and testbench concepts, basic terminal use.
- Task: compile and run a counter / FIFO; enable waveforms and relevant checks. Intentionally introduce a width error, latch, or assertion failure and inspect its log. Preserve `verilator --version` or equivalent version evidence in the project.
- Acceptance: explain each significant warning; tests detect errors; the run entry point does not depend on GUI actions. List language features used and their verification status.
- Access / boundaries: open-source tool; check installation dependencies in the official documentation. Support for classes, assertions, and functional coverage changes over time. Do not assume any SV/UVM project runs out of the box; the official language page also states limitations such as timing-check support. Functional simulation is not gate-level timing signoff.

### D3. cocotb: building a self-checking environment

- Official source: [cocotb Quickstart Guide](https://docs.cocotb.org/en/stable/quickstart.html). Checked: 2026-09-22.
- Suitable for: RTL self-tests, introductory DV, FPGA simulation; particularly useful with existing Python knowledge and no commercial verification tools.
- Prerequisites: Python functions, containers, exceptions; HDL clocks and signals; a compatible simulator already running.
- Task: run the official quickstart example, then write an independent FIFO reference queue, driver, monitor, and scoreboard. Add timeouts, fixed seeds, reset, and boundary tests.
- Acceptance: removing or breaking a DUT rule causes failure; the correct version passes. Record the HDL / Python sampling agreement and explain why it avoids races.
- Access / boundaries: the framework is public but still depends on the selected simulator and supported features. It teaches verification methods; it does not automatically provide UVM experience or complete requirements-based functional coverage. APIs change by version: consult the installed version's documentation and avoid combining old tutorials with incompatible new APIs.

### D4. Accellera UVM: methodology and reference implementation

- Official source: [Accellera — UVM Downloads](https://accellera.org/downloads/standards/uvm); conceptual entry point: [UVM Community](https://www.accellera.org/community/uvm). Checked: 2026-09-22.
- Suitable for: DV tracks whose target JD explicitly requires SystemVerilog / UVM.
- Prerequisites: SV classes, interfaces, concurrency, and an independently written self-checking environment; clear driver, monitor, and scoreboard responsibilities.
- Read first: components / transactions, phases, sequences, TLM, configuration, and reuse. Learn mechanisms such as the factory while solving actual reuse problems.
- Task: run a simple interface agent on an authorized simulator with confirmed compatibility. Change DUT parameters or instance count while preserving the same monitor and checking logic. Save UVM and simulator versions.
- Acceptance: trace a sequence to pins, then a monitor to the scoreboard; explain phases and objections; provide logs proving the environment actually executed.
- Access / boundaries: standard-related material and reference implementations are publicly available; simulator licensing and compatibility require separate checks. Reading alone counts as L1. Uncompiled / unexecuted code cannot be counted as a completed UVM project.

### D5. Yosys: synthesis, IR, and engineering source code

- Official source: [YosysHQ Yosys Documentation](https://yosyshq.readthedocs.io/projects/yosys/en/latest/). Checked: 2026-09-22.
- Suitable for: RTL synthesis foundations, PD prerequisites, and EDA synthesis / compiler specialties.
- Prerequisites: synthesizable HDL, flip-flops / combinational logic, basic shell; C++ and data structures for development work.
- Read first: Getting started, Synthesis starter, Scripting. Consult language support, memory / FSM / technology mapping as needed. RTLIL, extension, and testing documentation are for the development route.
- Task: synthesize a self-written FIFO / computation module and explain inferred registers, muxes, memories, or latches. Change width / pipelining and compare structures. Developers additionally trace one pass's inputs, outputs, and regression entry point.
- Acceptance: reproducible scripts and saved logs, no unexplained latches, and netlist / cell statistics linked back to RTL. Library origins and licenses are clear.
- Access / boundaries: Yosys is an open-source synthesis framework. The default and additional front ends differ in language support and licensing; check before use. Successful synthesis does not establish formal equivalence, CDC / RDC, or signoff. `latest` may describe development code; pin the actual release / commit for experiments.

### D6. OpenSTA: timing models, constraints, and reports

- Official project material: [OpenSTA README, OpenROAD project mirror](https://github.com/The-OpenROAD-Project/OpenSTA); the upstream project linked by that README is [Parallax OpenSTA](https://github.com/parallaxsw/OpenSTA). Checked: 2026-09-22.
- Suitable for: PD / STA as a primary track, timing foundations for RTL / EDA.
- Prerequisites: setup / hold, launch / capture, logic delay, small-netlist reading, Tcl.
- Task: use publishable Verilog netlists, Liberty, and SDC. Analyze a small single-clock circuit, then add I/O constraints or an available SPEF. Calculate and explain a complete setup / hold path by hand.
- Acceptance: state the purpose and units of every input file; trace reports to startpoints, endpoints, clocks, and constraints. Detect intentionally omitted constraints instead of only displaying WNS.
- Access / boundaries: public source and documentation; follow the selected version's license, as the project has different licensing arrangements. This material teaches gate-level STA and model interfaces. Industrial signoff depends on actual models, scenarios, checks, and accepted processes; it cannot be inferred from the tool name.

### D7. OpenROAD Flow Scripts: understanding RTL-to-GDS stage by stage

- Official source: [OpenROAD Flow Scripts Tutorial](https://openroad-flow-scripts.readthedocs.io/en/latest/tutorials/FlowTutorial.html). Checked: 2026-09-22.
- Suitable for: digital PD, physical feedback for RTL, understanding EDA engineering inputs / outputs.
- Prerequisites: synthesis basics, netlists, Liberty / LEF / DEF / SDC; Linux / containers or another officially supported environment. Check hardware requirements for the chosen design; suitability for every laptop is not guaranteed.
- Task: run the tutorial's small design and record each stage's output, then introduce a self-written small module. Fix the process platform and frequency and change one density / constraint / RTL parameter to observe its impact.
- Acceptance: distinguish synthesis, floorplan, place, CTS, and route; locate their logs / reports; identify the earliest stage where a failure appears.
- Access / boundaries: tools and teaching flows are public, but platform files, libraries, and designs carry their own licenses. Automatic flow completion does not establish all signoff checks. Tutorial performance values belong to its specific example and cannot be copied into the student's résumé as personal results.

### D8. OpenROAD DFT: scan experiments with a limited scope

- Official source: [OpenROAD — DFT: Design for Testing](https://openroad.readthedocs.io/en/latest/main/src/dft/README.html). Checked: 2026-09-22.
- Suitable for: DFT structural learning and exploration of open tools.
- Prerequisites: scan cells, shift / capture, standard-cell libraries, a simple physical flow.
- Task: read current commands and Limitations first. With supported cells and designs, inspect scan replacement / chain-planning behavior and check chain lengths and connections. If prerequisites are unmet, use the handwritten teaching scan project instead.
- Acceptance: distinguish commands that change a design from commands that only report it. Save versions, configuration, chain reports, and bounded verification. A successful exit code does not replace chain / mode checks.
- Access / boundaries: the checked page lists unimplemented scan optimization and other limitations. Different page sections / future versions may change; judge the pinned code, commands, and experiments together. This module does not replace a complete industrial ATPG, compression, MBIST, at-speed, or test-signoff suite.

### D9. Synopsys TestMAX: recognizing the scope of industrial DFT flows

- Official source: [Synopsys — Test Automation / TestMAX](https://www.synopsys.com/implementation-and-signoff/test-automation.html). Checked: 2026-09-22.
- Suitable for: understanding DFT roles and separating teaching projects from industrial work.
- Prerequisites: scan, fault models, and test objectives; product installation is unnecessary.
- Task: diagram “design test structures → generate / verify patterns → hand off to physical-design / test teams.” From the official description, list capabilities absent from the student's project, then compare real JDs.
- Acceptance: distinguish at least structure insertion, fault models / ATPG, pattern verification, and manufacturing test; identify university resource gaps and ways to fill them.
- Access / boundaries: a vendor product overview is a source for workflow scope. It does not establish free availability, independent effectiveness, current hiring at any company, or student proficiency with the product.

### D10. AMD UG903 / UG949: FPGA timing constraints

- Official source: [UG903 — About Constraints Methodology](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/About-Constraints-Methodology), with [UG949 — Defining Timing Constraints in Four Steps](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Defining-Timing-Constraints-in-Four-Steps). Checked: 2026-09-22.
- Suitable for: the FPGA track and understanding why constraints must match the actual application.
- Prerequisites: RTL, clocks, setup / hold, a basic Vivado project. For another vendor's tools, use its corresponding official guide.
- Task: identify clocks, I/O delays, clock relationships, and necessary exceptions for a small UART / streaming project. Explain why every exception fits the circuit structure and check for missing constraints.
- Acceptance: constraints match real ports / clocks; explain all critical paths and unconstrained items in reports; explain implementation changes after modifying constraints.
- Access / boundaries: public documentation; verify syntax, assistants, and device support for the selected software version. Setting a false path does not fix CDC; FPGA XDC cannot be copied unconditionally into an ASIC flow.

### D11. AMD UG908: programming and on-board debugging

- Official source: [Vivado Design Suite User Guide — Programming and Debugging, UG908](https://docs.amd.com/r/en-US/ug908-vivado-programming-debugging). Checked: 2026-09-22.
- Suitable for: FPGA students with a compatible board and authorized tools.
- Prerequisites: completed synthesis / implementation; known device, clock, pins, and electrical standards; correct programming connection.
- Task: generate and program the actual platform's bitstream. Use supported debug facilities to capture a handshake or FIFO-full event and compare it with simulated timing.
- Acceptance: record board model, build version, capture conditions, data, and explanation. Reproduce after power cycling from the instructions. A screenshot without trigger conditions is insufficient.
- Access / boundaries: public guide; boards, programmers, and software features depend on available resources. Debug logic can change resource use and timing; distinguish debug builds from performance builds. Reading the guide cannot substitute for board-test evidence.

### D12. AMD Vivado official entry point: check devices and licenses first

- Official source: [AMD Vivado Overview](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html). Checked: 2026-09-22.
- Suitable for: selecting an FPGA environment, not a course that must be completed end to end.
- Prerequisites: exact FPGA part on the available / borrowed board, operating system, and required IP.
- Task: use official links to check current versions, system requirements, downloads, device support, and licensing. Record “verified locally,” “documented as supported,” and “not yet confirmed” separately.
- Acceptance: create a minimal project for a specific device and complete the relevant steps. Before actual installation, retain a configuration plan rather than claiming the environment is ready.
- Access / boundaries: a public product page does not mean all devices / IP are free; licensing and support matrices may change. Do not encourage buying expensive boards or tools merely to match tutorial screenshots.

### D13. OpenROAD Developer Guide: reading a real EDA codebase

- Official source: [OpenROAD Developer Guide](https://openroad.readthedocs.io/en/latest/contrib/DeveloperGuide.html). Checked: 2026-09-22.
- Suitable for: EDA development, especially placement / routing, databases, and timing integration.
- Prerequisites: C++, CMake, Git, debugging, basic netlists and physical-design flow; a small algorithm project with tests already completed.
- Task: select a narrow module and diagram the call relationships among Tcl commands, interfaces, C++ core, database, and tests. Reproduce existing tests before making a meaningful small change.
- Acceptance: identify the code path actually executed; obtain test results for original and modified versions; provide a reviewable patch and impact statement.
- Access / boundaries: large projects have dependencies, build-resource needs, and contribution rules. Respect licenses and conventions. Successful compilation does not establish algorithm understanding; submitting a PR does not mean it has merged. This is advanced development material, not a replacement for introductory C++.

### D14. LLVM Programmer's Manual: selected compiler topics

- Official source: [LLVM Programmer's Manual](https://llvm.org/docs/ProgrammersManual.html). Checked: 2026-09-22.
- Suitable for: EDA students choosing compiler IR, front ends / intermediate representations, or related software foundations; not mandatory for every EDA role.
- Prerequisites: proficient C++, basic compiler principles, data structures, ability to build / debug small projects.
- Task: read only the data structures / interfaces needed for the current project. Implement a small IR traversal / transformation and check semantics before / after, including boundary inputs. STA / P&R students may defer this resource.
- Acceptance: explain why the data structure is appropriate; provide tests and explicit behavior for invalid inputs / unsupported IR.
- Access / boundaries: official public documentation changes by version; IR and APIs must match the installed LLVM version. Reading LLVM does not establish digital-synthesis or commercial EDA development proficiency.

### D15. MIT 6.006: algorithms and complexity foundations

- Official source: [MIT OpenCourseWare — Introduction to Algorithms, Fall 2011](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/); prerequisites in the [Syllabus](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/). Checked: 2026-09-22.
- Suitable for: EDA development; other digital tracks should select it only when algorithm skills are needed.
- Prerequisites: programming and discrete mathematics. The course assumes Python ability and should not be assigned directly to a complete programming beginner.
- Read first: project-relevant complexity, hashing / heaps, graph search, topological and path algorithms, and dynamic programming sections.
- Task: implement topological sorting and DAG longest paths with original inputs. Write correctness reasoning, complexity, and counterexamples, then map the graph to a teaching circuit.
- Acceptance: hand calculations and programs agree on small graphs; explain cycles, unreachable nodes, and scale changes. Provide reasoning as well as outputs.
- Access / boundaries: historical course environments may use old versions. Use and adapt a currently available environment to learn the algorithms; campus submission / grading systems may not be public. Respect course licenses and do not redistribute restricted material wholesale.

## 3. Actions for “I understand it, but cannot build it”

| Common obstacle | What to do in the next 1–3 hours | What not to do immediately |
|---|---|---|
| Documentation has too much English | Choose one command / concept and list inputs, outputs, prerequisites; AI translation is acceptable if checked against the original | Ask AI to read an entire manual and assign a mastery label |
| Tutorial does not run | Preserve the first error, versions, and minimal input; check current official installation / support information | Upgrade every dependency at once or copy many unknown commands |
| Waveform looks wrong | Draw the expected 5–10 cycles, compare sampling points cycle by cycle, reduce to a minimal reproducer | Repeatedly ask AI to change RTL without preserving failing versions |
| Run passes but learning is unclear | Change a parameter, add a boundary, inject one fault, explain changed outputs | Treat a success screenshot as L3 evidence |
| Project is too large | Reduce to one interface, one clock domain, and one testable function | Build a CPU, UVM environment, physical flow, and Linux boot together |
| No commercial EDA | Complete explicitly supported open experiments, document gaps, seek authorized university resources | Replace open-source tool names with commercial ones on a résumé |
| No development board | Finish RTL, tests, and implementation where possible; keep board tests pending | Present simulated waveforms as board results |

## 4. Resource checks and job-evidence rules

1. Links above are primary sources from universities, standards organizations, tool projects, or vendors. The checks cover publicly available content and its use; not every installation command / example has been executed. Run a minimal local experiment before raising a student's capability level.
2. Rolling `latest` / `stable` documentation can change. Record actual tool versions, source commits, platform / library versions, OS, and key configuration. Documentation screenshots do not replace execution logs.
3. This resource library does not turn senior roles in another location into local graduate-hiring requirements, nor claim that any company was hiring new graduates in a given direction on 2026-09-22. Personalized planning must separately collect real current JDs, locations, graduation cohorts, qualifications, and source dates.
4. If a link breaks, search the same official site for the title or document number. Update only after confirming migration and preserve the check date. Do not automatically replace original standards / tool sources with third-party reposts or invent an accessibility status.
5. Project hours, sizes, coverage points, and exercises are adjustable training designs written by this Skill. Proposed specifications, tool examples, and promotional figures must never be rewritten as the student's achieved results.
