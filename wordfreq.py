def tokenize(lines):
        """
        Splits input text into a list of tokens (words, numbers, and symbols).

        Args:
                lines (str or list): Input text, either as a single string or a list of strings.

        Returns:
                list: A list of tokens (strings), where words, digits, and symbols are separated.
        """
        
        if isinstance(lines, str):
                lines = lines.lower().split()
        else:
                lines = " ".join(lines)
                lines = lines.lower().split()


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
        """
        Counts how many times each word occurs, ignoring stop words.

        Args:
                words (list): A list of words (tokens) to count.
                stopWords (list): A list of words to exclude from counting.

        Returns:
                dict: A dictionary where keys are words and values are their frequencies.
        """

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
        """
        Prints the n most frequent words and their counts.

        Args:
                frequencies (dict): A dictionary with words as keys and their frequencies as values.
                n (int): The number of top frequent words to display.

        Returns:
                None
        """

        sort = sorted(frequencies.items(), key = lambda x:-x[1])
        for word, freq in sort[:n]:
                print(f'{word.ljust(20)}{str(freq).rjust(5)}')