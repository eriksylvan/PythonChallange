# http://www.pythonchallenge.com/pc/def/channel.html

import zipfile, re




f = zipfile.ZipFile("channel.zip")
print(f.comment.decode("utf-8"))
num = '90052'
while True:
    content = f.read(num + ".txt").decode("utf-8")
    print(f.getinfo(num + ".txt").comment.decode("utf-8"),end='')
    #print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)


    # HOCKEY
