# -*- coding: utf-8 -*-
"""Transfer Learning and Fine tuning model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B1R2OZDW13Wy1SCxDRJ6qIyA8J8Zdik3
"""

import tensorflow
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense,Flatten
from keras.applications.vgg16 import VGG16

!pip install tensorflow torchvision matplotlib
!pip install opendatasets --upgrade --quiet

import opendatasets as od
import os
from torchvision.datasets import ImageFolder
import matplotlib.pyplot as plt
import torchvision.transforms as tt
from torch.utils.data import random_split
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
import torch
import torch.nn as nn
import torch.nn.functional as F

conv_base = VGG16(
    weights='imagenet',
    include_top = False,
    input_shape=(300,300,3)
)

conv_base.trainable = True

set_trainable = False

for layer in conv_base.layers:
  if layer.name == 'block2_conv1' :
    set_trainable = True
  if set_trainable:
    layer.trainable = True
  else:
    layer.trainable = False


for layer in conv_base.layers:
  print(layer.name,layer.trainable)

conv_base.summary()

model = Sequential()

model.add(conv_base)
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

# generators
train_ds = keras.utils.image_dataset_from_directory(
    directory = '/content/real/', #fake
    labels='inferred',
    label_mode = 'int',
    batch_size=16,
    image_size=(300,300)
)

validation_ds = keras.utils.image_dataset_from_directory(
    directory = '/content/valid/', #real
    labels='inferred',
    label_mode = 'int',
    batch_size=16,
    image_size=(300,300)
)

# Normalize
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def process(image,label):
    image = tensorflow.cast(image/255. ,tensorflow.float32)

    #datagen = ImageDataGenerator(rotation_range=40, width_shift_range=0.2, height_shift_range=0.2)
    #image = datagen.random_transform(image)
    return image,label

train_ds = train_ds.map(process)
validation_ds = validation_ds.map(process)

model.compile(
    optimizer=keras.optimizers.RMSprop(learning_rate=1e-5),
    loss='binary_crossentropy',
    metrics=['accuracy']
  )

history = model.fit(train_ds,epochs=10,validation_data=validation_ds)

plt.plot(history.history['accuracy'],color='red',label='train')
plt.plot(history.history['val_accuracy'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.plot(history.history['accuracy'],color='green',label='train')
plt.plot(history.history['val_accuracy'],color='black',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['accuracy'],color='green',label='train')
plt.legend()
plt.show()

plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.plot(history.history['val_accuracy'],color='black',label='validation')
plt.legend()
plt.show()

from tensorflow.keras.preprocessing.image import load_img, img_to_array

img = load_img("1.png", target_size=(224, 224))

image_array = img_to_array(img)

image_array = image_array.reshape((1, 3, 224, 224)) / 255.0

from tensorflow.keras.applications.vgg16 import preprocess_input

processed_image = preprocess_input(image_array)

from google.colab import drive
drive.mount('/content/drive')

model.save('/content/drive/MyDrive/MODEL/my_model.keras')



print(model.input_shape)
import numpy as np

import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Assuming your Google Drive is already mounted

# Specify the path to your fine-tuned model
model_path = '/content/drive/MyDrive/MODEL/VGG16.h5'

# Load your fine-tuned model
model = load_model(model_path)

# Define the function to predict and display an image
def predict_image(image_path):
    # Load and prepare image
    img = load_img(image_path, target_size=(300, 300))
    image_array = img_to_array(img)
    image_array = image_array.reshape((1, 300, 300, 3)) / 255.0

    # Predict and interpret
    prediction = model.predict(image_array)
    threshold = 1  # Adjust threshold based on your model performance

    if prediction[0] > threshold:
        print("Predicted:", "Deepfake image")
        plt.imshow(img)
        plt.title("Predicted Deepfake")
        plt.show()
    else:
        print("Predicted:", "Real Image")
        plt.imshow(img)
        plt.title("Predicted Real")
        plt.show()

# Example usage
image_path = '/content/1.jpg'
predict_image(image_path)

image_path = '/content/2.jpg'
predict_image(image_path)

image_path = '/content/3.jpg'
predict_image(image_path)

image_path = '/content/4.jpg'
predict_image(image_path)
image_path = '/content/5.jpg'
predict_image(image_path)
image_path = '/content/6.jpg'
predict_image(image_path)
image_path = '/content/7.jpg'
predict_image(image_path)
image_path = '/content/8.jpg'
predict_image(image_path)
image_path = '/content/9.jpg'
predict_image(image_path)
image_path = '/content/10.jpg'
predict_image(image_path)
image_path = '/content/11.jpg'
predict_image(image_path)
image_path = '/content/12.jpg'
predict_image(image_path)
image_path = '/content/13.jpg'
predict_image(image_path)
image_path = '/content/14.jpg'
predict_image(image_path)
image_path = '/content/15.jpg'
predict_image(image_path)
image_path = '/content/16.jpg'
predict_image(image_path)