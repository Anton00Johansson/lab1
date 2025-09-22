def tokenize(lines):
        if isinstance(lines, str):
                lines = lines.lower().split()
        elif isinstance(lines, list):
                lines = " ".join(lines)
                lines = lines.lower().split()
        else:
                print(f'Fel format på input.')
        
        words = []
        for line in lines:

                start = 0
                while start < len(line):
                        if start < len(line) and line[start].isspace():
                                while start < len(line) and line[start].isspace():
                                        start += 1
                        
                        elif start < len(line) and line[start].isalpha():
                                word_start = start
                                while start < len(line) and line[start].isalpha():
                                        start += 1
                                words.append(line[word_start:start])

                        elif start < len(line) and line[start].isdigit():
                                word_start = start
                                while start < len(line) and line[start].isdigit():
                                        start += 1
                                words.append(line[word_start:start])

                        else:
                                words.append(line[start:start + 1])                                
                                start += 1    
        return words


def countWords(words, stopWords):
        frequencies = {}
        for word in words:
                if word in stopWords:
                        continue
                elif word in frequencies:
                        frequencies[word] += 1
                else:
                        frequencies[word] = 1
        
        return frequencies


def printTopMost(frequencies,n):
        sort = sorted(frequencies.items(), key = lambda x:-x[1])
        for word, freq in sort[:n]:
                print(f'{word.ljust(20)}{str(freq).rjust(5)}')


