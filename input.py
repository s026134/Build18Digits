from lib2to3.pytree import HUGE
import numpy as np
# import matplotlib
import cv2 as cv
import sys
from grid import *
from calculator import *

capture = cv.VideoCapture(0)
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

def getCell(frame, x1, y1, x2, y2):
    numRows, numCols = getGridDim()
    avgX = (x1 + x2)/2 # find middle of bounding box
    avgY = (y1 + y2)/2
    gridWidth = frame.width
    gridHeight = frame.height
    cellWidth = gridWidth // numCols
    cellHeight = gridHeight // numRows
    row = int(avgY / cellHeight)
    col = int(avgX / cellWidth)

    return(row, col)

def collision(frame, boundingBoxes):
    # returns coords of intersecting rectangle OR if no intersection, returns (0,0,0,0)
    # collisions = []
    if(boundingBoxes == None):
        return False, (0,0,0,0)

    for X1, Y1, X2, Y2 in boundingBoxes:
        for x1, y1, x2, y2 in boundingBoxes:
            if((X1 < x1 < X2) and (Y1 < y2 < Y2)): # or ((X1 < x2 < X2) and (Y1 < y1 < Y2))):
                if(y1 < Y1):
                    return True, (X1,Y1,x2,y2)
                if(y1 > Y1):
                    return True, (X1, y1, x2, Y2)
            if((X1 < x2 < X2) and (Y1 < y1 < Y2)):
                if(y1 < Y1):
                    return True, (x1, Y1, X2, y2)
                if(y1 > Y1):
                    return True, (x1, y1, X2, Y2)
    return False, (0,0,0,0)

        # row, col = getCell(frame, x1, y1, x2, y2)
        # calculatorInput(row, col)


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
        boundingBoxes = []
        
        if len(contours) != 0:
            for contour in contours:
                if cv.contourArea(contour) > 500 and cv.contourArea(contour) < 2000:
                    x, y, w, h = cv.boundingRect(contour)
                    boundingBoxes.append((x, y, x+w, y+h))
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

        collide, coords = collision(frame, boundingBoxes)
        x1, y1, x2, y2 = coords
        if(collide):
            row, col = getCell(frame, x1, y1, x2, y2)
            calculatorInput(row, col)
        else:
            continue
        # imgResult = cv.bitwise_and(frame, frame, mask=maskBlue)
        # imgHor = np.hstack((frame, hsv, imgResult, imgResult2))
        imgHor = np.hstack((frame, imgResult, imgResult2))
        gridLayout(frame)
        imgHor2Masks = np.hstack((maskRed, maskBlue, maskOrange))

        #shows an image stacked horizontally (a dual image)
        # cv.imshow("Horizontal", imgHor)
        # cv.imshow("Masked Layers", imgHor2Masks)


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
