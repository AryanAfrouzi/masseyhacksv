
#!/usr/bin/python3
# enable debugging
import cgitb
cgitb.enable()

from keras.models import Sequential
from keras.layers import Dense
import numpy
from numpy import array
# fix random seed for reproducibility
numpy.random.seed(7)
dataset = numpy.loadtxt("dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:54]
Y = dataset[:,54]
print(X)
print("---------")
print(Y)

model = Sequential()
model.add(Dense(12, input_dim=54, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=200, batch_size=20)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

weights_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(weights_json)
model.save_weights("model.h5")