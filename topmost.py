import sys
import wordfreq as w


def main():
    # Opens and tokenize the text.
    text = open(sys.argv[2], encoding="utf-8")
    tokens = w.tokenize(text)
    text.close()

    # Open stopwords and count the frequence.
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        stop_words = f.read().splitlines()
        frequencies = w.countWords(tokens, stop_words)

    # Prints the n most common words.
    n = int(sys.argv[3])
    w.printTopMost(frequencies, n)


if __name__ == "__main__":
    main()


# Kör koden med: python3 topmost.py eng_stopwords.txt examples/article1.txt 10