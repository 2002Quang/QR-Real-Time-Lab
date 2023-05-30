import tensorflow as tf
import numpy as np
from PIL import Image

class Task1:
    def __init__(self):
        print("Initiate task 1")
        return

    def Task1_Run(self):
        print("Task 1 is activated")

    def classify_image(self, image_path):
        model = tf.keras.models.load_model('C:/Users/Administrator/Desktop/Subjects/Realtime System/keras_model.h5')
        
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
        
        prediction = model.predict(img_array)
        predicted_class = tf.keras.applications.resnet50.decode_predictions(prediction, top=1)[0][0][1]
        
        return predicted_class
