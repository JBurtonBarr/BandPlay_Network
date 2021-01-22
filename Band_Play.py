#Neural Network Band Test
import tensorflow as tf
import matplotlib as plt

num_rec = tf.keras.datasets.mnist #Dataset including handwritten numbers 0-9
 # Stick to these now and upgrade the system later
 # Have our encrypted message read in two number sets
 # the first number is the multiplier and the second is the "letter code"
      #This allows reach to all letters of the alphabet + better (although obvious) encryption
      # e.g. 2     7       = 14 = N

(x_train, y_train), (x_test, y_test) = num_rec.load_data()


x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)
# Normalisation helps the network learn

plt.imshow(x_train[0])
plt.show()

model = tf.keras.models.Sequential()
   #Feed forward model

model.add(tf.keras.layers.Flatten())
  #Clean up mess

model.add(tf.keras.layers.Dense(256, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(256, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
   # output layer = number of possible outcomes 
