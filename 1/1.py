#
# print (ord('a'))
# print (ord('.'))
#
# print (ord('A'))
# print (ord('z'))
# print (ord(' '))
#

with open("inputUrl") as f:
    for line in f:
       for ch in line:
           asciiNo = ord(ch)
           if ord('A') <= asciiNo <= ord('z'):
               print(chr((asciiNo - ord('a') + 2) % 26 + ord('a')),  end = '')
           else:
               print(ch,  end = '')

