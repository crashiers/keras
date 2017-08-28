from keras import models
from keras.models import Sequential
from keras.layers import Dense, Activation


# layer = Dense(32)
# config = layer.get_config()
# reconstructed_layer = Dense.from_config(config)
# print(layer.get_config())

# model = Sequential()
# model.add(Dense(32, input_shape=(16,)))
# print(model)

# now the model will take as input arrays of shape (*, 16)
# and output arrays of shape (*, 32)
# this is equivalent to the above:
model = Sequential()
model.add(Dense(32, input_shape=(16,)))
# after the first layer, you don't need to specify
# the size of the input anymore:
model.add(Dense(32))
Dense()
