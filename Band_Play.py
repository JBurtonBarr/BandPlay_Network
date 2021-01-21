#Neural Network Band Test
import tensorflow as tf

num_rec = tf.keras.datasets.mnist #Dataset including handwritten numbers 0-9
 # Stick to these now and upgrade the system later
 # Have our encrypted message read in two number sets
 # the first number is the multiplier and the second is the "letter code"
      #This allows reach to all letters of the alphabet + better (although obvious) encryption
      # e.g. 2     7       = 14 = N

(x_train, y_train), (x_test, y_test) = num_rec.load_data()
