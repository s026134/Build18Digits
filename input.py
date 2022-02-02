from lib2to3.pytree import HUGE
import numpy as np
# import matplotlib
import cv2 as cv
import sys

capture = cv.VideoCapture(1)
calc_input = ""
ip = ""

def empty(a):
    pass

cv.namedWindow("Track Bars") # use following lines for testing color
cv.createTrackbar("hue min", "Track Bars", 0, 179, empty)
cv.createTrackbar("hue max", "Track Bars", 179, 179, empty)
cv.createTrackbar("sat min", "Track Bars", 0, 255, empty)
cv.createTrackbar("sat max", "Track Bars", 255, 255, empty)
cv.createTrackbar("val min", "Track Bars", 0, 255, empty)
cv.createTrackbar("val max", "Track Bars", 255, 255, empty)

def resizeVid(w, h):
    capture.set(3, w)
    capture.set(4, h)


def findGridPos(img):
    # find position of finger on grid
    return None


def isInput(img):
    # write code to determine if frame is an input, return boolean

    return True

def findingValues():
    while True:
        success, frame = capture.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # for getting the colors
        #############################################################
        minHue = cv.getTrackbarPos("hue min", "Track Bars")
        maxHue = cv.getTrackbarPos("hue max", "Track Bars")
        minSat = cv.getTrackbarPos("sat min", "Track Bars")
        maxSat = cv.getTrackbarPos("sat max", "Track Bars")
        minVal = cv.getTrackbarPos("val min", "Track Bars")
        maxVal = cv.getTrackbarPos("val max", "Track Bars")

        lower = np.array([minHue, minSat, minVal])
        upper = np.array([maxHue, maxSat, maxVal])
        mask = cv.inRange(hsv, lower, upper)
        cv.imshow("masked", mask)
        print(f"Hue min: {minHue} Hue max {maxHue}")
        print(f"Sat min: {minSat} Hue max {maxSat}")
        print(f"Val min: {minVal} Val max {maxVal}")


        #############################################################

        if cv.waitKey(30) == ord(
                'q'):  # this never triggers which is why I fear this is an infinite loop. Play around with break conditions.
            break  # maybe if the equals symbol is pressed, this break condition is met?


def findColor():
    while True:
        success, frame = capture.read()  # write code to process the frame image
        # cv.imshow('Frame', frame)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # cv.imshow('HSV', hsv)
        blurred = cv.GaussianBlur(hsv, (3,3), cv.BORDER_DEFAULT)

        #Hue, Sat, Val
        minRedColorVals = [0,139,121]
        maxRedColorVals = [179,255,255]
        minBlueColorVals = [84, 154, 112]
        maxBlueColorVals = [179,255,255]
        minOrangeColorVals = [0,149,165]
        maxOrangeColorVals = [179, 255, 255]

        #arrays
        lowerRed = np.array(minRedColorVals)
        lowerBlue = np.array(minBlueColorVals)
        upperRed = np.array(maxRedColorVals)
        upperBlue = np.array(maxBlueColorVals)
        lowerOrange = np.array(minOrangeColorVals)
        upperOrange = np.array(maxOrangeColorVals)

        #masks
        maskRed = cv.inRange(blurred, lowerRed, upperRed)
        maskBlue = cv.inRange(blurred, lowerBlue, upperBlue)
        maskOrange = cv.inRange(blurred, lowerOrange, upperOrange)

        # isInput(maskRed)
        # isInput(maskBlue)

        imgResult = cv.bitwise_and(frame, frame, mask=maskRed)
        imgResult2 = cv.bitwise_and(frame, frame, mask=maskBlue)

        # this is to make the bounding boxes
        # blurRed = cv.GaussianBlur(maskRed, (3, 3), cv.BORDER_DEFAULT)
        # cannyRed = cv.Canny(blurRed, 125, 175)
        contours, hierarchy = cv.findContours(maskRed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        if len(contours) != 0:
            for contour in contours:
                if cv.contourArea(contour) > 500 and cv.contourArea(contour) < 2000:
                    x, y, w, h = cv.boundingRect(contour)
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv.rectangle(imgResult, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # blurBlue = cv.GaussianBlur(maskBlue, (3, 3), cv.BORDER_DEFAULT)
        # cannyBlue = cv.Canny(blurBlue, 125, 175)
        # contours2, hierarchy2 = cv.findContours(maskBlue, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # if len(contours) != 0:
        #     for contour in contours2:
        #         if cv.contourArea(contour) > 500 and cv.contourArea(contour) < 2000:
        #             x, y, w, h = cv.boundingRect(contour)
        #             cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        #             cv.rectangle(imgResult2, (x, y), (x + w, y + h), (0, 0, 255), 3)


        # imgResult = cv.bitwise_and(frame, frame, mask=maskBlue)
        # imgHor = np.hstack((frame, hsv, imgResult, imgResult2))
        imgHor = np.hstack((frame, imgResult, imgResult2))
        imgHor2Masks = np.hstack((maskRed, maskBlue, maskOrange))

        #shows an image stacked horizontally (a dual image)
        cv.imshow("Horizontal", imgHor)
        cv.imshow("Masked Layers", imgHor2Masks)


        if cv.waitKey(30) == ord(
                'q'):  # this never triggers which is why I fear this is an infinite loop. Play around with break conditions.
            break  # maybe if the equals symbol is pressed, this break condition is met?


# enter inputs into calculator
# while(isInput()):
# isInput = False

findColor()
# findingValues()
capture.release()
cv.DestroyAllWindows()
