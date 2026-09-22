# 今晚发布指南

项目仓库：[https://github.com/jianshengchuanchaun/semiconductor-career-skill](https://github.com/jianshengchuanchaun/semiconductor-career-skill)。简介可用：面向半导体研究生的岗位能力规划Skill，从技能诊断到项目、实习与求职，适配Codex与WorkBuddy。

## 已准备的发布内容

源码、MIT许可、README、两端安装说明、13条岗位路线、学习资源、模板、示例、评测、手册与演示内容源、逐页讲稿、构建脚本和B站文案。本版发布包版本为v1.1.0，新增6家企业官方来源岗位案例和从JD到学习任务的示范。**源码ZIP不含Word、PPT、PDF成品；源码可在没有这些成品文件的情况下独立打包。** 成品可选择作为独立Release附件或推广材料提供，文件名见 [DOWNLOADS.md](DOWNLOADS.md)。GitHub仓库已创建，README和B站文案已补入真实地址；本次仅上传源码，Release及Office附件尚未发布。v1.0.0历史资料由作者本地保留，不将旧版验证记录改写为新版实测。

## 发布步骤

1. 检查 `docs/QA-v1.1.md` 的验证范围，在准备宣传的客户端按安装文档完成真实导入测试。
2. 解压本版 `semiconductor-career-planner-source-v1.1.0.zip`，使用其中的发布文件。登录GitHub，新建名为 `semiconductor-career-skill` 的仓库，选择合适可见性。将解压后含README的项目目录内文件上传到仓库根目录，不要多包一层目录。源码包排除作者本地`.qa/`草稿、旧版产物、私人学习目录及所有Word/PPT/PDF成品。
3. 检查首页README链接、`skills/semiconductor-career-planner/SKILL.md`和`docs/DOWNLOADS.md`是否可读；源码中不需要存在Office成品文件。
4. 创建 `v1.1.0` Release，上传两个平台的v1.1.0 ZIP；完整源码ZIP也可作为附件。**Word手册、讲解PPT和另行提供的PDF均为可选独立附件，不放回源码ZIP。** 如选择上传，核对实际文件和QA记录，再在`docs/DOWNLOADS.md`补入真实附件链接；不误传v1.0旧成品。
5. 把真实GitHub链接填入 `docs/BILIBILI.md` 的简介与置顶评论；录制真实调用画面后发布视频。

如使用Git命令，先确认当前目录确为这个新项目、远端是自己的新仓库，避免在其他项目执行初始化或推送。不要覆盖已有仓库历史。GitHub网页上传即可完成首次发布。

## Release说明可直接复制

半导体研究生就业规划Skill v1.1.0，由“我的模拟电路世界”发布。

从目标岗位能力开始，提供基础诊断、技能差距、学期与90天路线、周任务、项目验收、实习校招和持续复盘。覆盖13条主要路线，以IC设计为主。

本版增加NXP、Renesas、NVIDIA、芯朋微、泰凌微和圣邦微六家企业官方来源案例，说明如何分清硬要求、加分项、工作职责，再转为学习任务和验收证据。Renesas样本已过期，圣邦微样本为要求3年以上经验的社招成长参照；NXP/NVIDIA为官方索引级核查。案例不是当前在招清单，不据此承诺任何投递状态。

Codex用户选择codex ZIP；WorkBuddy用户选择workbuddy ZIP。两个包的教学核心一致，元数据与压缩层级按平台文档适配。请按安装说明完成客户端验收；验证状态详见QA文档。

源码包含使用模板、手册/演示内容源、逐页讲稿和构建脚本，不包含Word/PPT/PDF成品。可编辑Word手册和约10分钟讲解PPT作为可选独立附件或推广材料提供，具体以本次Release清单及获取说明为准。本项目按MIT开源，不提供就业保证或未授权EDA/PDK。

## 维护者重建

核心素材修改后，在仓库根目录运行：

```bash
python scripts/validate_release.py
python scripts/build_release.py
```

以上源码/技能包发布流程不以Word、PPT或PDF成品存在为前提。只有需要重新生成或单独发布成品时，才执行下面的Office构建与视觉检查；不能把源码打包成功写成Office视觉验收通过。

Word内容由 `scripts/create_manual_content.py` 及 `docs/manual-analog-pages.json`、`docs/manual-digital-pages.json` 维护，汇总为 `docs/manual-content.json`，再由 `scripts/build_manual.py` 生成。需要Python 3.10+和python-docx：

```bash
python scripts/create_manual_content.py
python scripts/build_manual.py
```

生成后仍应使用可用的Word或受支持文档渲染器逐页检查。生成成功不代表分页已验收。文档源、参考库和平台说明有交叉内容，更新某一份后应检查其余内容是否一致。

PPT重建需要Codex配套Node运行时和Artifact Tool，具体变量、可编辑源及新输出路径要求见 [演示材料说明](../presentations/README.md)。普通用户若下载了独立PPT附件，可直接打开，无需重建环境；附件获取方式见 [DOWNLOADS.md](DOWNLOADS.md)。

正式发布前检视：作者署名；所有ZIP内文件齐全；没有个人计划或敏感文件；没有虚构兼容性或项目结果；安装文档链接有效；推广占位符已替换。SHA256清单用于核对下载文件是否完整，不代表签名或安全认证。

v1.1新增核对：两个平台ZIP都包含 `references/company-examples.md` 与 `.json`；案例总数为6且状态文字完整；源码ZIP不含`.docx`、`.pptx`、`.pdf`成品且文档入口指向获取说明。若另行提供Office附件，再核对投影片上的公司要求与教学建议分开、瑞萨标明过期、圣邦微标明社招3年经验；Word/PPT页数和演讲时长只在实际检查后填写。
