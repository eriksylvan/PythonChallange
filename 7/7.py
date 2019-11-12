# http://www.pythonchallenge.com/pc/def/oxygen.html

# pip install pillow

from PIL import Image

img = Image.open('oxygen.png')
pix = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
print(img.size) # (width, height)


for i in range(0,629,7):
    pix = img.getpixel((i,47))
    if pix[0]==pix[1] and pix[0]==pix[2]:
        #print(pix)
        print(chr(pix[0]),end='')
print()


# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for ch in answer:
    print(chr(ch),end='')