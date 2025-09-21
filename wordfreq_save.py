def tokenize(lines):
        if isinstance(lines, str):
                lines = lines.lower().split()
        
        words = []
        for line in lines:

                start = 0
                while start < len(line):
                        if start < len(line) and line[start].isspace():
                                while start < len(line) and line[start].isspace():
                                        start += 1
                                words.append(line[word_start:start])
                        
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


print(tokenize("Hej,jag heter Anton!"))