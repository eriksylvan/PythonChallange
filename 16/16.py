# http://www.pythonchallenge.com/pc/return/mozart.html


from PIL import Image

img = Image.open('mozart.gif')
piximg = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
print(piximg[1,1])
(width, hight) = img.size
mode = img.mode
print(mode)
print("w/h",width,hight)


# Build new image
newimg = Image.new(img.mode, (width, hight))
# dur to orgignal image have a Image.palette define, I copy this to the new image to get the colors right
newimg.putpalette(img.getpalette())

# for i in range(0, hight):
#     for f in range(0, width-7):
#         pixel = img.getpixel((f,0))
#         print(pixel)
#         if pixel==195:
#             print("BoooM!!")
#     print("================================")
    # if pixel[3]==0:
    #     print(f)

# pixel sequence to line up against(249, 195, 195, 195, 195, 195, 252)

offset = []
for h in range(0, hight):
    for of in range(0, width-7):
        pixel1 = img.getpixel((of, h))
        pixel2 = img.getpixel((of+1, h))
        pixel3 = img.getpixel((of+1, h))
        if pixel1 == 195 and pixel2 == 195 and pixel3 == 195:
            offset.append(of)
            for w in range(0,width):
                pixel = piximg[w,h]
                newimg.putpixel(((w-of)%width, h), pixel)
                # print(pixel)
            break


newimg.save('newImg.gif', format='GIF')


