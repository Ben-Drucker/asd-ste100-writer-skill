#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


SENTENCE_SPLIT_RE = re.compile(r"[.!?]+\s+|[.!?]+$")
WORD_RE = re.compile(r"[A-Za-z0-9'-]+")
PASSIVE_RE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+[a-zA-Z]+ed\b", re.IGNORECASE
)


def load_cases(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_blocked_words(path: Path) -> list[str]:
    return [
        line.strip().lower()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def split_sentences(text: str) -> list[str]:
    parts = SENTENCE_SPLIT_RE.split(text.strip())
    return [p.strip() for p in parts if p.strip()]


def count_words(sentence: str) -> int:
    return len(WORD_RE.findall(sentence))


def find_blocked_words(text: str, blocked_words: list[str]) -> list[str]:
    lower = text.lower()
    found = []
    for word in blocked_words:
        if " " in word:
            if word in lower:
                found.append(word)
        else:
            if re.search(rf"\b{re.escape(word)}\b", lower):
                found.append(word)
    return sorted(set(found))


def evaluate_case(output_text: str, max_words: int, blocked_words: list[str]) -> dict:
    sentences = split_sentences(output_text)
    sentence_length_violations = [
        {"sentence": s, "word_count": count_words(s)}
        for s in sentences
        if count_words(s) > max_words
    ]
    blocked = find_blocked_words(output_text, blocked_words)
    passive_hits = PASSIVE_RE.findall(output_text)

    score = 100
    score -= len(sentence_length_violations) * 20
    score -= len(blocked) * 10
    score -= len(passive_hits) * 5
    score = max(score, 0)

    return {
        "score": score,
        "sentence_count": len(sentences),
        "sentence_length_violations": sentence_length_violations,
        "blocked_words_found": blocked,
        "passive_voice_hits": len(passive_hits),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run simple ASD-STE100 evals.")
    parser.add_argument(
        "--cases",
        default="evals/cases/cases.json",
        help="Path to cases.json",
    )
    parser.add_argument(
        "--blocked-words",
        default="evals/fixtures/blocked-words.txt",
        help="Path to blocked words list",
    )
    parser.add_argument(
        "--outputs",
        default="evals/outputs",
        help="Path to output files directory",
    )
    args = parser.parse_args()

    cases = load_cases(Path(args.cases))
    blocked_words = load_blocked_words(Path(args.blocked_words))
    outputs_dir = Path(args.outputs)

    total_score = 0
    scored_cases = 0

    for case in cases:
        case_id = case["id"]
        max_words = int(case["max_words_per_sentence"])
        output_file = outputs_dir / f"{case_id}.md"

        if not output_file.exists():
            print(f"[MISS] {case_id}: output file not found at {output_file}")
            continue

        result = evaluate_case(
            output_text=output_file.read_text(encoding="utf-8"),
            max_words=max_words,
            blocked_words=blocked_words,
        )
        total_score += result["score"]
        scored_cases += 1

        print(f"[CASE] {case_id}")
        print(f"  score: {result['score']}/100")
        print(f"  sentences: {result['sentence_count']}")
        print(
            f"  sentence length violations: {len(result['sentence_length_violations'])}"
        )
        if result["sentence_length_violations"]:
            for hit in result["sentence_length_violations"]:
                print(
                    "    - "
                    f"{hit['word_count']} words: {hit['sentence']}"
                )
        print(f"  blocked words found: {len(result['blocked_words_found'])}")
        if result["blocked_words_found"]:
            print("    - " + ", ".join(result["blocked_words_found"]))
        print(f"  passive voice hits: {result['passive_voice_hits']}")

    if scored_cases == 0:
        print("\nNo case was scored.")
        return 1

    average = total_score / scored_cases
    print(f"\n[SUMMARY] scored {scored_cases} case(s)")
    print(f"[SUMMARY] average score: {average:.1f}/100")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
