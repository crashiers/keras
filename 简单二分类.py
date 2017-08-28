from keras.models import Sequential
from keras.layers import Dense, Activation


#模型搭建阶段
model= Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
# Dense(32) is a fully-connected layer with 32 hidden units.
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Sequential()代表类的初始化；
# Dense代表全连接层，此时有32个全连接层，最后接relu，输入的是100维度
# model.add，添加新的全连接层，
# compile，跟prototxt一样，一些训练参数,solver.prototxt

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, nb_epoch =10, batch_size=32)