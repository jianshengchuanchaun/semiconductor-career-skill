# Bilingual release guide

[简体中文](RELEASE.md) | **English** · [English home](../README.en.md)

Repository: [semiconductor-career-skill](https://github.com/jianshengchuanchaun/semiconductor-career-skill). Bilingual version: **v1.2.0**.

## Deliverables

The source includes two self-contained skill folders, 13 role routes per language, resources, nine templates per language, six translated employer cases, examples, installation guidance, and reproducible packaging scripts.

Four language/platform ZIPs are provided in `release/`:

```text
semiconductor-career-planner-zh-codex-v1.2.0.zip
semiconductor-career-planner-zh-workbuddy-v1.2.0.zip
semiconductor-career-planner-en-codex-v1.2.0.zip
semiconductor-career-planner-en-workbuddy-v1.2.0.zip
```

The full source package is `semiconductor-career-planner-source-v1.2.0.zip`. It excludes Office/PDF files, private learning directories, `.qa/`, and historical release binaries. Older releases remain in the maintainer's local archive and Git history.

The Chinese skill keeps the name `semiconductor-career-planner`; the English skill uses `semiconductor-career-planner-en`. Codex packages contain a folder with that name. WorkBuddy packages put `SKILL.md` at the ZIP root and adapt metadata to the documented format. Within each language, the operational body and supporting files are identical between platforms.

## Rebuild and inspect

From the repository root, using Python 3.10+:

```bash
python scripts/validate_release.py
python scripts/build_release.py --list-source
python scripts/build_release.py
```

The build checks required files, relative links, language inventories, employer evidence invariants, archive content, and platform parity. It creates a versioned SHA-256 list. Read [the QA record](QA-v1.2.md) for the actual verification scope; package checks do not establish client import, all engineering-project results, or employment outcomes.

Publishing the repository or copying a generated ZIP does not publish a GitHub Release automatically. To create one, choose the intended tag and upload the four skill packages, optionally the source package and its checksum list. Office files are optional separate attachments and are not required for a skill release.

## Suggested release description

Semiconductor Graduate Career Planner v1.2.0 adds a complete English edition alongside Simplified Chinese. Users choose a language and a Codex or WorkBuddy package. Both editions explain target-role capabilities first, then diagnose foundations, plan tasks, evaluate project evidence, and support weekly review.

Each edition covers 13 role routes and nine student templates. Six employer examples retain their China-region context and 2026-09-22 source date. The Renesas example is expired, SGMICRO is an experienced-hire reference, and NXP/NVIDIA use official search-index evidence with unverified current application status. Teaching tasks are not company hiring standards.

The project uses the MIT license. Client import remains subject to real-client acceptance checks. Source packages exclude Word/PPT/PDF deliverables.
