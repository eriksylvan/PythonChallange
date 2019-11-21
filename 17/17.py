# http://www.pythonchallenge.com/pc/return/romance.html

# small image looks like the one in challange 4, big picture gives a clue that cookies is uses
# http://www.pythonchallenge.com/pc/def/linkedlist.php
import bz2
import os
import urllib
from urllib.parse import unquote_to_bytes
# from 13 import Phonebook

from urllib.request import urlopen
import re
import requests

# Challange no 4 page have a cookie: info = you+should+have+followed+busynothing...
r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
c = r.cookies
i = c.items()

for name, value in i:
    print(name, value)
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php"



# Following ?busynothing=12345 instead
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"

num = "12345"
busylist= []
busystring = ""

pattern = re.compile("and the next busynothing is (\d+)")
#
# while True:
#     content = urlopen(uri % num).read().decode('utf-8')
#     print(content)
#     r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(num))
#     c = r.cookies
#     i = c.items()
#     busylist.append(i[0])
#     busystring+=i[0][1]
#
#     match = pattern.search(content)
#     if match == None:
#         print(busystring)
#         print(busylist)
#         break
#     num = match.group(1)

# that's it.
# BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
# [('info', 'B'), ('info', 'Z'), ('info', 'h'), ('info', '9'), ('info', '1'), ('info', 'A'), ('info', 'Y'), ('info', '%26'), ('info', 'S'), ('info', 'Y'), ('info', '%94'), ('info', '%3A'), ('info', '%E2'), ('info', 'I'), ('info', '%00'), ('info', '%00'), ('info', '%21'), ('info', '%19'), ('info', '%80'), ('info', 'P'), ('info', '%81'), ('info', '%11'), ('info', '%00'), ('info', '%AF'), ('info', 'g'), ('info', '%9E'), ('info', '%A0'), ('info', '+'), ('info', '%00'), ('info', 'h'), ('info', 'E'), ('info', '%3D'), ('info', 'M'), ('info', '%B5'), ('info', '%23'), ('info', '%D0'), ('info', '%D4'), ('info', '%D1'), ('info', '%E2'), ('info', '%8D'), ('info', '%06'), ('info', '%A9'), ('info', '%FA'), ('info', '%26'), ('info', 'S'), ('info', '%D4'), ('info', '%D3'), ('info', '%21'), ('info', '%A1'), ('info', '%EA'), ('info', 'i'), ('info', '7'), ('info', 'h'), ('info', '%9B'), ('info', '%9A'), ('info', '%2B'), ('info', '%BF'), ('info', '%60'), ('info', '%22'), ('info', '%C5'), ('info', 'W'), ('info', 'X'), ('info', '%E1'), ('info', '%AD'), ('info', 'L'), ('info', '%80'), ('info', '%E8'), ('info', 'V'), ('info', '%3C'), ('info', '%C6'), ('info', '%A8'), ('info', '%DB'), ('info', 'H'), ('info', '%26'), ('info', '3'), ('info', '2'), ('info', '%18'), ('info', '%A8'), ('info', 'x'), ('info', '%01'), ('info', '%08'), ('info', '%21'), ('info', '%8D'), ('info', 'S'), ('info', '%0B'), ('info', '%C8'), ('info', '%AF'), ('info', '%96'), ('info', 'K'), ('info', 'O'), ('info', '%CA'), ('info', '2'), ('info', '%B0'), ('info', '%F1'), ('info', '%BD'), ('info', '%1D'), ('info', 'u'), ('info', '%A0'), ('info', '%86'), ('info', '%05'), ('info', '%92'), ('info', 's'), ('info', '%B0'), ('info', '%92'), ('info', '%C4'), ('info', 'B'), ('info', 'c'), ('info', '%F1'), ('info', 'w'), ('info', '%24'), ('info', 'S'), ('info', '%85'), ('info', '%09'), ('info', '%09'), ('info', 'C'), ('info', '%AE'), ('info', '%24'), ('info', '%90')]



a = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

res = unquote_to_bytes(a.replace("+", " "))
print(bz2.decompress(res).decode())

# gives:
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.


# I give up for now:
# https://www.hackingnote.com/en/python-challenge-solutions/level-17



# http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345



#
# from PIL import Image
#
# img = Image.open('cookies.jpg')
# piximg = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
# (width, hight) = img.size
# mode = img.mode
# print(mode)
# print("w/h",width,hight)
# print(img.info)

Phonebook('Bert')
