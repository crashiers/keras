import os
import random
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.preprocessing import image
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping


IMAGE_HEIGHT = 23
IMAGE_WIDTH = 68
MAX_CAPTCHA = 4
CHAR_SET_LEN = 26

def get_name_and_image():
    all_image = os.listdir('H:/rieuse/keras/baihe/baihe_img/')
    random_file = random.randint(0, 489)
    base = os.path.basename('H:/rieuse/keras/baihe/baihe_img/' + all_image[random_file])
    name = os.path.splitext(base)[0]
    image = Image.open('H:/rieuse/keras/baihe/baihe_img/' + all_image[random_file])
    image = np.array(image)
    return name, image


def name2vec(name):
    vector = np.zeros(MAX_CAPTCHA*CHAR_SET_LEN)
    for i, c in enumerate(name):
        idx = i * 26 + ord(c) - 97
        vector[idx] = 1
    return vector


def vec2name(vec):
    name = []
    for i in vec:
        print(i)
        a = chr(int(i) + 97)
        name.append(a)
    return "".join(name)

def get_next_batch(batch_size=64):
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT*IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA*CHAR_SET_LEN])

    for i in range(batch_size):
        name, image = get_name_and_image()
        batch_x[i, :] = 1*(image.flatten())
        batch_y[i, :] = name2vec(name)
    return batch_x, batch_y


model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(23, 68,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(64,(3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    'data/train',  # this is the target directory
    target_size=(150, 150),  # all images will be resized to 150x150
    batch_size=32,
    class_mode='binary',
    classes=['dog','cat'])  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
validation_generator = test_datagen.flow_from_directory(
    'data/validation',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary')


early_stopping = EarlyStopping(monitor='val_loss', patience=2)
model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=100,
        validation_data=validation_generator,
        validation_steps=100,
        callbacks=[early_stopping])
model.save('cat_dog_model2.h5')
model.save_weights('cat_dog_weights2.h5')