from lib2to3.pytree import HUGE
import numpy as np
import matplotlib
import cv2 as cv
import sys

capture = cv.VideoCapture(0)
calc_input = ""
ip = ""

def resizeVid(w, h):
    capture.set(3, w)
    capture.set(4, h)

def findGridPos(img):
    # find position of finger on grid
    return None

def isInput():
    # write code to determine input, return boolean
    
    return True

def findColor():
    frame = capture.read() # write code to process the frame image
    
    newFrame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.namedWindow("Track Bars") # use following lines for testing color
    cv.createTrackbar("hue min", "Track Bars", 0, 179)
    cv.createTrackbar("hue max", "Track Bars", 179, 179)
    cv.createTrackbar("sat min", "Track Bars", 0, 255)
    cv.createTrackbar("sat max", "Track Bars", 255, 255)
    cv.createTrackbar("val min", "Track Bars", 0, 255)
    cv.createTrackbar("val max", "Track Bars", 255, 255)
    while True:
        minHue = cv.getTrackbarPos("hue min", "Track Bars")
        maxHue = cv.getTrackbarPos("hue max", "Track Bars")
        minSat = cv.getTrackbarPos("sat min", "Track Bars")
        maxSat = cv.getTrackbarPos("sat max", "Track Bars")
        minVal = cv.getTrackbarPos("val min", "Track Bars")
        maxVal = cv.getTrackbarPos("val max", "Track Bars")
        lower = np.array([minHue, minSat, minVal])
        upper = np.array([maxHue, maxSat, maxVal])
        mask = cv.inRange(newFrame, lower, upper)
        #result = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("og", frame)
        cv.imshow("hsv", newFrame)
        cv.imshow("masked", mask)
        cv.waitKey(1)
        key = cv.waitKey(0)
        if key == ord('d'):
            break

# enter inputs into calculator
#while(isInput()): 
   #isInput = False

findColor()
capture.release()
cv.DestroyAllWindows()





