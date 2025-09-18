def tokenize(lines):
        for line in lines:
                start = 0
                words = []
                while start < len(line):
                        while line[start].isspace() == True:
                                start += start
                        if line[start].isalpha():
                                end = start
                                while end < len(line) and line[end].isalpha():
                                        end = end + 1
                                words.append(line[start : end])
                        elif line[start].isdigit():
                                end = start
                                while end < len(line) and line[end].isdigit():
                                        end += end
                                words.append(line[start : end])
                        else:
                                end = start
                                words.append(line[start : end])
                                
                        print(words)
                        start = start + 1
        return words


tokenize(['apple','pie'])


"""
.lower()
.isalpha():
.isdigit():
.isspace()
"""