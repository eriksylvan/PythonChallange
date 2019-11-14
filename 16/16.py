# http://www.pythonchallenge.com/pc/return/mozart.html


from PIL import Image

img = Image.open('mozart.gif')
pix = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]
(width, hight) = img.size
print("w/h",width,hight)

# Build new image
newimg = Image.new('RGB', (width * 2,hight))


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
        # print(f)
        pixel1 = img.getpixel((of, h))
        pixel2 = img.getpixel((of+2, h))
        pixel3 = img.getpixel((of+3, h))
        # print(pixel1, pixel2, pixel3)
        if (pixel1 == 195 and pixel2 == 195 and pixel3 == 195):
            offset.append(of)
            print("found")
            for w in range(0,width):
                pixel = img.getpixel((w,h))
                newimg.putpixel((w + of, h), pixel)
                print(pixel)
            break


newimg.save('newImg.gif')





 # for i in range():
#     for j in range(100):
#         pixel = img.getpixel((i*100+j,0))
#         newimg.putpixel((i,j), pixel)
#
# newimg.save('newImg.jpg')
#
# 249
# 195
# BoooM!!
# 195
# BoooM!!
# 195
# BoooM!!
# 195
# BoooM!!
# 195
# BoooM!!
# 252
