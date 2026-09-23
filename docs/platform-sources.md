# 平台兼容性来源与验证边界

作者：我的模拟电路世界  
访问与核实日期：2026-09-22

这份记录只核对 Skill 的文件格式、安装和调用，不用于证明课程内容、就业率或特定模型的规划质量。技能包的静态检查、客户端导入与真实对话是不同层次的证据。

## 官方来源

| ID | 官方页面 | 本项目采用的事实 | 访问情况 |
| --- | --- | --- | --- |
| P1 | [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills) | Skill 包含 `SKILL.md`；`name` 与 `description` 为必备；用户级 `~/.agents/skills` 与项目级 `.agents/skills`；CLI/IDE 的 `/skills` 与 `$` 调用；未显示更新时可重启 | 已打开并读取正文；`developers.openai.com/zh-Hans/docs/build-skills` 当日重定向至此页面 |
| P2 | [WorkBuddy：技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) | 客户端通过“添加技能→上传技能”导入本地包；已安装技能可启用或关闭；可在对话中使用 | 官方页面的搜索索引返回完整相关正文；页面直接打开返回工具 Internal Error，本地 HTTPS 抓取亦失败。因此记录为官方索引正文核实，未作客户端实测 |
| P3 | [WorkBuddy 开放平台：技能](https://open.workbuddy.cn/docs/skill) | 技能目录包含 `SKILL.md` 与可选资源目录；开放平台使用 ZIP；frontmatter 表列出中文/英文描述、版本、作者等必填字段；技能市场入口 | 已打开并读取正文 |

本地补充证据：核实日运行当前环境的 `codex --help`，确认 CLI 可用，但该帮助没有给出完整技能目录说明，因此安装规范以 P1 为依据。本文没有利用第三方博客推断 WorkBuddy 的安装路径。

## 适配决定

1. **每种语言一个维护源。** 中文维护在 `skills/semiconductor-career-planner/`，英文维护在 `skills/semiconductor-career-planner-en/`。同一种语言的 Codex 包使用标准核心 frontmatter；WorkBuddy 包在构建时补充 P3 所列平台元数据。正文和配套资料在两个平台包之间保持一致。双语适配更新于2026-09-23，不改变上方来源核查日期。
2. **优先指令与资料。** 规划本身不依赖某个平台专用工具名，不要求 EDA、Python 或外部 API 才能开始对话。宿主的文件、搜索和导出能力在运行时检查。
3. **Codex 安装遵循当前公开目录。** 新安装文档使用 `.agents/skills`；不因作者本机存在历史目录而把旧路径写成新用户唯一入口。
4. **WorkBuddy 通过界面上传。** 没有充分证据把 `.workbuddy/skills` 或 CodeBuddy Code 的 `.codebuddy/skills` 当成 WorkBuddy 桌面端的通用安装契约，因此不提供这类路径命令。
5. **包名明确区分语言和平台。** v1.2.0采用 `semiconductor-career-planner-{zh|en}-{codex|workbuddy}-v1.2.0.zip`，共四个包。准确下载入口见[安装说明](INSTALL.md)；旧版包由作者本地保留。

## 尚未被这些来源证明的事项

- P3 展示的是技能文件夹结构，没有明确规定 ZIP 是否必须带单一顶层目录。WorkBuddy 包采用 `SKILL.md` 直接位于 ZIP 根目录的布局属于项目实现决定，需要客户端导入验证。
- P2 的“本地技能包”安装描述不代表所有历史版本、企业管理策略或账号均开放自定义安装。
- P3 的字段要求属于开放平台规范；客户端个人导入是否强制所有相同字段尚未确认。项目补齐字段以降低这种差异带来的风险。
- Codex 官方文档更推荐用插件分发可复用能力；本项目首先提供用户可审阅、可手工复制安装的独立 Skill，不能据此声称已进入 OpenAI 插件目录。
- 本次没有在 WorkBuddy 客户端完成 ZIP 上传、技能启用或多轮规划，也没有把本技能安装到作者全局 Codex 配置后做真实端到端对话。不能在 README、视频或发布说明中写“双端实测通过”。

## 发布者复核记录模板

| 平台 | 客户端版本 | 安装包 SHA-256 | 导入结果 | 调用结果 | 实际读取的参考文件 | 执行人/日期 |
| --- | --- | --- | --- | --- | --- | --- |
| Codex | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 |
| WorkBuddy | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 | 待填写 |

保留真实截图、报错与运行输出，再更新这一记录。静态校验应另附报告，不能用它代替以上端到端记录。
