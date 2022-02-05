import cv2
import time
import os
from cvzone.HandTrackingModule import HandDetector
from matplotlib.pyplot import draw

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=4)
#previousTime
pTime = 0

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

        lmList = detector.findPosition(img, draw = False)
 
        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        #length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw

        #Finger Counting code
        if len(lmList) != 0:
            fingers = []

            #Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                   fingers.append(1)
                else:
                    fingers.append(0)
        
            print(f'One Hand: {fingers}')
            
        

 
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right

            lmList2Hands = detector.findPosition(img, draw = False)
            #Finger Counting code
            if len(lmList2Hands) != 0:
                fingers = []
                for id in range(0,5):
                    if lmList2Hands[tipIds[id]][2] < lmList2Hands[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
            
                print(f'Two Hands: {fingers}')
 
            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw

            #centerpoint 1 and centerpoint 2 contain the (x,y) coordinates for each center
            x1,y1 = centerPoint1
            x2,y2 = centerPoint2


    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(30) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()