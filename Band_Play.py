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
   # softmax - normalises the output to a probability distribution
       # causes a within 0-1 interval distribution

model.compile(optimizer = 'adam', loss= 'sparse_categorical_crossentrophy',
              metrics = ['accuracy'])
        #Add more metrics and compare optimizer
model.fit(x_train, y_train, epochs = 3)

#At this stage I want to optimise generalizability

loss, acc = model.evaluation(x_test, y_test)
print("Loss = " + loss + "\n" + "Accuracy = " + acc)


#model.save('thats_numberwang.model')
#Look into predictions (x.predict([test])
