# 10 分钟推广演示

作者：我的模拟电路世界。版本：1.1.0。岗位来源核查日期：2026-09-22。

- [12页可编辑PPT成品获取说明](../docs/DOWNLOADS.md)
- [逐页讲稿与时间分配](10分钟逐页讲稿.md)
- [内容源数据](talk-content.json)

源码ZIP保留演示内容源、逐页讲稿与构建脚本，不含PPT、Word或PDF成品。PPT可作为独立Release附件或推广材料另行提供；下载入口与准确文件名见上方获取说明。仅使用Skill或打包源码不需要生成PPT。

## 讲解与修改

在PowerPoint的备注区或演讲者视图查看讲稿。12页建议时长合计600秒，口播正文约1900个汉字，留有换页、指表和停顿时间。请按自己的语速彩排一次；这不是实际录音计时结果。

正文、7个表格、标题与备注均可编辑。封面采用AI生成概念配图，不对应具体企业产品。中文字体使用Microsoft YaHei（微软雅黑）；在其他设备上展示前请确认字体可用并检查换行。

第3–5页用6份官方岗位样本讲解JD拆解。瑞萨已过期，圣邦为3年以上经验社招，NXP与NVIDIA为官方索引级核查且投递状态未确认。保留这些画面上的边界说明。案例里的练习来自本项目教学设计，不是企业面试题或招聘承诺。

第11页按官方文档说明安装入口，尚未完成两个客户端实测。第12页暂以项目名指引；发布GitHub后可添加你自己的真实仓库链接或二维码。

## 重新生成

普通使用者下载独立PPT附件后直接打开，不需要脚本环境。开发者可用源码中的`talk-content.json`和`../scripts/build_presentation.mjs`重建；源码解压后没有PPT成品是正常情况。

构建使用Codex工作区依赖中的Node.js与`@oai/artifact-tool`，并调用presentations技能附带的验证器。它不是只安装Python即可重建的脚本。需要设置：

- `CODEX_NODE_MODULES`：包含`@oai/artifact-tool`的依赖目录。
- `PRESENTATIONS_SKILL`：包含`container_tools`的presentations技能目录。
- `RUNTIME_PYTHON`：验证器使用的Python可执行文件。
- `PRESENTATION_OUTPUT`：可选的**新文件绝对路径**。已存在的最终输出不能直接覆盖，保留原文件后指定新名称。

在仓库根目录运行 `node scripts/build_presentation.mjs`。验证记录与草稿保存在不发布的`.qa/`目录。重新生成后还应使用本机PowerPoint导出查看：

```powershell
./scripts/export_presentation_native.ps1 -PresentationPath '新生成的PPT绝对路径' -OutputDirectory '项目内新的检查目录绝对路径'
```

脚本只读打开输入文件，导出PNG和PDF；发现PowerPoint已有打开的演示文稿时会停止，避免影响现有工作。自动检查不能替代逐页视觉与来源检查。
