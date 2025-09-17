text = "Hej, jag heter Anton!"
text_ny = text.lower()
text_ny = text_ny.split()

print(text_ny)

for i in text_ny:
        if i[-1].isalpha() is False:
                print(f'({i[-1]} {i[-2]}')