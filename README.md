# ASD-STE100 Writer Skill

This repository gives you an installable skill for ASD-STE100 writing.
Use it to write or rewrite technical text in Simplified Technical English.

## Install with `skills`

Run this command:

```bash
npx --yes skills add blagoySimandov/asd-ste100-writer-skill --skill ste100-writer -a github-copilot -g -y
```

You can also use the full URL:

```bash
npx --yes skills add https://github.com/blagoySimandov/asd-ste100-writer-skill --skill ste100-writer -a github-copilot -g -y
```

The command installs the skill to your GitHub Copilot skills directory.

Use this command to see the skills before you install:

```bash
npx --yes skills add blagoySimandov/asd-ste100-writer-skill --list
```

## Install from this repository

1. Clone this repository.
2. Copy `skills/ste100-writer` to your local skills directory.
3. Restart your tool.

```bash
git clone https://github.com/blagoySimandov/asd-ste100-writer-skill.git
mkdir -p ~/.claude/skills
cp -R asd-ste100-writer-skill/skills/ste100-writer ~/.claude/skills/ste100-writer
```

## Use

Ask for a rewrite in ASD-STE100.

Example prompt:

```text
Rewrite this maintenance procedure in ASD-STE100.
Keep all technical data and all safety data.
```

## Skill files

- `skills/ste100-writer/SKILL.md`: Skill instructions.
- `skills/ste100-writer/references/rules.md`: Rule summary.
- `skills/ste100-writer/references/checklist.md`: Final check list.
- `skills/ste100-writer/references/word-choices.md`: Example word choices.

## Evals

The repository has simple evals in `evals/`.
Read `evals/README.md` for setup and commands.
