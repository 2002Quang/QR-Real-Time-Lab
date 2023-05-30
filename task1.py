import tensorflow as tf
import numpy as np
from keras.models import load_model
import cv2

class Task1:
    def __init__(self,index):
        print("Initiate task 1")
        np.set_printoptions(suppress=True)

        self.model = load_model("keras_model.h5", compile = False)
        self.class_names = open("prediction.txt", "r").readlines()

        self.camera = cv2.VideoCapture(index)
        self.cameraID = index
        return

    def Task1Run(self):
        print("Task1 is activated")
       
        ret, image = self.camera.read()

        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        cv2.imshow("Webcam Image", image)

        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        image = (image / 127.5) - 1

        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        keyboard_input = cv2.waitKey(1)
