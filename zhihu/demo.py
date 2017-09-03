import time
import requests
from io import BytesIO
from PIL import Image
import numpy as np

myUrl = 'https://www.zhihu.com/people/mo-xie-gu-shi/activities'
url = 'https://www.zhihu.com'
loginUrl = 'https://www.zhihu.com/login/email'

headers = {
    # "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
    "Referer": "http://www.zhihu.com/",
    'Host': 'www.zhihu.com',
    'rememberme': "true"
}

data = {
    'email': 'goodme@163.com',
    'password': 'zhihu6112',
}


# timeStamp = int(time.time()*1000)
# captchaUrl = url + '/captcha.gif?=' + str(timeStamp)
# print(captchaUrl)
# # file = BytesIO(requests.get(captchaUrl, headers=headers).content)
# # img = Image.open(file)
# # img.show()
# for i in range(10):
#     with open('img/zhihu_img{}.jpg'.format(i), 'wb') as f:
#         f.write(requests.get(captchaUrl, headers=headers).content)


if __name__ == '__main__':
    mapList = ['3', '5', '6', '7', '8', '9', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'R', 'S', 'T',
               'U', 'V', 'X', 'Y']
    mapArray = np.array(mapList)
    print(type(mapArray))

        




