import wordfreq
import sys

def main():
        text = ['It','is','a','book']
        stopWords = ['a','is','it']
        n = int(10)
        
        text = wordfreq.tokenize(text)
        frequencies = wordfreq.countWords(wordfreq.tokenize(text), stopWords)

        print(f'{text}')
        print(f'{frequencies}')
        wordfreq.printTopMost(frequencies,n)



if __name__ == "__main__":
        main()


"""
        stopWords = open(sys.argv[1], encoding="utf-8")
        inp_file = open(sys.argv[2], encoding="utf-8")
        n = int(sys.argv[3])

        text = wordfreq.tokenize(inp_file)
        frequencies = wordfreq.countWords(wordfreq.tokenize(text), stopWords)

        wordfreq.printTopMost(frequencies,n)

        # Closing files
        inp_file.close()
        stopWords.close()
"""        