# Installation and first use

[简体中文](INSTALL.md) | **English** · [English home](../README.en.md)

Version: **v1.2.0**. Author: 我的模拟电路世界 (My Analog Circuit World).

## Choose a language first

| Language | Skill folder and invocation name | Codex ZIP | WorkBuddy ZIP |
| --- | --- | --- | --- |
| English | `semiconductor-career-planner-en` | [English / Codex](../release/semiconductor-career-planner-en-codex-v1.2.0.zip) | [English / WorkBuddy](../release/semiconductor-career-planner-en-workbuddy-v1.2.0.zip) |
| 简体中文 | `semiconductor-career-planner` | [中文 / Codex](../release/semiconductor-career-planner-zh-codex-v1.2.0.zip) | [中文 / WorkBuddy](../release/semiconductor-career-planner-zh-workbuddy-v1.2.0.zip) |

Choose one edition to start. Each is self-contained. Their different names allow both to be installed, but select one explicitly for a conversation. The Chinese edition keeps its existing skill name for compatibility. An explicit request to answer in another language takes precedence over the edition default.

Keep the whole skill directory, including `references/` and `templates/`. Installing only `SKILL.md` loses the role guides and worksheets. Normal planning does not require Python, Node.js, EDA software, or an API key. Host-model fees and internet access depend on the service you use; individual learning tasks may require authorized engineering tools.

**Validation boundary:** platform documentation was reviewed on 2026-09-22. The bilingual packages have not been imported and exercised in both actual clients. Package structure and language checks are separate from end-to-end client verification. The employer snapshot is also dated 2026-09-22.

## Codex

Official documentation identifies the user-level directory as `~/.agents/skills/` and a project-level directory as `.agents/skills/`. Skills are discovered from `name` and `description` in `SKILL.md`; restart Codex if a new skill does not appear. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills)

### Install the English edition from the repository

Run these commands from the repository root containing `skills/`. They stop if a destination already exists, so a customized installation is not silently overwritten.

Windows / PowerShell:

```powershell
$skillSource = (Resolve-Path -LiteralPath '.\skills\semiconductor-career-planner-en').Path
$skillParent = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillParent 'semiconductor-career-planner-en'
if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md') -PathType Leaf)) {
    throw 'Source SKILL.md is missing. Run from the repository root.'
}
if (Test-Path -LiteralPath $skillTarget) {
    throw 'This skill already exists. Back it up and move it outside the scanned directory first.'
}
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse
Get-Item -LiteralPath (Join-Path $skillTarget 'SKILL.md')
```

macOS / Linux / WSL, Bash or Zsh:

```bash
skill_source="./skills/semiconductor-career-planner-en"
skill_parent="$HOME/.agents/skills"
skill_target="$skill_parent/semiconductor-career-planner-en"
if [ ! -f "$skill_source/SKILL.md" ]; then
  printf '%s\n' 'Source SKILL.md is missing. Run from the repository root.'
elif [ -e "$skill_target" ]; then
  printf '%s\n' 'This skill already exists. Back it up and move it outside the scanned directory first.'
else
  mkdir -p "$skill_parent" &&
  cp -R "$skill_source" "$skill_target" &&
  ls -l "$skill_target/SKILL.md"
fi
```

For Chinese, replace `semiconductor-career-planner-en` with `semiconductor-career-planner` in the paths and invocation. Under WSL, install for the Linux user running Codex; a Windows installation does not automatically install the skill in WSL.

### Install from a Codex ZIP

Extract the chosen Codex package. It contains one folder with the matching skill name. Copy that complete folder to `~/.agents/skills/`, or adjust `skillSource` / `skill_source` above to the actual extracted folder. The English layout should be:

```text
~/.agents/skills/
└── semiconductor-career-planner-en/
    ├── SKILL.md
    ├── references/
    └── templates/
```

For project-only installation, put the folder under `<learning-project>/.agents/skills/` and open that project in Codex. Choose a user-level or project-level location for each edition; duplicate installations of the same name can make selection ambiguous.

### Invoke it

