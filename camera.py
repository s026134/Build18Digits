import cv2 as cv
from HandGestures import *

#in our case cap would be the tape
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
#brightness
cap.set(10, 150)

def snapshot(frame, x1, y1, x2, y2, isPic):
    # pass in frame in which picture is being taken
    cropped = frame.copy()
    if(y1 > y2):
        if(x1 > x2):
            cropped = frame[y2:y1, x2:x1].copy()
        if(x2 > x1):
            cropped = frame[y2:y1, x1:x2].copy()
    if(y2 > y1):
        if(x1 > x2):
            cropped = frame[y1:y2, x2:x1].copy()
        if(x2 > x1):
            cropped = frame[y1:y2, x1:x2].copy()
    if(isPic):
        cv.imshow("Snapshot",cropped)
        cv.waitKey(0)


while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break