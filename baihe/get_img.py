import random
from os import path
import os
from io import BytesIO
import requests
import time
from PIL import Image

def get_img(i):
    if not path.exists('baihe_img'):
        os.makedirs('baihe_img')
    tmpId = "%d.%s" % (time.time() * 1000, str(round(random.random(), 4))[2:])
    url = "http://my.baihe.com/Getinterlogin/getVerifyPic?jsonCallBack=?&tmpId=%s"%tmpId
    # url2 = 'http://www.zhihu.com/captcha.gif'
    # file = BytesIO(requests.get(url).content)
    # img = Image.open(file)
    # img.show()
    with open('baihe_img/{}.jpg'.format(i),'wb')as f:
        f.write(requests.get(url).content)
        print('save number {}'.format(i))



if __name__ == '__main__':
    i = 385
    while True:
        i += 1
        get_img(i)
        if i == 500:
            break