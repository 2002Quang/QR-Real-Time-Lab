from keras.models import load_model
import cv2
import numpy as np

class Task3:
    def __init__(self, index):
        print("Init Task 3")
        np.set_printoptions(suppress=True)

        # Load model
        self.model = load_model("keras_model.h5", compile=False)

        # Load file
        self.class_names = open("prediction.txt", "r").readlines()
        self.camera = cv2.VideoCapture(index)
        self.cameraID = index
        return

    def Task3Run(self):
        print("Task 3 is activated!")
        print("camera number " + str(self.cameraID) + "is activated")

        # Grab the webcamera's image.
        ret, image = self.camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)
