# http://www.pythonchallenge.com/pc/return/5808.html

# pip install pillow

from PIL import Image

img = Image.open('cave.jpg')
pix = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
(width, hight) = img.size
print("w/h",width,hight)

# Build new image
evenImg = Image.new('RGB', (width // 2, hight // 2))
oddImg = Image.new('RGB', (width // 2, hight // 2))

for i in range(width):
    for j in range(hight):
        pixel = img.getpixel((i,j))
        if (i + j) % 2 == 1:
            oddImg.putpixel((i // 2, j // 2), pixel)
        else:
            evenImg.putpixel((i // 2, j // 2), pixel)
evenImg.save('even.jpg')
oddImg.save('odd.jpg')
