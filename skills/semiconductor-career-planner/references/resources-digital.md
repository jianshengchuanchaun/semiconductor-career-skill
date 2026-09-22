# 数字方向：少而精的资源与练习入口

作者 / 品牌：我的模拟电路世界。资源核验日期：2026-09-22。

本表服务于 [roles-digital.md](roles-digital.md)。先选一个岗位主线，每个阶段只打开“基础解释 + 当前工具 + 当前项目”所需资源，避免把收藏当学习。页面可公开阅读不等于相关商业软件、IP、开发板或云资源免费。各项任务与小时建议由本 Skill 设计，不是原作者课程的官方要求。

## 1. 各方向最小资源组合

| 方向 | 起步只用这些 | 项目进入对应阶段再加入 |
|---|---|---|
| RTL | D1 数字基础、D2 仿真、D3 自检查 | D5 综合、D6 时序 |
| DV | D1 中的时序基础、D2、D3 | D4 UVM；须先确认仿真器的特性支持 |
| PD / STA | D6 时序、D7 实现流程 | D5 综合；STA 与 PD 深度按 JD 分开 |
| DFT | 共享数字基础、D8 scan、D9 工业流程范围 | 自写故障仿真实验；商业工具部分按学校合法资源补齐 |
| FPGA | D1、D2、D10 约束 | D11 板上调试、D12 官方器件 / 工具范围核对 |
| EDA 开发 | D15 算法、一个自写小项目 | D13 真实工程、D5 / D6 某个模块；D14 仅编译器专题选用 |

学习一个资源后的共同验收：不看原文复述核心概念；写出一个小实验；主动修改一个条件并预测结果；把失败原因记录下来。若仍只能照着教程运行，最多计为局部 L2，不计独立 L3。

## 2. 资源卡片

### D1. MIT 6.004：数字电路与计算结构基础

- 官方来源：[MIT OpenCourseWare — Computation Structures, Spring 2017](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)。核验日期：2026-09-22。
- 适用：RTL、DV、FPGA、DFT 的共同基础；PD / EDA 补数字电路概念。
- 先修：高中代数、二进制与基本逻辑；能读少量英文。零基础先看数字抽象，再到组合逻辑、时序逻辑和 FSM。
- 只先读：组合逻辑、时序逻辑、FSM、性能指标与流水线相关单元；不要求一开始完成整门计算机体系课程。
- 任务：画一个计数器 / FIFO 的状态变化和关键时序，手算延迟与吞吐；自己出一道“功能相同但流水线不同”的题并解释取舍。
- 验收：能区分组合逻辑与状态、时钟周期与运算延迟、延迟与吞吐；基础题有推导，不只有答案。
- 访问 / 边界：公开课资料可读；历史课程的实验环境和校内服务不保证仍可用。采用原理与题目，不照搬过时安装环境。公开材料须遵守其许可，不把整套讲义搬进本仓库。

### D2. Verilator：仿真、lint 与支持范围

