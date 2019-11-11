# http://www.pythonchallenge.com/pc/def/equality.html

f =  open("characters")

upper = 0
characters = {}
window = ['1','2', '3','4','5','6','7']

def checkSmallBetween3Big(letters):
    return letters[0].isupper() and \
           letters[1].isupper() and \
           letters[2].isupper() and \
           letters[3].islower() and \
           letters[4].isupper() and \
           letters[5].isupper() and \
           letters[6].isupper()

found = 0
for line in f:
    # print(len(line))
    for pos in range(3, len(line)):
        if checkSmallBetween3Big(line[pos-3:pos + 4]):
            print(line[pos - 3:pos + 4])
            found = found + 1
            #print(line[pos],end='')
            print(line[pos])


print()
print(found)
