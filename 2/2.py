# http://www.pythonchallenge.com/pc/def/ocr.html

f =  open("characters")

linecount = 0
characters = {}

def charactersCounter(ch):
    if ch not in characters.keys():
        # New character, start counting
        characters[ch] = 1
    else:
        characters[ch] = characters[ch] + 1

for line in f:
    linecount = linecount+1
    for ch in line:
        charactersCounter(ch)


for char in characters.items():
    if char[1] == 1:
        print(char[0],end = '')
