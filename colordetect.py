import numpy as np
import matplotlib
import cv2 as cv
import sys

def empty(a):
    pass

capture = cv.VideoCapture(1)
cv.namedWindow("Track Bars") # use following lines for testing color
cv.resizeWindow("Track Bars", 250, 250)
cv.createTrackbar("hue min", "Track Bars", 0, 179, empty)
cv.createTrackbar("hue max", "Track Bars", 179, 179, empty)
cv.createTrackbar("sat min", "Track Bars", 0, 255, empty)
cv.createTrackbar("sat max", "Track Bars", 255, 255, empty)
cv.createTrackbar("val min", "Track Bars", 0, 255, empty)
cv.createTrackbar("val max", "Track Bars", 255, 255, empty)

while True:
    success, frame = capture.read() # write code to process the frame image
    #cv.imshow('Frame', frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #cv.imshow('HSV', hsv)

    while True:
        minHue = cv.getTrackbarPos("hue min", "Track Bars")
        maxHue = cv.getTrackbarPos("hue max", "Track Bars")
        minSat = cv.getTrackbarPos("sat min", "Track Bars")
        maxSat = cv.getTrackbarPos("sat max", "Track Bars")
        minVal = cv.getTrackbarPos("val min", "Track Bars")
        maxVal = cv.getTrackbarPos("val max", "Track Bars")
        lower = np.array([minHue, minSat, minVal])
        upper = np.array([maxHue, maxSat, maxVal])
        mask = cv.inRange(hsv, lower, upper)
        #result = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("og", frame)
        cv.imshow("hsv", hsv)
        cv.imshow("masked", mask)
        #cv.waitKey(30)
        if cv.waitKey(30) == ord('d'): # probably an issue with these if statements
            break
    #cv.waitKey(30)
    if cv.waitKey(30) == ord('q'):
            break

capture.release()
cv.destroyAllWindows()