import cv2 as cv
import time
import os
from cvzone.HandTrackingModule import HandDetector
from matplotlib.pyplot import draw
from HandTrackingModule import *
from calculator import *
from grid import *

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=4) # maybe change maxHands to 2
#previousTime
pTime = 0

def getCell(frame, x1, y1, x2, y2):
    numRows, numCols = getGridDim()
    avgX = (x1 + x2)/2 # find middle of bounding box
    avgY = (y1 + y2)/2
    gridWidth = frame.shape[1]
    gridHeight = frame.shape[0]
    cellWidth = gridWidth // numCols
    cellHeight = gridHeight // numRows
    row = int(avgY / cellHeight)
    col = int(avgX / cellWidth)
    cv.rectangle(frame, (cellWidth*(col - 1), cellHeight*(row - 1)), (cellWidth*col, cellHeight*row),(0, 0, 255), 4)
    cv.imshow("getCell", frame)
    print(row, col)
    return row, col

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (500, 70), cv2.FONT_HERSHEY_PLAIN, 
    3,(255,0,0), 3)

    tipIds = [4, 8, 12, 16, 20]

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        
        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        #length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw
 
        if len(hands) == 2:
            lmList_hand1 = detector.findPosition(img, 1, draw = False)

            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right

            #Finger Counting code
            if len(lmList_hand1) != 0:
                fingers = []
                # print(lmList_hand1)
                # for id in range(0,5):
                #     if lmList2Hands[tipIds[id]][2] < lmList2Hands[tipIds[id]-2][2]:
                #         fingers.append(1)
                #     else:
                #         fingers.append(0)
            
                # print(f'Two Hands: {fingers}')
 
            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw

            #centerpoint 1 and centerpoint 2 contain the (x,y) coordinates for each center
            x1,y1 = centerPoint1
            x2,y2 = centerPoint2

        else:
            lmList_hand1 = detector.findPosition(img, 0, draw = False)
            #Finger Counting code
            if len(lmList_hand1) != 0:
                fingers = []

                #Thumb
                if lmList_hand1[tipIds[0]][1] > lmList_hand1[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for id in range(1,5):
                    if lmList_hand1[tipIds[id]][2] < lmList_hand1[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                if(fingers[1] == 1):
                    if(fingers[2] == 1):
                        x1 = lmList_hand1[tipIds[1]][1]
                        y1 = lmList_hand1[tipIds[1]][2]
                        row, col = getCell(img, x1, y1, x1, y1)
                        calculatorInput(row,col)
                print(f'One Hand: {fingers}')
            


    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(30) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()