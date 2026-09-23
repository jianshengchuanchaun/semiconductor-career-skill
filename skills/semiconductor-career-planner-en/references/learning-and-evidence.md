# Learning Method and Engineering Evidence

## One complete learning cycle

For a 90-minute session: 10 minutes recalling previous material without notes; 20 minutes reading one concept; 35 minutes on a calculation/code/simulation/data task; 15 minutes changing one condition and predicting the result; 10 minutes recording errors, failures, and next steps. Scale proportionally for 60 minutes. Adjust reading versus practice to the topic, but do not indefinitely watch lectures without producing outputs.

Replace “study feedback” with: draw the loop and define signs; derive a first-order closed loop; sweep a compensation parameter in simulation; predict bandwidth and phase changes; compare results; explain departures from prediction. Digital and process tracks use the same predict → run → explain differences cycle.

## Example task cards

**Task A1-W2-01: Common-source operating point and small signal.** Prerequisites: MOS operating regions, resistors/capacitors, basic simulation. Read DC/AC topics in the referenced course and the simulator's official documentation. Estimate 2 hours. Build a circuit using a legally available educational model and record its source. Calculate approximate operating point/gain; run DC and AC; change bias; compare theory and simulation. Outputs: netlist/schematic, model source, parameter table, plots. Acceptance: explain operating region, gain sign, trend, and sources of discrepancy rather than supplying screenshots alone. Debug in order: connections/reference ground → parameter units → bias → analysis setup → model applicability. Without a commercial PDK, label the result an educational-model experiment.

**Task D2-W3-01: FIFO boundary tests.** Prerequisites: queues, clocks, reset, basic HDL. Estimate 3 hours. Define full/empty, simultaneous read/write, and reset semantics first. Build a reference queue; test depth boundaries and pointer wraparound; deliberately inject one error; retain the failure log. Acceptance: reproduce the error, pass regression after the fix, and explain which timing/CDC behaviors are outside scope. Test count is not proof of sufficiency; map each test to a specification point.

**Task A4-W3-01: Process-data experimental design.** Prerequisites: mean, variance, controls. Estimate 2 hours. Use explicitly synthetic data for a two-factor experiment; plot main effects and interaction; inspect replication, randomization, and confounders; state conclusions that cannot be extrapolated. Acceptance: rerunnable script, correct units, and a distinction between correlation and causation. Never label synthetic data as measured foundry data.

## Three project tiers

### Tier 1: Minimal experiment

First complete an introductory microtask in 2–8 task hours. A full “minimal project” in the references can require 25–50 hours or more. Estimate calendar weeks as project task hours divided by scheduled weekly budget, adding resource waiting separately; do not promise every project takes one or two weeks. Keep inputs, environment, and outputs narrow. First verify the student can run, explain, and repeat it. Add complexity after acceptance; do not start beginners with a full SoC, PLL, or complete process-flow model.

### Tier 2: Core project

Allow 6–12 weeks or longer under the time budget. Freeze function/performance/conditions in a one-page specification, implement modules, add abnormal/boundary checks, and organize evidence. Record real test conclusions, including an all-pass result within the frozen scope. For real failures, review causes and fixes. For debugging practice, separately conduct explicitly labeled educational fault injection. Arrange one justified comparative change and compare before/after results; it need not originate from a real defect. For course or public-repository projects, state the source, reused content, and personal modifications.

### Tier 3: Advanced extension

Only after core acceptance, add more complex constraints, automation, statistics, multi-condition comparisons, post-layout simulation, or hardware testing. An extension should answer a new engineering question rather than accumulate features. If resources are missing, leave it pending and do not claim experience not obtained.

## Reproducible directory

```text
project/
  README.md            # Goal, scope, reproduction entry point
  spec.md              # Conditions, units, educational acceptance criteria
  src/                 # Publishable code/netlists
  tests/               # Tests and check scripts
  scripts/             # Data processing and automation
  results/             # Publishable raw/derived results
  evidence.md          # Files and conditions supporting each conclusion
  limitations.md       # Unverified matters and confidential exclusions
```

Do not commit restricted PDKs, libraries, company data, or material the school prohibits publishing. Substitute authorized explanations, sanitized results, or only personally written scripts. Do not upload secrets, accounts, or internal laboratory network paths. Document anonymization methods and preserve the validity of conclusions.

## Evidence levels and wording

| Work actually completed | Supported wording | Unsupported wording |
| --- | --- | --- |
| Read a tutorial and reproduced an example | Reproduced the example and explained parameter effects | Independently completed an industrial design |
| Simulated an educational MOS model | Completed model-level DC/AC experiments | Completed process signoff |
| Simulated under an authorized PDK | Met self-defined metrics under the listed models/corners | Stable production under all conditions |
| Obtained actual DRC/LVS reports | Check result for the specified views/rules was… | Simulation succeeded, therefore LVS passed |
| Tape-out with test results | Tested this sample under listed conditions | Full process compliance without supporting data |
| Used an open-source implementation flow | Reproduced implementation with specified open libraries/tool versions | Proficiency in commercial tools never used |
| Used synthetic or public sample data | Validated an analysis method using synthetic/public data | Improved actual production yield |

Grades and acceptance results require student execution or inspectable tool output. AI can help read logs, design tests, and review explanations; the student must independently repeat key steps and answer follow-up questions.

## Avoid false progress

Answer each week: What new capability evidence was added? Which step can you repeat without the tutorial? What was the most valuable observation, distinguishing real failures from educational injections if either occurred? What would happen if a parameter or boundary changed? When there is no output, shrink the task rather than add resources. For each stage, use at most one main textbook/course, one main tool-documentation set, and 1–2 supplemental references.
