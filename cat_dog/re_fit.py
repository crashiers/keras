from keras.callbacks import EarlyStopping
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator


model = load_model('cat_dog_model.h5')
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