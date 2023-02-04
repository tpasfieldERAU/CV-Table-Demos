import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

def rects(img):
    b,g,r = cv2.split(img)
    imgGray = r

    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)
    eyes = eyeCascade.detectMultiScale(imgGray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    for (x, y, w, h) in eyes:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

    return img