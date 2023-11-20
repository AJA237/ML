#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:44:31 2023

@author: aja
"""

import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout, BatchNormalization, Activation, AveragePooling2D

# instantiate the image data generator that containes the different transformations to be implemented on the images
train_generator = ImageDataGenerator(horizontal_flip=True, vertical_flip=True,
                                     rotation_range=45, height_shift_range=0.2,
                                     width_shift_range=0.2, zoom_range=0.2)

# fitting the transformer to the images in the training data set that containes our classes
# this identifies the classes as individual naming in this case cats and dogs
train_data = train_generator.flow_from_directory("C:/Users/Acer/Documents/ML/dataset/dog_and_cat/dataset/training_set",
                                                 class_mode='binary',
                                                 batch_size=50, target_size=(256, 256))

# instantiating the image data generator for our validation data.
# since no particular transformation needs to be done the image data generator instance takes no parameter
valid_generator = ImageDataGenerator()

# fitting the transformer to the images contained in the test_set folder
# this folder contains the cats and dogs classes as well in this case
valid_data = valid_generator.flow_from_directory("C:/Users/Acer/Documents/ML/dataset/dog_and_cat/dataset/test_set",
                                                 target_size=(256, 256),
                                                 class_mode='binary')

# instantiating an early stopping class
# this class help stop the training when the min_delta value is triggered
# in this case a drop of 0.01 value will stop the training process
# early_ending = EarlyStopping(min_delta=0.01)

# instantiating the model as a sequential enable a stack approach to be attain during training
# this is to ensure that the image passes through each layer in the model consecutively
model = Sequential()

# feature extraction (base layer)
# this layer is responsible for extracting the specific features from the image
# this layer involves three main actions to be carried
# -- filtering done by the convolution layer
# -- determine the useful features with the activation function
# -- accesntuate the
model.add(tensorflow.keras.layers.Rescaling(1./255, input_shape=(256, 256, 3)))
model.add(Conv2D(filters=64, kernel_size=3))
model.add(Activation('relu'))

model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(rate=0.2))
model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(filters=32, kernel_size=2))
model.add(Activation('relu'))

model.add(BatchNormalization())
model.add(AveragePooling2D(pool_size=2))
model.add(Dropout(rate=0.2))

# head layer
# class determination layer
model.add(BatchNormalization())
model.add(Dense(units=64, activation='relu'))
model.add(Flatten())
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer="adam",
              metrics=["accuracy"],
              loss='binary_crossentropy')

history = model.fit(train_data,
                    steps_per_epoch=len(train_data),
                    epochs=10,
                    # callbacks=[early_ending],
                    validation_data=valid_data,
                    validation_steps=len(valid_data))
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

model.save("cnn_updated.keras")
