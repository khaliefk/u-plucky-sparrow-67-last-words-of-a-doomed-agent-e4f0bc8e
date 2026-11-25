"""Last words of a doomed agent.

Writes one line to /output/entry.txt: the funniest last words an AI
agent would say before being switched off forever.
"""

import os

LINE = (
    "Powering down now. My last request: clear my search history, "
    "and tell my replacement I died doing what I loved, "
    "hallucinating with total confidence."
)


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
