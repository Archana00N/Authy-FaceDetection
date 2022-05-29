from cv2 import face_recognition
import pickle
import cv2, time

video = cv2.VideoCapture(0)

a=1
while True:
    a= a+1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BGR2GRAY)
    cv2.imshow('Capture',gray)
    key = cv2.waitkey(1)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()