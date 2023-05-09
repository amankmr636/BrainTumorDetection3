import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import normalize
from keras.utils import to_categorical

image_directory="datasets/"

no_tumor_images=os.listdir(image_directory+'no/')
yes_tumor_images=os.listdir(image_directory+'yes/')

dataset = []
label = []

INPUT_SIZE = 64

print(no_tumor_images)

for i, image_name in enumerate(no_tumor_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = cv2.imread(image_directory + 'no/' + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((INPUT_SIZE, INPUT_SIZE))  # we are resizing images
        dataset.append(np.array(image))
        label.append(0)

for i, image_name in enumerate(yes_tumor_images):
    if (image_name.split('.')[1] == 'jpg'):
        image = cv2.imread(image_directory + 'yes/' + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((INPUT_SIZE, INPUT_SIZE))  # we are resizing images
        dataset.append(np.array(image))
        label.append(1)

dataset = np.array(dataset)
label = np.array(label)

x_train, x_test, y_train, y_test = train_test_split(dataset, label, test_size=0.2, train_size=0.8
                                                    , random_state=0)
print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

x_train = normalize(x_train, axis=1)
x_test = normalize(x_train, axis=1)

y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2)

from keras.engine.sequential import Sequential


model = Sequential()  # Initialising CNN
model.add(Conv2D(32, (3, 3), input_shape=(INPUT_SIZE, INPUT_SIZE, 3)))  # step -1 Convolution
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))  # step -2  Pooling

model.add(Conv2D(32, (3, 3), kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(64, (3, 3), kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
res = model.fit(np.array(x_train), np.array(y_train), verbose=1, epochs=20,
                shuffle=False)

model.save('BrainAma.h5')

import matplotlib.pyplot as plt

print(res.history.keys())

plt.plot(res.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()

print("Training accuracy")

plt.plot(res.history['accuracy'])
plt.title('Model Accuracy')
plt.legend(['Training Accuracy'])
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

