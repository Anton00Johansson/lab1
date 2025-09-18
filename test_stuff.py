text = "Hej, jag heter Anton!"

"""
.lower()
.isalpha():
.isdigit():
"""

def split(text):
        result = []
        word = ""
        for char in text:
              if char == " " and if word:
                      result.append(word)
                      word = " "


def my_split(s):
    result = []
    current = ""

    for char in s:  # gå igenom tecken för tecken
        if char == " ":  # hittat ett mellanslag → börja ett nytt ord
            if current:            # spara bara om vi har byggt ett ord
                result.append(current)
                current = ""
        else:
            current += char        # bygg på ordet
    if current:                    # sista ordet (om något finns kvar)
        result.append(current)

    return result