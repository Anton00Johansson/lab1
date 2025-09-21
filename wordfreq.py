def tokenize(lines):
        if isinstance(lines, str):
                lines = lines.lower()
                lines = lines.split()
        
        words = []

        for line in lines:
                start = 0
                while start < len(line) and line[start].isspace():
                        start += 1

                                
        print(words)
        start = start + 1

        return words


tokenize("Hej,jag heter Anton!")