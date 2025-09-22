import sys
import wordfreq as w
from pathlib import Path


def load_stopwords(path: Path):
    # Läser ord separerade av whitespace (rad/blanktecken) och trimmar
    with path.open(encoding="utf-8") as f:
        return [w.strip() for w in f.read().split() if w.strip()]


def load_text(path: Path) -> str:
    with path.open(encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) >= 4:
        stopwords_path = Path(sys.argv[1])
        text_path = Path(sys.argv[2])
        n = int(sys.argv[3])

        # Grundläggande felkoll
        if not stopwords_path.exists():
            print(f"Fel: stopwords-fil finns inte: {stopwords_path}")
            return
        if not text_path.exists():
            print(f"Fel: textfil finns inte: {text_path}")
            return

        stop_words = load_stopwords(stopwords_path)
        text = load_text(text_path)
    else:
        # Fallback-exempel för att kunna köra direkt i VS Code
        stop_words = ["a", "is", "it", "."]
        text = "It is a good book. Good for reading."
        n = 2

    tokens = w.tokenize(text)
    frequencies = w.countWords(tokens, stop_words)

    print(tokens)
    print(frequencies)
    w.printTopMost(frequencies, n)


if __name__ == "__main__":
    main()


# python3 topmost.py eng_stopwords.txt examples/article1.txt 3