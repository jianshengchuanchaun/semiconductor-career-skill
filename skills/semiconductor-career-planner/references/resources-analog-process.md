# 资源库 B：模拟、器件、制造、封装测试与应用

品牌：我的模拟电路世界。核实日期：2026-09-22。

只按当前岗位和技能缺口选资源。每一阶段最多一门主课 + 一份官方工具文档 + 一个项目；资源多不等于学习完成。以下“先修、练习、验收、用时”是本 Skill 的教学安排，不是资源作者的课程承诺。官方页面可随时变化；版本、授权与支持平台以实际下载页为准，禁止寻找破解版 EDA、泄露 PDK 或绕过许可。

## R1. 器件与电路基础：MIT OCW 6.012

- 来源：[Microelectronic Devices and Circuits, Fall 2009](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/)，MIT 官方课程；已核实课程覆盖微电子器件、结/MOS 物理、电路模型和分析，并提供讲义/习题等学习材料。
- 适用：A1 模拟、A3 器件；A2/A4 可按缺口选读。
- 先修：微积分、基本电路、电势/电场概念。若不会 KCL/KVL 和 RC 暂态，先补相关课程章节。
- 怎么学：只先读 PN 结、MOS、等效小信号、放大器相关章节；每次先画物理图/等效图，再独立做一道题，最后用仿真检查数量级。建议 30–50 小时定向选学。
- 验收：不看答案推导一个偏置点与小信号增益；说明近似条件；保留三道错题与修正。看完视频/读完讲义不算 L2。
- 边界：课程年份较早但基础内容稳定；它不能替代目标 PDK、先进器件专题或当前工具实操。引用材料遵循课程页面许可，不把整套讲义重新分发成个人教材。

## R2. 模拟应用基础：TI Precision Labs – Op Amps

