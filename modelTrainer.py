
#!/usr/bin/python3
# enable debugging
import cgitb
cgitb.enable()

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import to_categorical

import numpy
from numpy import array
# fix random seed for reproducibility
numpy.random.seed(7)
dataset = numpy.loadtxt("dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:54]
Y = to_categorical(dataset[:,54])
#print(X)
#print("---------")
#print(Y)

#data normalization

def normalize(column_id):
    column = []
    for x in range(len(X[0])):
        column.append(X[x][column_id])
    cmax = max(column)
    cmin = min(column)
    for x in range(len(X[0])):
        cval = X[x][column_id]
        X[x][column_id] = (cval - cmin) / (cmax - cmin)
    return column
    #normalized_data = (data - minimum) / (maximum - minimum)

model = Sequential()
model.add(Dense(55, input_dim=54, activation='relu'))
model.add(Dense(36, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.05), metrics=['accuracy'])
model.fit(X, Y, epochs=20, batch_size=10, shuffle=True)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

weights_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(weights_json)
model.save_weights("model.h5")