- 官方来源：[Verilator User's Guide](https://verilator.org/guide/latest/)，特性边界见 [Input Languages](https://verilator.org/guide/latest/languages.html)。核验日期：2026-09-22。
- 适用：RTL / DV / FPGA 入门和 EDA 仿真专题。
- 先修：能写小型 Verilog / SystemVerilog 模块，理解时钟和 testbench；基础终端操作。
- 任务：编译并运行计数器 / FIFO；启用波形和必要检查；有意制造位宽错误、锁存器或断言失败，观察对应日志；在项目中保存 `verilator --version` 或等价版本证据。
- 验收：每个重要 warning 都能解释；错误可由测试捕获；运行入口不依赖 GUI 操作；列出项目使用的语言特性及验证状态。
- 访问 / 边界：开源工具，安装依赖按官方文档核对。类、断言、功能覆盖等支持持续变化，不能保证任意 SV/UVM 项目开箱即用；官方语言页面也说明了 timing checks 等限制。不要把功能仿真当门级时序签核。

### D3. cocotb：建立自检查环境

- 官方来源：[cocotb Quickstart Guide](https://docs.cocotb.org/en/stable/quickstart.html)。核验日期：2026-09-22。
- 适用：RTL 自测、DV 起步、FPGA 仿真，尤其适合已有 Python 基础但暂缺商业验证工具的学生。
- 先修：Python 函数、容器、异常；HDL 时钟与信号；已能运行一个兼容仿真器。
- 任务：从官方 quickstart 跑通小例子后，为 FIFO 写独立参考队列、driver、monitor、scoreboard；增加超时、固定种子、复位与边界测试。
- 验收：移除或破坏 DUT 一条规则时能失败；正确版能通过；记录 HDL 与 Python 两边的采样约定，能解释为何没有竞态。
- 访问 / 边界：框架公开，但仍依赖所选仿真器及其特性。它适合训练验证方法，不自动提供 UVM 经历，也不自动产生需求完整的功能覆盖。API 随版本变动，按安装版本查文档，避免旧教程与新版本混用。

### D4. Accellera UVM：正式方法与参考实现

- 官方来源：[Accellera — UVM Downloads](https://accellera.org/downloads/standards/uvm)，概念入口 [UVM Community](https://www.accellera.org/community/uvm)。核验日期：2026-09-22。
- 适用：目标 JD 明确要求 SystemVerilog / UVM 的 DV 路线。
- 先修：SV 类、interface、并发，已独立写过自检查环境；知道 driver、monitor、scoreboard 各自职责。
- 只先读：组件 / transaction、phase、sequence、TLM、配置与复用；factory 等机制结合实际复用问题学习。
- 任务：在确认兼容的合法仿真器中，把一个简单接口 agent 跑起来；更换 DUT 参数或实例数量，保留同一 monitor 与检查逻辑；保存 UVM / 仿真器版本。
- 验收：能从 sequence 追踪到 pin，再从 monitor 追踪到 scoreboard；能解释 phase 与 objection 的作用；运行日志证明环境实际执行。
- 访问 / 边界：标准相关资料和参考实现可公开取得；仿真器授权及兼容性另行核实。只完成阅读时计 L1；代码未编译 / 未运行时不得计“UVM 项目完成”。

### D5. Yosys：综合、IR 与工程源码

- 官方来源：[YosysHQ Yosys Documentation](https://yosyshq.readthedocs.io/projects/yosys/en/latest/)。核验日期：2026-09-22。
- 适用：RTL 综合基础、PD 前置、EDA 综合 / 编译专题。
- 先修：可综合 HDL、触发器 / 组合逻辑、基本 shell；开发专题另需 C++ 与数据结构。
- 只先读：Getting started、Synthesis starter、Scripting；需要时再看语言支持、memory / FSM / tech mapping。开发路线才读 RTLIL、扩展和测试说明。
- 任务：综合自写 FIFO / 运算模块，解释为何出现寄存器、mux、memory 或 latch；改变位宽 / 流水线后做结构比较。开发者再跟踪一个 pass 的输入、输出与回归入口。
- 验收：脚本能重跑，日志保存；没有未解释的锁存器；网表 / 单元统计能与 RTL 对应。映射库来源和许可清楚。
- 访问 / 边界：Yosys 是开源综合框架；默认前端与附加前端的语言支持 / 授权不同，使用前确认。综合通过不等于形式等价、CDC / RDC 或 signoff 通过。`latest` 可能是开发版文档，实验应固定实际 release / commit。

### D6. OpenSTA：时序模型、约束与报告

- 官方项目资料：[OpenSTA README（OpenROAD 项目镜像）](https://github.com/The-OpenROAD-Project/OpenSTA)，其 README 指向的上游为 [Parallax OpenSTA](https://github.com/parallaxsw/OpenSTA)。核验日期：2026-09-22。
- 适用：PD / STA 主线，RTL / EDA 时序基础。
- 先修：setup / hold、launch / capture、逻辑延迟；能看小网表和 Tcl。
- 任务：使用可公开的 Verilog 网表、Liberty、SDC；先分析单时钟小电路，再添加 I/O 约束或提供可用 SPEF；手算并解释一条完整 setup / hold 路径。
- 验收：列明每种输入文件的用途和单位；报告能回到起点、终点、时钟和约束；故意漏掉约束后能发现，不能只展示 WNS。
- 访问 / 边界：公开源码及文档；遵守所用版本许可，项目存在不同授权方式。该材料可学习门级 STA 与模型接口；学生项目是否完成工业签核取决于实际模型、场景、检查和认可流程，不能由工具名称推断。

### D7. OpenROAD Flow Scripts：逐阶段理解 RTL 到 GDS

- 官方来源：[OpenROAD Flow Scripts Tutorial](https://openroad-flow-scripts.readthedocs.io/en/latest/tutorials/FlowTutorial.html)。核验日期：2026-09-22。
- 适用：数字 PD 主线、RTL 的物理反馈、EDA 工程输入输出理解。
- 先修：基础综合、网表、Liberty / LEF / DEF / SDC；Linux / 容器或符合官方要求的环境。硬件资源先按所选设计检查，不保证任意笔记本都适用。
- 任务：先运行教程提供的小设计，记录各阶段输出；再引入自写小模块。固定工艺平台和频率，改变一项密度 / 约束 / RTL 参数，观察影响。
- 验收：能解释 synthesis、floorplan、place、CTS、route 的区别，找到各自日志 / 报告；能说清失败最早出现在哪一阶段。
- 访问 / 边界：工具与教学流公开，但平台文件、库和设计各自有许可；自动跑完流程不代表学生已完成全部签核检查。教程中的性能数值属于特定示例，不能直接写入自己的项目简历。

### D8. OpenROAD DFT：有限范围的 scan 实验

- 官方来源：[OpenROAD — DFT: Design for Testing](https://openroad.readthedocs.io/en/latest/main/src/dft/README.html)。核验日期：2026-09-22。
- 适用：DFT 的结构学习与开放工具探索。
- 先修：scan 单元、shift / capture、标准单元库与简单物理流程。
- 任务：先读当前版本的命令与 Limitations；在支持的单元与设计中检查 scan replacement / chain planning 的行为，核对链长度和连接；条件不满足时退回手写 scan 教学项目。
- 验收：说清哪些命令真的改变设计、哪些只报告；保存版本、配置、链报告与限定范围验证。不能用工具退出码代替链 / 模式检查。
- 访问 / 边界：核验页面列有未实现的 scan optimization 和其他限制；页面不同部分 / 新版本可能变化，应以固定版本的代码、命令与实验共同判断。此模块不能代替完整工业 ATPG、压缩测试、MBIST、at-speed 与测试签核套件。

### D9. Synopsys TestMAX：工业 DFT 流程范围识别

- 官方来源：[Synopsys — Test Automation / TestMAX](https://www.synopsys.com/implementation-and-signoff/test-automation.html)。核验日期：2026-09-22。
- 适用：DFT 岗位认知、把教学项目与工业工作分清楚。
- 先修：scan、故障模型与测试目的；无需先安装产品。
- 任务：画“设计测试结构 → 生成 / 验证图样 → 与后端 / 测试交接”的流程图；从官方介绍中列出自己项目完全没有覆盖的能力，再核对真实 JD。
- 验收：至少区分结构插入、故障模型 / ATPG、pattern 验证与制造测试；能指出学校资源缺口及补齐途径。
- 访问 / 边界：这是厂商产品介绍，作为流程范围的来源；不证明免费可用、不构成独立效果评测、不说明某家公司正在招聘，也不代表学生已掌握产品。

### D10. AMD UG903 / UG949：FPGA 时序约束

- 官方来源：[UG903 — About Constraints Methodology](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/About-Constraints-Methodology)，配套 [UG949 — Defining Timing Constraints in Four Steps](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Defining-Timing-Constraints-in-Four-Steps)。核验日期：2026-09-22。
- 适用：FPGA 主线；帮助理解约束需要匹配实际应用。
- 先修：RTL、时钟、setup / hold、基础 Vivado 项目；使用其他厂商工具时另找对应官方指南。
- 任务：对小型 UART / 流式项目梳理 clocks、I/O delays、clock relationships 与必要例外；解释每一条例外为什么符合电路结构，检查遗漏约束。
- 验收：约束能匹配真实端口 / 时钟；报告中所有关键路径和未约束项有解释；修改约束后能说明实现结果变化。
- 访问 / 边界：文档公开；语法、向导和器件支持按具体软件版本核对。不要把“设为 false path”当成 CDC 修复，也不要把 FPGA XDC 无条件照搬到 ASIC 流程。

### D11. AMD UG908：下载与板上调试

- 官方来源：[Vivado Design Suite User Guide — Programming and Debugging, UG908](https://docs.amd.com/r/en-US/ug908-vivado-programming-debugging)。核验日期：2026-09-22。
- 适用：有兼容板卡和合法工具环境的 FPGA 学生。
- 先修：已完成综合 / 实现，知道板卡器件、时钟、引脚和电气标准；有正确下载连接。
- 任务：按实际平台生成并下载 bitstream；使用工具支持的调试能力捕获一次握手或 FIFO 满事件；与仿真时序对照。
- 验收：记录板卡型号、构建版本、捕获条件、数据与解释；重新上电后按文档可重复；捕获不是只截一张没有触发条件的图。
- 访问 / 边界：指南公开；板卡、下载器、软件特性依具体资源。插入调试逻辑可能改变资源和时序，应记录调试构建与性能构建的区别。未上板时不能以指南阅读替代板测等级。

### D12. AMD Vivado 官方入口：先核对器件与授权

- 官方来源：[AMD Vivado Overview](https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html)。核验日期：2026-09-22。
- 适用：FPGA 环境选择，不作为需要从头学完的课程。
- 先修：明确已有 / 拟借用板卡的准确 FPGA 型号、操作系统与所需 IP。
- 任务：沿官方入口核对当前版本、系统要求、下载、器件支持和授权；把“本机已验证”“文档标明支持”“尚未确认”分开记录。
- 验收：能够为一个具体器件建立最小工程并完成相应步骤；未实际安装时只保留配置计划，不写“环境已搭好”。
- 访问 / 边界：产品页面公开不等于全部器件 / IP 都免费；许可政策和支持矩阵可能更新。不要让学生为了教程截图购买暂时不需要的昂贵板卡或工具。

### D13. OpenROAD Developer Guide：读真实 EDA 工程

- 官方来源：[OpenROAD Developer Guide](https://openroad.readthedocs.io/en/latest/contrib/DeveloperGuide.html)。核验日期：2026-09-22。
- 适用：EDA 开发主线，尤其布局布线 / 数据库 / 时序集成专题。
- 先修：C++、CMake、Git、调试、基础网表与物理设计流程；已做过一个有测试的小算法项目。
- 任务：选一个范围小的模块，画出 Tcl 命令、接口、C++ 核心、数据库和测试的调用关系；先复现现有测试，再做有意义的小改动。
- 验收：指出真正被执行的代码路径；原始 / 修改版的测试有结果；提交可审阅 patch 和影响范围说明。
- 访问 / 边界：大型工程有依赖、构建资源与贡献规范；遵守许可证和项目约定。编译成功不等于理解算法，提交 PR 也不等于已合并。此资源是开发进阶材料，不适合代替 C++ 入门课。

### D14. LLVM Programmer's Manual：编译器专题选读

- 官方来源：[LLVM Programmer's Manual](https://llvm.org/docs/ProgrammersManual.html)。核验日期：2026-09-22。
- 适用：选择编译器 IR、前端 / 中间表示、相关软件基础的 EDA 学生；不是所有 EDA 岗位必修。
- 先修：C++ 熟练、基本编译原理和数据结构；能构建与调试小工程。
- 任务：只读当前项目需要的数据结构与接口部分；写一个小规模 IR 遍历 / 变换实验，检查前后语义与边界输入。目标若为 STA / P&R，可暂缓。
- 验收：能说明选择的数据结构为何合适；小例子有测试；错误输入 / 不支持的 IR 有明确行为。
- 访问 / 边界：官方文档公开且随版本变化；IR 与 API 要匹配所用 LLVM 版本。阅读 LLVM 并不代表已掌握数字综合或商业 EDA 软件开发。

### D15. MIT 6.006：算法与复杂度补课

- 官方来源：[MIT OpenCourseWare — Introduction to Algorithms, Fall 2011](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)，先修见 [Syllabus](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/)。核验日期：2026-09-22。
- 适用：EDA 开发主线；其他数字方向仅在需要算法能力时选读。
- 先修：编程与离散数学；该课程假定已有 Python 能力，不能直接丢给完全零编程学生。
- 只先读：复杂度、哈希 / 堆等数据结构、图搜索、拓扑与路径、动态规划中与项目有关的章节。
- 任务：用自己的输入实现拓扑排序与 DAG 最长路径；写正确性解释、复杂度与反例；再把图对应到教学电路。
- 验收：小图手算与程序一致；能解释环、不可达节点和规模变化；结果之外还有推理。
- 访问 / 边界：历史课程的软件环境可能使用旧版本，学习算法时采用当前可用环境并自行适配；MIT 校内提交 / 评分系统不一定对外提供。遵守课程材料许可，不将受限内容整包搬运。

## 3. 针对“看得懂、做不出”的学习动作

| 常见卡点 | 下一个 1–3 小时怎么做 | 不应直接做什么 |
|---|---|---|
| 文档英文多 | 只选一个命令 / 概念，列输入、输出、前提；允许 AI 翻译后回看原文 | 要求 AI 代读整本手册并直接给“精通”标签 |
| 教程跑不通 | 保存首个报错、版本和最小输入，核对当前官方安装 / 支持范围 | 同时升级全部依赖或复制大量未知命令 |
| 波形看起来不对 | 先画预期 5–10 周期，与采样点逐拍对照；缩到最小复现 | 仅让 AI 反复改 RTL，且不保留失败版本 |
| 运行通过但不知道学会什么 | 改参数、加边界、注入一个故障，解释输出变化 | 把成功截图当 L3 证据 |
| 项目太大 | 删到一个接口、一个时钟域、一个可验收功能 | 同时写 CPU、UVM、后端与 Linux 启动 |
| 无商业 EDA | 完成明确支持的开放实验，写缺口；争取学校合法资源补证据 | 把开源工具名替换成商业工具名写简历 |
| 无开发板 | 先完成 RTL、测试与条件允许的实现，保留板测待完成 | 将仿真波形包装成板上结果 |

## 4. 资源核验和岗位证据规则

1. 上述链接均为学校、标准组织、工具项目或厂商的主来源；核验的是公开内容与用途，没有对所有安装命令 / 例子逐一运行。实际使用时，先做本机最小实验再提升能力等级。
2. 滚动文档的 `latest`、`stable` 可能变化。学生记录实际工具版本、源码 commit、平台 / 库版本、操作系统和关键配置；文档截图不能替代真实运行日志。
3. 本资源库没有把外地资深岗位当国内校招门槛，也没有声称某家公司在 2026-09-22 正在招收某一方向应届生。个性化规划必须另采集当前真实 JD、地点、毕业年份、学历和来源日期。
4. 若发现链接失效：先搜索同一官方站点的标题或文档编号；确认迁移后更新链接并保留核验日期。不拿第三方转载自动替代标准 / 工具原文，不编造可访问状态。
5. 项目计划中的小时、规模、覆盖点与题目由本 Skill 编写，属于可调整的训练设计。严禁将建议规格、工具示例或宣传数据改写成学生已实现结果。
