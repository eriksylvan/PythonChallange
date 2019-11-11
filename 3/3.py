# http://www.pythonchallenge.com/pc/def/equality.html

f =  open("characters")


def checkSmallBetween3Big(letters):
    return letters[0].islower() and \
           letters[1].isupper() and \
           letters[2].isupper() and \
           letters[3].isupper() and \
           letters[4].islower() and \
           letters[5].isupper() and \
           letters[6].isupper() and \
           letters[7].isupper() and \
           letters[8].islower()
found = 0
for line in f:
    # print(len(line))
    for pos in range(4, len(line)-4):
        if checkSmallBetween3Big(line[pos-4:pos + 5]):
            #print(line[pos - 4:pos + 5])
            found = found + 1
            print(line[pos],end='')
            #print(line[pos])


print()
#print(found)
