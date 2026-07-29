# Evals for the ASD-STE100 Writer Skill

Use these evals to check output quality.
The evals are simple and fast.

## What the eval checks

- Sentence length limit by case type.
- Use of words from a blocked-word list.
- Use of passive voice with a simple pattern check.

## Case files

- `evals/cases/cases.json`: Case list and limits.
- `evals/cases/<case>/source.md`: Source text.
- `evals/cases/<case>/reference.md`: Example good output.

## Output files

Write your model output to `evals/outputs/<case>.md`.

Use the case id from `cases.json` as the file name.

## Run the eval

```bash
python3 evals/run_eval.py --outputs evals/outputs
```

## Quick self-check

Use the reference outputs to test the harness.

```bash
mkdir -p evals/outputs
cp evals/cases/procedure-basic/reference.md evals/outputs/procedure-basic.md
cp evals/cases/safety-warning/reference.md evals/outputs/safety-warning.md
cp evals/cases/descriptive-data/reference.md evals/outputs/descriptive-data.md
python3 evals/run_eval.py --outputs evals/outputs
```
