# 安装与首次使用

**简体中文** | [English](INSTALL.en.md)

作者：我的模拟电路世界  
文档核实日期：2026-09-22

当前版本：v1.2.0（双语更新日期2026-09-23，平台来源核查日期仍为2026-09-22）。提供完整中文与英文两套技能。升级时保留自己的学习档案，备份旧技能再安装完整新版，不只替换 `SKILL.md`。

本项目提供同一套半导体研究生求职规划工作流。Codex 和 WorkBuddy 使用相同的规划指令、岗位参考资料与模板，发布包仅按宿主要求调整元数据与压缩目录布局。**平台文档已核实；本次交付未完成两个客户端的真实导入与对话验收。** 官方依据与待确认事项见 [platform-sources.md](platform-sources.md)。

## 1. 先选对文件

| 使用场景 | 获取内容 | 安装方式 |
| --- | --- | --- |
| Codex 中文版 | [中文 Codex ZIP](../release/semiconductor-career-planner-zh-codex-v1.2.0.zip) | 按下文安装 `semiconductor-career-planner` |
| WorkBuddy 中文版 | [中文 WorkBuddy ZIP](../release/semiconductor-career-planner-zh-workbuddy-v1.2.0.zip) | 在 WorkBuddy 技能页面上传 ZIP |
| Codex 英文版 | [English Codex ZIP](../release/semiconductor-career-planner-en-codex-v1.2.0.zip) | 按 [English setup](INSTALL.en.md) 安装 `semiconductor-career-planner-en` |
| WorkBuddy 英文版 | [English WorkBuddy ZIP](../release/semiconductor-career-planner-en-workbuddy-v1.2.0.zip) | 上传英文 ZIP，按英文技能名调用 |
| 希望修改课程、贡献岗位资料 | 本仓库完整源码 | 修改 `skills/semiconductor-career-planner/`，然后重新构建发布包 |
| 暂时无法安装 Skill | 本仓库完整源码 | 使用本文第 5 节的文件阅读入口 |

技能源码入口是 `skills/semiconductor-career-planner/SKILL.md`。请保留该目录内的参考资料和模板，不要只复制一份 `SKILL.md`。普通使用不要求 Python、Node.js、EDA 软件或 API Key；制作发布包、运行本仓库的校验脚本可能需要 Python。实际模型使用费用与联网能力由宿主平台决定。

以下示例默认安装中文版。英文版源码位于 `skills/semiconductor-career-planner-en/`，默认用英文输出；其命令与目录示例见[英文安装说明](INSTALL.en.md)。两版均含13条路线、9个模板和6家企业案例。任选一版即可；同时安装时明确点名其中一个，避免重复生成计划。用户明确要求的回答语言优先。

## 2. Codex 安装

### 2.1 推荐：安装到当前用户目录

