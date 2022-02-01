from lib2to3.pytree import HUGE
import numpy as np
#import matplotlib
import cv2 as cv
import sys

capture = cv.VideoCapture(0)
calc_input = ""
ip = ""
# cv.namedWindow("Track Bars") # use following lines for testing color
# cv.createTrackbar("hue min", "Track Bars", 0, 179, empty)
# cv.createTrackbar("hue max", "Track Bars", 179, 179, empty)
# cv.createTrackbar("sat min", "Track Bars", 0, 255, empty)
# cv.createTrackbar("sat max", "Track Bars", 255, 255, empty)
# cv.createTrackbar("val min", "Track Bars", 0, 255, empty)
# cv.createTrackbar("val max", "Track Bars", 255, 255, empty)
def resizeVid(w, h):
    capture.set(3, w)
    capture.set(4, h)

def findGridPos(img):
    # find position of finger on grid
    return None

def isInput(img):
    # write code to determine if frame is an input, return boolean
    
    return True

def findColor():
    while True:
        success, frame = capture.read() # write code to process the frame image
        #cv.imshow('Frame', frame)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #cv.imshow('HSV', hsv)

        while True:
            minHueRed = cv.getTrackbarPos("hue min", "Track Bars") # next 6 lines: change to values recorded on Monday 1/31 + get rid of trackbars.
            minHueBlue = cv.getTrackbarPos("hue min", "Track Bars")
            maxHue = 179 # max is always 179 for Hue
            minSatRed = cv.getTrackbarPos("sat min", "Track Bars") # will need separate values for red and blue
            minSatBlue = cv.getTrackbarPos("sat min", "Track Bars")
            maxSat = 255 # maxSat is always 255 (unless we're working with yellow - that's a different story lol)
            minValRed = cv.getTrackbarPos("val min", "Track Bars")
            minValBlue = cv.getTrackbarPos("val min", "Track Bars")
            maxVal = 255 # maxVal is always 255 (again, may have to play around with this for colors other than red and blue)
            lowerRed = np.array([minHueRed, minSatRed, minValRed])
            lowerBlue = np.array([minHueBlue, minSatBlue, minValBlue])
            upper = np.array([maxHue, maxSat, maxVal])
            maskRed = cv.inRange(hsv, lowerRed, upper)
            maskBlue = cv.inRange(hsv, lowerBlue, upper)
            #result = cv.bitwise_and(frame, frame, mask=mask)
            cv.imshow("og", frame)
            cv.imshow("hsv", hsv)
            cv.imshow("red masked", maskRed)
            cv.imshow("blue masked", maskBlue)
            isInput(maskRed)
            isInput(maskBlue)
            #cv.waitKey(30)
            if cv.waitKey(30) == ord('d'): # probably an issue with these if statements
                break                      # also, need to change this break condition; next frame shouldn't have to wait for d to pressed to capture a frame
                                           # could possibly have some kind of isInput variable/method that returns True if the frame registers a valid input
                                           # consider using datetime class? Maybe try processing 2 or 3 frames per second (break condition checks time instead)
        #cv.waitKey(30)
        if cv.waitKey(30) == ord('q'): # this never triggers which is why I fear this is an infinite loop. Play around with break conditions. 
            break                      # maybe if the equals symbol is pressed, this break condition is met?
# enter inputs into calculator
#while(isInput()): 
   #isInput = False

findColor()
capture.release()
cv.DestroyAllWindows()





