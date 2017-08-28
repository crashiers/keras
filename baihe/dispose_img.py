from PIL import Image
from PIL import Image,ImageEnhance
import pytesseract




def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 244:
                count = count + 1
            if pixdata[x,y+1] > 244:
                count = count + 1
            if pixdata[x-1,y] > 244:
                count = count + 1
            if pixdata[x+1,y] > 244:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img


img = Image.open('vucx-0.jpg').convert("L")
# img.show()
# depoint(img).save('vucx-1.jpg')
sharpness =ImageEnhance.Contrast(img) #对比度增强
new_img = sharpness.enhance(2)  # 清晰度增加
new_img.show()

# depoint(new_img).save('vucx-3.jpg')
# code = pytesseract.image_to_string(new_img)
# print(code)



def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

# print(img.size) # (68, 23)
# img.thumbnail((34,12)) # 缩略图
# img.show()