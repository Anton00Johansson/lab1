import wordfreq
import sys

def main():
        if len(sys.argv) >= 4:
                stopWords = sys.argv[1]
                inp_file = sys.argv[2]
                n = int(sys.argv[3])
                a = True
        else:
                stopWords = ['a','is','it', '.']
                inp_file = ['It','is','a', 'good','book', '.', 'Good', 'for', 'reading', '.']
                n = 2
                a = False

        inp_file = wordfreq.tokenize(inp_file)
        frequencies = wordfreq.countWords(inp_file, stopWords)

        print(f'{inp_file}')
        print(f'{frequencies}')
        wordfreq.printTopMost(frequencies,n)

        if a == True:
        # Closing files
                inp_file.close()
                stopWords.close()


if __name__ == "__main__":
        main()

# python3 topmost.py eng_stopwords.txt examples/article1.txt 20