from PIL import Image
from PIL import ImageEnhance
import os



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


def chage_img(img_path):
    img = Image.open(img_path).convert("L")
    # img.show()
    # depoint(img).save('tzwy-1.jpg')
    sharpness = ImageEnhance.Contrast(img)  # 对比度增强
    new_img = sharpness.enhance(2)  # 清晰度增加
    # new_img.save('tzwy-2.jpg')
    # new_img.show()

    depoint(new_img).save('baihe_img/new_{}'.format(img_path))
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


if __name__ == '__main__':
    img_path = input('input imgage path: ')
    chage_img(img_path)
