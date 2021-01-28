#Neural Network Band Test

#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
import matplotlib.pyplot as plt





print("Reach: 1")
num_rec = tf.keras.datasets.mnist #Dataset including handwritten numbers 0-9
 # Stick to these now and upgrade the system later
 # Have our encrypted message read in two number sets
 # the first number is the multiplier and the second is the "letter code"
      #This allows reach to all letters of the alphabet + better (although obvious) encryption
      # e.g. 2     7       = 14 = N

print("Reach: 2")
(x_train, y_train), (x_test, y_test) = num_rec.load_data()


print("Reach: 3")

x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)
# Normalisation helps the network learn


print("Reach: 4")
#plt.imshow(x_train[0])
#plt.show()

model = tf.keras.models.Sequential()
   #Feed forward model

print("Reach: 5")

model.add(tf.keras.layers.Flatten())
  #Clean up mess

print("Reach: 6")

model.add(tf.keras.layers.Dense(32, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(32, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
   # output layer = number of possible outcomes
   # softmax - normalises the output to a probability distribution
       # causes a within 0-1 interval distribution

print("Reach: 7")

model.compile(optimizer = 'adam', loss= 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])
        #Add more metrics and compare optimizer
print("Reach: 8")

model.fit(x_train, y_train, epochs = 3)


print("Reach: 9")
#At this stage I want to optimise generalizability

#loss, acc = model.evaluation(x_test, y_test)
#print("Loss = " + loss + "\n" + "Accuracy = " + acc)


model.save('thats_numberwang.model')
print("Reach: Saved")

predictions = (x.predict([test]))