Where the Codex CLI or IDE supports it, use `/skills` or type `$` to select the skill. In other interfaces, choose it from the available skills or name it explicitly. [Invocation documentation](https://learn.chatgpt.com/docs/build-skills)

```text
$semiconductor-career-planner-en
I am a first-year semiconductor graduate student, expecting to graduate in 2029.
I have 12 hours per week and am considering analog IC design.
Explain the required capabilities first, then diagnose my starting point.
Ask about my research, target location, and tools rather than assuming them.
Give me a first-week plan with actions, estimated time, outputs, and acceptance criteria.
```

In a shell, use single quotes around a prompt containing `$` so it is not expanded as a variable:

```bash
codex '$semiconductor-career-planner-en I have 12 hours per week. Diagnose my starting point and derive a learning plan from the target job skills.'
```

## WorkBuddy

1. Download the chosen **WorkBuddy** ZIP, not the full repository source ZIP.
2. Open the client's skills section. The documented Chinese interface uses “专家·技能·连接器”, then “技能”.
3. Choose “添加技能” and “上传技能”, select the ZIP, and complete import.
4. Confirm the skill appears under installed skills and is enabled. Then start a conversation.

UI labels may change with client version, and organization policies may restrict custom skills. The package includes `description_zh`, `description_en`, `version`, and `author` metadata documented by the open platform. These metadata descriptions do not change the language of the operational content. [Client skills guide](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market), [open-platform format](https://open.workbuddy.cn/docs/skill)

Each WorkBuddy ZIP places `SKILL.md` at the ZIP root, with `references/` and `templates/` next to it. This is a packaging decision: the reviewed documentation shows a skill-folder structure but does not definitively prescribe whether a ZIP must contain a single outer folder. This archive layout has not been verified by a real client import. If a client explicitly requires a different outer level, preserve all content, adjust that level, and record the version and exact error.

Do not substitute unverified `.workbuddy/skills` or `.codebuddy/skills` paths, or assume that CodeBuddy Code CLI commands apply to the WorkBuddy desktop client.

Example prompt:

```text
Use the installed semiconductor-career-planner-en skill and answer in English.
I am entering a semiconductor graduate program and have 12 hours per week.
First show the capabilities needed for relevant IC design roles, then use short tasks to diagnose my foundation.
Consider my research obligations, graduation date, location, and available tools.
Recommend one main role and an adjacent alternative, and write the first week's tasks with outputs and acceptance checks.
```

This uses natural-language selection. It does not claim that WorkBuddy implements Codex's `$` selector.

## Check the installation with a short conversation

Use a separate learning folder and fictional student details for the first check.

| Check | Expected observable result |
| --- | --- |
| Discovery and language | The chosen skill name appears, and the response uses its default language unless explicitly overridden. |
| Actual reference access | Ask which files were read. The assistant lists accessible skill references rather than merely repeating the README. |
| Role-first planning | It explains job capabilities before diagnosing gaps and selecting a route. |
| Time budget | A 12-hour net week normally has about 9.6 scheduled hours and 2.4 buffer hours. |
| Actionable tasks | Each task specifies actions, outputs, acceptance checks, and a feasible time estimate. |
| Limited tools | Without commercial EDA/PDK access it proposes a lawful alternative and explains what that alternative cannot prove. |
| Evidence integrity | It does not invent tapeout, LVS, measurements, or experience. Clearly labeled teaching faults remain separate from real defects. |
| Employer examples | It retains sample region, source date, recruiting cohort, expired status, and experience requirements. |

These are user acceptance steps, not a record that the author has already completed them on both clients. The six examples include an expired Renesas internship and an experienced SGMICRO role. They do not establish current vacancies. If browsing is unavailable, use supplied job descriptions or label the material as a general framework or dated snapshot.

## File-reading fallback

Open the extracted repository as the host's workspace and ask:

```text
Read skills/semiconductor-career-planner-en/SKILL.md in this workspace.
Follow its workflow and read the relevant references and templates as needed.
First list the files you can actually access. If something is missing, say so.
I am a new semiconductor graduate student with 12 hours per week.
Show the target-role skills first, then diagnose my foundation and propose a first-week plan.
```

If the host cannot access files, paste the entrypoint and provide supporting references when requested. This is execution from supplied files, not proof of successful skill installation.

## Updating and troubleshooting

- Keep your student profile and weekly records outside the installed skill folder. Back up customized skills before upgrading.
- If the advice is generic, explicitly name the edition, ask which references were read, and provide your graduation date, available time, and tools.
- If both languages are installed, choose the intended skill name. If the same name appears twice, check duplicate user/project installations.
- For a WorkBuddy parsing error, verify the dedicated ZIP, YAML metadata, and file inventory. Record the actual client error before changing the ZIP structure.
- Local installation is separate from submitting a skill to a marketplace. This GitHub repository does not mean either platform has approved it.
- A translated English edition does not imply that the included China recruiting examples apply to another country's hiring rules.