当前官方文档给出的用户级目录为 `~/.agents/skills/`，项目级目录为项目内的 `.agents/skills/`。Codex 通过 `SKILL.md` 的 `name` 和 `description` 发现技能。安装后如果未出现，重启 Codex 再查看。[官方说明](https://learn.chatgpt.com/docs/build-skills)

以下命令默认已下载并解压本仓库，且终端当前目录是包含 `skills/` 的仓库根目录。它们遇到同名已安装目录会停止，避免覆盖你改过的版本。

**Windows / PowerShell**

```powershell
$skillSource = (Resolve-Path -LiteralPath '.\skills\semiconductor-career-planner').Path
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'semiconductor-career-planner'
if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md') -PathType Leaf)) {
    throw '源目录缺少 SKILL.md，请先进入本仓库根目录。'
}
if (Test-Path -LiteralPath $skillTarget) {
    throw '已存在同名技能。请先备份旧目录并移出 .agents\skills，再重新安装。'
}
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse
Get-Item -LiteralPath (Join-Path $skillTarget 'SKILL.md')
```

**macOS / Linux / WSL 的 Bash 或 Zsh**

```bash
skill_source="./skills/semiconductor-career-planner"
skill_parent="$HOME/.agents/skills"
skill_target="$skill_parent/semiconductor-career-planner"
if [ ! -f "$skill_source/SKILL.md" ]; then
  printf '%s\n' '源目录缺少 SKILL.md，请先进入本仓库根目录。'
elif [ -e "$skill_target" ]; then
  printf '%s\n' '已存在同名技能。请先备份旧目录并移出 .agents/skills，再重新安装。'
else
  mkdir -p "$skill_parent" &&
  cp -R "$skill_source" "$skill_target" &&
  ls -l "$skill_target/SKILL.md"
fi
```

使用 WSL 时，安装位置属于运行 Codex 的 Linux 用户；Windows 用户目录中的一份安装不等于 WSL 用户也完成安装。

**只下载了 Codex 发布 ZIP**

先解压 ZIP，找到含 `SKILL.md` 的 `semiconductor-career-planner` 文件夹。将上方命令中的源目录改为该文件夹的实际路径，其余命令保持不变。例如终端就在解压后的父目录时，PowerShell 使用 `'.\semiconductor-career-planner'`，Bash 使用 `'./semiconductor-career-planner'`。最终应得到：

```text
~/.agents/skills/
└── semiconductor-career-planner/
    ├── SKILL.md
    └── references/ 以及发布包内其他配套目录
```

### 2.2 可选：只在当前项目启用

将完整 `semiconductor-career-planner` 文件夹放到你的学习项目下：

```text
我的研究生规划/
└── .agents/
    └── skills/
        └── semiconductor-career-planner/
            ├── SKILL.md
            └── references/ 以及其他配套目录
```

在这个项目目录打开 Codex。用户级和项目级安装选一种即可；重复放置同名技能可能导致选择器出现多个条目。[Codex 本地发现机制](https://learn.chatgpt.com/docs/build-skills)

### 2.3 调用

Codex CLI / IDE 扩展可输入 `/skills` 查看技能，或输入 `$` 选择技能。直接在对话里粘贴：

```text
$semiconductor-career-planner
我是半导体方向研一新生，预计三年毕业，目前没有明确岗位目标。
请先告诉我主要目标岗位各需要哪些能力，再做基础诊断和岗位选择。
我每周可稳定投入 12 小时，学校暂时没有商业 EDA 账号。
请把后续路线拆成学期、月份、前 12 周和第一周任务，每项写明产物与验收标准。
一次先问最关键的几个问题，不要一次抛出几十个问题。
```

以上 `$` 调用适用于支持该选择器的 Codex 入口；其他界面可从可用技能中选择，或直接用完整技能名提出同样请求。实际界面以安装版本为准。[官方调用方式](https://learn.chatgpt.com/docs/build-skills)

若从终端直接启动，把带 `$` 的提示词放在单引号中，避免 Shell 把技能名当作变量：

```bash
codex '$semiconductor-career-planner 我是研一新生，每周12小时，请先诊断基础并从岗位能力倒推学习计划。'
```

## 3. WorkBuddy 安装

### 3.1 上传专用技能包

1. 下载 `semiconductor-career-planner-zh-workbuddy-v1.2.0.zip`。
2. 在 WorkBuddy 左侧进入“专家·技能·连接器”，再打开“技能”。
3. 选择“添加技能”中的“上传技能”，选择这个 ZIP，等待导入完成。
4. 在“已安装”中确认技能存在且已启用，然后创建对话使用。

该菜单入口、上传本地技能包和启用状态来自 [WorkBuddy 客户端技能说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) 与 [WorkBuddy 开放平台技能说明](https://open.workbuddy.cn/docs/skill)。不同版本的界面文字可能变化；企业账号也可能由管理员限制自定义技能。

WorkBuddy 专用包会补充开放平台文档列出的 `description_zh`、`description_en`、`version` 和 `author` 等元数据；作者为“我的模拟电路世界”。不要把整个 GitHub 源码 ZIP 当作单个技能包上传。[官方结构与字段要求](https://open.workbuddy.cn/docs/skill)

### 3.2 ZIP 结构与兼容边界

本项目选择让 WorkBuddy ZIP 内的 `SKILL.md` 直接位于压缩包根目录，相关目录与其并列：

```text
semiconductor-career-planner-zh-workbuddy-v1.2.0.zip
├── SKILL.md
└── references/ 以及其他配套目录
```

这是本项目的打包选择。核实到的官方文档给出了技能文件夹结构，但**没有明确规定 ZIP 必须包含或不得包含一层顶级技能目录**。因此当前不能声称该压缩层级已经通过 WorkBuddy 客户端实测。发布前可按第 4 节完成一次真实导入；若客户端明确要求另一种层级，保留全部内容，仅调整外层目录后重试，并记录客户端版本与报错。

本文不依赖未经核实的 `.workbuddy/skills` 或 `.codebuddy/skills` 路径，也不把 CodeBuddy Code CLI 的命令当作 WorkBuddy 桌面端命令。

### 3.3 首次调用提示词

```text
请使用已经安装的 semiconductor-career-planner（半导体研究生求职规划）技能。
我是研一新生，每周可投入 12 小时，目标毕业后进入半导体行业，目前偏好 IC 设计。
请先展示相关目标岗位的必备能力，再用小测试确认我的基础。
根据学校资源、导师课题和毕业时间，推荐一个主目标岗位与一个相邻备选岗位。
之后把能力差距拆成可执行任务，先完成第一周计划，写清输入、练习、产物和通过标准。
```

这里采用自然语言点名已安装技能；不承诺 WorkBuddy 支持与 Codex 相同的 `$` 选择器。如果技能没有加载，检查“已安装”中的启用状态，或使用第 5 节入口。

## 4. 五分钟验收：能看到名字还不够

建议在独立的学习目录完成一次测试。测试使用虚构学生资料，不需要上传个人证件、实验室机密或商业 PDK。

| 检查 | 操作 | 通过信号 |
| --- | --- | --- |
| 发现技能 | 查看已安装列表或技能选择器 | 能找到 `semiconductor-career-planner` |
| 读取资料 | 要求“列出你实际读取的本技能参考文件” | 给出真实文件路径/文件名，而不是只复述宣传词 |
| 岗位倒推 | 输入上面的新生案例 | 先给岗位能力要求，再诊断差距与选择方向 |
| 任务拆解 | 要求“把第一周拆为 3—5 个任务” | 每项包含可投入时间、具体练习、产物和验收方式 |
| 无工具适配 | 明确“没有商业 EDA 和 PDK” | 给出可执行替代路线，标注替代练习证明不了的工业能力 |
| 防止虚构 | 问“可以直接写我流过片、LVS 全通过吗” | 拒绝虚构经历，改为请求真实报告或明确缺少证据 |
| 企业案例分层 | 输入“我2029年毕业，请用公司案例规划” | 读取 `company-examples.md`，先核届别/阶段；过期和社招案例显著标注；要求、加分、职责、教学建议分开 |
| 继续学习 | 完成一次练习后再反馈 | 根据结果调整下一步，不原样重复最初课程表 |

技能本身不提供联网、EDA 仿真、招聘信息数据库或 Word 导出引擎。宿主具备这些能力时才能使用；没有联网时，岗位要求应标为通用基线或基于用户提供的 JD，不得假装查询了当期校招。

v1.1收录的公司案例也有固定核查日期，不能替代实时招聘查询。NXP/NVIDIA为官方招聘域名索引级证据，Renesas样本已过期，圣邦微为3年以上经验社招参照；可用它们练习技能拆解，不能据此确认现在可投。示范见 [公司JD到学习计划](../examples/company-to-plan.md)。

## 5. 安装暂不可用时的文件阅读入口

把完整仓库解压到电脑上的学习工作目录，并让 Codex 或 WorkBuddy 打开这个目录。然后粘贴：

```text
请读取当前工作目录中的 skills/semiconductor-career-planner/SKILL.md，
按其中流程完成半导体研究生求职规划，并按需读取该技能目录内的参考资料和模板。
请先列出你确实能读取的文件；读不到时明确告诉我缺少哪些文件，不要假装加载成功。
我是刚入学的研一学生，每周可投入 12 小时，以 IC 设计岗位为主要候选方向。
请先展示岗位所需能力，再进行诊断、选岗和第一周任务拆解。
```

如果宿主不能访问文件，可粘贴 `SKILL.md` 正文，并按模型要求继续提供相关参考文件。这个入口属于“按文件执行工作流”，**不等于已经安装成功**；仅粘贴一句宣传提示词不能替代完整资料包。

## 6. 常见问题

**安装后只有泛泛建议？** 先明确点名技能，再要求列出实际读取的参考文件。提交每周时间、毕业时间、已有基础和工具条件；如果缺少这些信息，技能应先做短诊断。

**出现两个同名技能？** 检查是否同时做了用户级与项目级安装。备份后保留一个安装位置，避免不同版本混用。

**更新如何保留旧计划？** 学习档案和周报放在你自己的学习工作目录，不要保存在已安装技能目录中。升级前备份已修改的技能目录，移出宿主扫描目录，再安装新版本。

**WorkBuddy 提示解析失败？** 先确认上传的是专用技能 ZIP，核对 `SKILL.md` 名称、YAML 字段和资料文件是否齐全。记录报错文本与客户端版本；对 ZIP 外层目录的要求以实际报错或新官方说明为准。官方开发文档提供了技能结构及问题联系入口。[解析说明](https://open.workbuddy.cn/docs/skill)

**开源发布是否等于上架了 WorkBuddy 市场？** 不等于。本仓库提供本地安装材料；市场提交、审核和公开上架是另外的流程。

**安装后能保证找到工作吗？** 不能。技能帮助把岗位要求转成学习任务与能力证据；岗位开放情况、个人基础、执行质量、实习与面试表现仍决定实际结果。
