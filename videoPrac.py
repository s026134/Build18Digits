import numpy
import matplotlib
import cv2 as cv
import sys


capture = cv.VideoCapture(0) # 1 for external webcam

def changeRes(w, h):
    #only works for live video; same thing as a resize function(see imagePrac)
    capture.set(3, w)
    capture.set(4, h)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame) #display each frame

    if cv.waitKey(20) & 0xFF == ord('d'): #if d is pressed, break out of loop and stop playing video
        break
capture.release()
cv.destroyAllWindows()