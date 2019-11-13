# http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221]




def nextInSequence(numstr):
    next = []
    # print("Sekvens: ",numstr)
    # print(len(numstr))
    pos = 0
    ch = numstr[pos]
    count = 0
    for j in numstr:
        if j == ch:
            count = count + 1


        else:
            # print("count: {}_{}".format(count, ch))
            next.append([count, ch])
            count = 1
            ch = j
    else:
        # print("count: {}_{}".format(count, ch))
        next.append([count, ch])
    result = ''
    for e in next:
        for f in e:
            result += str(f)
    return result

a=["1"]
for i in range(31):
    a.append(nextInSequence(a[i]))

print("Number: ", a[30])
print("Answer: len(a[30])=", len(a[30]))


