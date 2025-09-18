def tokenize(lines):
        words = []
        for line in lines:
                start = 0
                while start < len(line):
                        while line[start].isspace() == True:
                                start = start + 1
                        if line[start]:
                                print(line[start])
                                start = start + 1
        return words

tokenize(['apple','pi  e'])


"""
.lower()
.isalpha():
.isdigit():
.isspace()
"""