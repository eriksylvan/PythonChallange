# http://www.pythonchallenge.com/pc/return/evil.html


# Bert is evil! go back!

data = open("evil2.gfx", "rb").read()
for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])