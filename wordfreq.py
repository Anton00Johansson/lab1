def tokenize(lines):
        words = []
        for line in lines:
                start = 0
                while start < len(line):
                        while line[start].isspace() == True:
                                start += start
                        if line[start].isalpha():
                                end = start
                                start += start
                                while end < len(line) and line[end].isalpha():
                                        end = end + 1
                                words.append(line[start : end])
                        elif line[start].isdigit():
                                start += start
                                end = start
                                while end < len(line) and line[end].isdigit():
                                        end += end
                                words.append(line[start : end])
                        else:
                                start += start
                                end = start
                                words.append(line[start : end])
                                
                        print(words)
                        start = start + 1
        return words


tokenize("Hej,jag heter Anton!")


"""
.lower()
.isalpha():
.isdigit():
.isspace()
"""