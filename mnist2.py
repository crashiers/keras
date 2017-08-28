#define our time-distributed setup
from keras.layers import TimeDistributed, Convolution2D, Activation, Reshape, np, GRU, Dropout, Dense
from keras.models import Sequential
from keras.optimizers import RMSprop

model = Sequential()
model.add(TimeDistributed(Convolution2D(8, 4, 4, border_mode='valid'), input_shape=(maxToAdd,1,size,size)))
model.add(Activation('relu'))
model.add(TimeDistributed(Convolution2D(16, 3, 3, border_mode='valid')))
#model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2),border_mode='valid')))
#model.add(Activation('relu'))
#model.add(TimeDistributed(Convolution2D(8, 3, 3, border_mode='valid')))
model.add(Activation('relu'))
model.add(Reshape((maxToAdd,np.prod(model.output_shape[-3:])))) #this line updated to work with keras 1.0.2
model.add(Activation('relu'))
model.add(GRU(output_dim=100,return_sequences=True))
model.add(GRU(output_dim=50,return_sequences=False))
model.add(Dropout(.2))
model.add(Dense(1))

rmsprop = RMSprop()
model.compile(loss='mean_squared_error', optimizer=rmsprop)