# http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221]
a = [1]


for i in a:
    print(i)
    numstr = str(i)
    print(numstr)
    print(len(numstr))
    pos = 0
    ch = numstr[pos]
    count = 0
    next = []

    for j in numstr:
        if j == ch:
            count = count + 1
            print("count: {}_{}".format(count, ch))
            next.append([count,ch])
        else:
            next = ch + str(count)
            count = 1
            ch = j
            print(next)

    print("---")
    print(next)



