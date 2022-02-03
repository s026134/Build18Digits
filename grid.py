import numpy as np
import matplotlib
import cv2 as cv
import sys

capture = cv.VideoCapture(0) # 1 for external webcam

# def changeRes(w, h):
#     #only works for live video; same thing as a resize function(see imagePrac)
#     capture.set(3, w)
#     capture.set(4, h)

def getGridDim():
    return (6, 4)
    
def gridLayout(frame):
    # isTrue, frame = capture.read()
    # cv.line(frame,(10,10),(10, frame.shape[0] - 10),(255,0,0),2)
    # cv.line(frame,(10,frame.shape[0] - 10),(frame.shape[1] - 10, frame.shape[0] - 10),(255,0,0),4)
    # cv.line(frame,(frame.shape[1] - 10, frame.shape[0] - 10),(frame.shape[1] - 10, 10),(255,0,0),4)
    # cv.line(frame,(frame.shape[1] - 10,10),(10, 10),(255,0,0),4)
    # cv.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (255, 0, 0), 4)
    gridDim = (6, 4)
    x,y = gridDim
    sqw = int(frame.shape[1]/y)
    sqh = int(frame.shape[0]/x)
    for i in range(0, x):
        cv.line(frame, (0,i*sqh), (frame.shape[1],i*sqh), (255, 0, 0), 4)
    for j in range(0, y):
        cv.line(frame, (j*sqw, 0), (j*sqw, frame.shape[0]), (255, 0, 0), 4)
    cv.imshow('Video', frame) #display each frame
    # if cv.waitKey(20) & 0xFF == ord('q'): #if d is pressed, break out of loop and stop playing video
    #     break
#capture.release()
#cv.destroyAllWindows()