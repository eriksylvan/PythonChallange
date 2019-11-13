# http://www.pythonchallenge.com/pc/return/italy.html

# pip install pillow

from PIL import Image

img = Image.open('wire.png')
pix = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
(width, hight) = img.size
print("w/h",width,hight)

# Build new image
newimg = Image.new('RGB', (100,100))

for i in range(100):
    for j in range(100):
        pixel = img.getpixel((i*100+j,0))
        newimg.putpixel((i,j), pixel)

newimg.save('newImg.jpg')
# bit
#you took the wrong curve.

# Image will be built by 50 rounds
#
#         top
#      ----------
#      |        |
# left |        | right
#      |        |
#      ---------|
#        bottom
#
#  toplength = 100 - 2n
#  topstart = (n,n)
#  topend = (100 - n -1, n)
#  rightlength = top - 1
#  rightstart = (toplength + 2n, n+1)
#  bottomlength = top - 1
#  bottomstart = (100 - 2n -1, 100 - n)
#  leftlength = top - 2
#  leftstart = (n, 100 - 2n)


# Build newer image
newerimg = Image.new('RGB', (100,100))

pixpos = 0
for n in range(50): # n = 0..49
    topstart = n
    topend = 100-n
    rightstart = n+1
    rightend = 100-n
    bottomstart = 100-n-2
    bottomend = n-1
    leftstart = 100-n-1
    leftend = n+1

    # top loop
    # # print("top ", n)
    # print("len ",topend - topstart)
    for t in range(topstart, topend):
        pixel = img.getpixel((pixpos, 0))
        newerimg.putpixel((t,n),pixel)
        pixpos+=1
        #print(t,end=',')

    # rigth loop
    # print("right ", n)
    # print("len ",rightend - rightstart)
    for r in range(rightstart, rightend):
        pixel = img.getpixel((pixpos, 0))
        newerimg.putpixel((100-n-1, r),pixel)
        pixpos += 1
        #print(r, end=',')

    # bottom loop
    # print("bottom ", n)
    # print("len ", bottomstart - bottomend)
    for b in range(bottomstart, bottomend,-1):
        pixel = img.getpixel((pixpos, 0))
        newerimg.putpixel((b,100-n-1), pixel)
        pixpos += 1
        #print(b,end=',')

    # left loop
    # print("left ", n)
    # print("len ",leftstart - leftend)
    for l in range(leftstart, leftend,-1):
        pixel = img.getpixel((pixpos, 0))
        newerimg.putpixel((n,l), pixel)
        pixpos += 1
        #print(l,end=',')

newerimg.save('newerImg.jpg')


