#!/usr/bin/python
# -*- coding: utf-8 -*
from keras.preprocessing import image
from keras.models import load_model
from keras import backend as K
import numpy as np


model = load_model('cat_dog_model.h5')
img_path = 'dog-4.png'
img = image.load_img(img_path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
#x = preprocess_input(x)

preds = model.predict(x)
# print(model.predict_proba(x))
# print(model.predict_classes(x))
class_num = int(preds[0][0])
print('Predicted:', class_num)
if class_num == 1:
    print('this image is dog !')
elif class_num == 0:
    print('this image is cat !')
# else:
#     print('this image is not dog or cat !')
K.clear_session()