- 来源：[TI 官方运放课程](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html)、[Stability Introduction](https://www.ti.com/video/4080235259001)。已核实课程含短视频、测验/练习，稳定性入门要求先了解运放带宽。
- 适用：A1 的反馈/噪声补充，A6 测试，A7 应用。它更偏运放应用与测量，不能单独证明晶体管级 IC 设计能力。
- 先修：理想运放、RC、Bode 图。按输入/输出范围 → 带宽 → 稳定性 → 噪声学习，不从最复杂专题跳读。
- 练习：同一闭环增益下改变负载电容并预测响应；增加补偿并比较；做输入误差预算与噪声积分，记录模型是否包含相关噪声。
- 验收：一份有单位、频段与来源的误差/噪声预算；一组失稳/改进前后仿真；能够解释相位裕度测量方式。建议 20–35 小时，不要求整站全部看完。

## R3. 低门槛 SPICE：ngspice 或 LTspice，先选一个

- 来源：[ngspice 官方入门](https://ngspice.sourceforge.io/ngspice-tutorial.html)、[ngspice 官方文档](https://ngspice.sourceforge.io/docs.html)、[Analog Devices 官方 LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)。2026-09-22 已核实入口；ngspice 文档与教程的示例版本可能不同，按安装版本查手册。
- 适用：A1、A6、A7。ngspice 便于网表和脚本训练；LTspice 可用于其支持的器件宏模型与电路仿真。不同仿真器语法/模型兼容性需实测，不能直接假定可互换。
- 先修：电路、器件模型和基本文本文件操作。
- 练习：DC/AC/transient 各一个最小网表；扫三个参数组合，输出原始数据；故意构造浮空节点和错误激励再定位。建议 10–20 小时建立基础，再随项目查文档。
- 验收：从干净目录重跑；记录版本、模型来源、输入、log 与测量命令；手算一个结果。没有 PDK 的 MOS/宏模型仿真只能按原理/应用层标注。
- 授权：工具和模型分别看许可。免费工具不意味着所有下载模型都可再分发。

## R4. 开源 PDK 学习入口：SkyWater SKY130

- 来源：[SkyWater PDK 官方项目文档](https://skywater-pdk.readthedocs.io/en/main/)、[项目官方仓库入口](https://github.com/google/skywater-pdk)。页面明确开放版本仍标为 experimental preview/alpha，并提示不用于 production setting；这一限制在 2026-09-22 的核实页面仍存在。
- 适用：A1 的合法 PDK 练习、A2 版图规则与器件识别。
- 先修：MOS、工艺层、SPICE；愿意维护匹配工具版本和环境。安装不是本路线第一周必须完成的任务，可先做 R3。
- 练习：选一种合法器件核对引脚/模型与额定条件；查五条具体设计规则；跑一个小电路。进入版图前确认当前工具、规则、器件提取和模型确实配套。
- 验收：列出 PDK commit/版本、器件名、model corner、规则配置、测试电路和可复现运行。缺失 LVS/PEX 支持时如实降级。
- 边界：公开文档不能保证任意下载组合可用；官方某些验证子页仍有 TODO。开源教学流程通过不代表生产签核，也不代表掌握某公司先进工艺。不要把 PDK 文件随自己的 Skill 一起打包。

## R5. 版图验证的职责边界与工具入口

- 来源：[Cadence 官方：What are DRC and LVS in Physical Verification?](https://support1.cadence.com/public/docs/content/20514747.html)、[Magic 官方入口](https://opencircuitdesign.com/magic/)、[Netgen 官方入口](https://opencircuitdesign.com/netgen/)。Cadence 页面用于核对 DRC/LVS 的独立职责；Magic/Netgen 入口可达但本次网页正文抽取有限，不据此声称已验证安装步骤、当前版本或所有 PDK 的兼容性。
- 适用：A2，A1 的后仿真阶段。商业流程优先使用学校合法环境的对应版本文档和 PDK 手册；不要套用网上未知工艺 rule deck。
- 先修：电路连接、器件尺寸、工艺层。先弄清哪一份 schematic/netlist 对哪一份 layout。
- 练习：一个电流镜完成 DRC 和 LVS；人为加一个短路/开路/参数错误，重新运行并修复；若具备提取流程，回标一个关键网寄生。
- 验收：每次有检查器、命令/设置、输入版本、规则、报告及最终结论；原理图 check、Spectre 运行、DRC 和 LVS 四项状态独立记录。建议 20–40 小时起步，难度取决于环境成熟度。
- 边界：没有 checker 报告不判 LVS 通过；没有官方配套流程不声称 foundry signoff。

## R6. TCAD 工具职责：Synopsys 官方概览

- 来源：[TCAD 概览](https://www.synopsys.com/manufacturing/tcad.html)、[Sentaurus Process](https://www.synopsys.com/manufacturing/tcad/process-simulation/sentaurus-process.html)、[Sentaurus Device](https://www.synopsys.com/manufacturing/tcad/device-simulation/sentaurus-device.html)。已核实 Process 用于工艺步骤/结构演变建模，Device 用于器件电、热、光等响应；可用功能与模型仍依许可证和版本而定。
- 适用：A3，A4 的工艺—器件关联。
- 先修：半导体物理、PN/MOS、电场/载流子输运、单位检查。
- 怎么学：产品页只用于确认职责，不当作完整教程；有学校合法授权时从本地官方入门示例开始，做 PN 结 → MOS → 网格/步长 → 参数提取；同步保留官方版本文档出处。建议首个可解释基准 20–40 小时。
- 验收：能说明结构从哪里来、哪些模型被启用、边界如何设、为什么收敛；三档网格比较。启动 Workbench/发现 executable/许可证查询成功都不等于 deck 已正确执行。
- 边界：不能推荐下载他人泄露的安装包/许可证/工艺 deck。工具可描述某种器件不等于默认参数已经对目标工艺校准。

## R7. 无商业 TCAD 条件：DEVSIM

- 来源：[DEVSIM 官方站点](https://devsim.org/)，已核实它提供半导体器件数值仿真项目入口与文档链接。
- 适用：A3 的方程、离散化、器件基准；不替代所有商业 TCAD 模型和工艺模块。
- 先修：PN 结、泊松/连续性方程、Python、数值收敛概念。基础不足先用解析 PN 结练习。
- 练习：从当前官方支持的简单器件示例开始，只改变一个物理量；对比解析极限和三档网格，记录求解失败。安装方式按实际系统文档检查，不能保证 Windows 上任意版本直接可用。
- 验收：完整输入/模型定义、版本、mesh、log 和解释；声明是否有真实数据校准。建议 25–45 小时建立首个基准。

## R8. 统计、DOE、SPC、可靠性：NIST/SEMATECH e-Handbook

- 来源：[NIST 官方手册入口](https://www.itl.nist.gov/div898/handbook/)、[过程能力说明](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)。已核实手册含量测、实验设计、过程控制和可靠性相关内容；过程能力解释以稳定过程及相应分布假设为条件。
- 适用：A4、A5、A6，也可补 A3 的拟合和测量不确定性。
- 先修：均值/方差、概率、基础 Python。按当前项目选一个主题，不要求通读手册。
- 练习：用标明来源的数据完成控制图与分层分析；设计一个 2³ DOE；或处理带删失的寿命数据。每项先列假设，再算指标，最后检查模型诊断。建议一个主题 15–25 小时。
- 验收：控制界限与规格界限分开；样本独立性和分布假设说明；合成数据标记；不把漂移数据直接汇成一个 Cpk；寿命结论报告不确定性。

## R9. 工艺与制造岗位职责：TSMC 官方角色页

- 来源：[2025 Campus Recruitment — Explore Our Roles](https://www.tsmc.com/static/english/careers/campus_recruitment_2025/index.html)。2026-09-22 核实时仍能读取 PIE、PE、EE、先进封装等角色说明；这是 2025 活动页面，不能用其证明当前招聘状态。
- 适用：A4 的岗位选择、A5 的封装职责理解。
- 先修：无需额外先修，但应有个人偏好/地点/实验条件记录。
- 练习：把 PIE 的跨模块/产品问题与 PE 的模块变异控制分别改写成“输入—动作—交付物”；再找目标地区三条当前官方 JD 对照。建议 2–3 小时完成首次比较。
- 验收：说清自己选哪个岗位及项目如何支持，列出三项当前缺口；没有最新 JD 时写“通用画像待校准”。

## R10. 封装与热：TI 官方 Packaging 应用资料

- 来源：[SMT & packaging application notes](https://www.ti.com/design-development/packaging/smt-application-notes.html)，已核实该入口列有 IC Package Thermal Metrics 和封装装联相关资料。搜索结果可识别 SPRA953D（2024 修订）等文档，但本次直接 PDF 抓取失败，因此**不据此引用未经逐页核实的具体公式/条款**；学习时从入口打开当前文档并登记修订号。
- 适用：A5，A7 的板级热分析。
- 先修：热流、功率、稳态温升、单位。
- 练习：比较 θJA、θJC、ψJT 的定义和条件；对同一器件在两种 PCB/边界下做参数敏感性，不把封装表格数字跨场景直接套用。
- 验收：每个参数有来源、单位、边界条件和适用解释；完成一个可复现热 RC 练习。建议 8–15 小时起步，真实结温验证需要合适测量链。

## R11. 可靠性证据入口：TI Quality & Reliability

- 来源：[质量可靠性总览](https://www.ti.com/quality-reliability/overview.html)、[官方 FAQ](https://www.ti.com/quality-reliability/faqs.html)、[General quality guidelines](https://www.ti.com/quality-reliability/quality/guidelines.html)。已核实这些入口解释器件质量/可靠性与资格验证框架，不能直接替代任何具体器件的 qualification report 或标准正文。
- 适用：A5、A6。
- 先修：失效机制、样本与统计；先知道想验证哪种机制。
- 练习：选一个公开产品，查其公开资格信息，把“器件/封装/条件/依据/尚缺内容”整理成表；设计一个机制驱动的验证计划。
- 验收：能区分设计验证、资格验证、量产监控、客户现场失效；没有公开信息就标缺失。建议 6–12 小时。
- 边界：JESD、AEC 等标准的版本、条款、样本量和测试应力必须另查当前官方正文及使用授权；不编造“按最新标准通过”。

## R12. 仪器自动化：PyVISA 官方文档

- 来源：[Communicating with your instrument](https://pyvisa.readthedocs.io/en/latest/introduction/communication.html)，已核实包含资源打开、通信设置和故障排查思路；使用版本应与本机库一致。
- 适用：A6、A7。
- 先修：Python、函数/异常/文件、仪器操作与实验室规则。
- 练习：先写可注入错误的 mock；再用实验室许可仪器读取 ID 与已知量，配置超时和结束符。每台仪器的 SCPI 命令以该机型手册为准，不能假定完全通用。
- 验收：设备 ID、通信参数、命令日志、时间戳、单位与原始数据齐全；断连和超时能明确失败；硬件接入前审查会改变输出/量程的指令。建议 8–15 小时软件起步，真实设备验证另计。
- 边界：PyVISA 是通信工具，不能自动证明仪器校准、测量正确或设备兼容；mock 不能写成实测。

## R13. ADC 测试：Analog Devices 官方技术资料

- 来源：[INL/DNL Measurements for High-Speed ADCs](https://www.analog.com/en/resources/technical-articles/inldnl-measurements-for-types-of-highspeed-adcs.html)、[System Applications Guide — Section 16: Techniques for Verifying High Speed ADC Performance](https://www.analog.com/media/en/training-seminars/design-handbooks/system-applications-guide/Section16.pdf)。已核实页面/PDF摘要涉及静态与动态 ADC 测试；文章时间较早，基本测量方法可用，具体设备和产品推荐需重新核实。
- 适用：A6，A7 的数据采集细分。
- 先修：量化、采样、FFT、噪声/失真与基础统计。
- 练习：先用已知理想量化器/合成正弦验证分析脚本；再处理真实板卡数据，记录采样、输入、窗口、频点、源质量与溢出。
- 验收：说明 INL/DNL 的参考定义，解释 SINAD→ENOB 的条件；给出原始样本和脚本；分辨 ADC、输入源、时钟和采集链可能贡献。建议 15–25 小时。
- 边界：ADC 标称位数不是实测 ENOB；不具备有效动态测试链就只报告能够支持的静态结果。

## R14. 应用/FAE 的工作情境：TI 官方介绍

- 来源：[A day in the life: TI Field Applications Engineer](https://www.ti.com/video/6351499567112)，2026-09-22 已核实官方视频入口。
- 适用：A7 岗位探索；用来理解客户与技术协作情境，不用来推断所有公司的岗位职责、薪资、出差或工时。
- 先修：准备一个自己完成的小电路，知道其规格与限制。
- 练习：对同一项目写两版说明：面向工程师的验证证据和面向产品同事的约束取舍；模拟一次需求不清的客户问题，先提出可判定的问题再给方案。
- 验收：5 分钟说明中能回答需求、方案、证据、限制、下一步；不编真实客户案例，不自动向外发送邮件。建议 2–4 小时探索，后续沟通训练融入项目。

## 学习资源使用与更新协议

1. Agent 每次只推荐与本周交付物直接对应的资源；写明读哪部分、做什么、如何过关、预计多少有效小时。
2. 链接失效先找同一机构的当前入口；不能悄悄换成来源不明的下载站。网页可访问只说明资源入口存在，实际安装、登录、许可证、运行仍须现场验证。
3. JD 每次制定投递计划时重查；基础课可沿用，工具版本/授权/标准条款/硬件价格需当次核实。没有联网时标“未联网核实”，请求学生提供资料或使用已有合法文档。
4. 资料引用只摘必要结论和链接，不搬运整本教材、课程、标准或商业手册；学生项目中保留作者、题名、版本/日期和对应页码/章节。
5. 本文件未验证任何安装命令实际运行、商业许可证可用、PDK 可生产签核、实验样品实测达标或企业在招状态。项目数值和工时是教学规划建议，生成个人计划时必须重新检查可行性。
