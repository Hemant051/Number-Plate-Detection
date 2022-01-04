#Number Plate Detection

import cv2
import numpy as np
########################################################################################
frameWidth = 640
frameHeigth = 480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
########################################################################################

vid = cv2.VideoCapture(0)
vid.set(3,frameWidth)
vid.set(4,frameHeigth)
vid.set(10,150)
count = 0

while True:
    success, frame = vid.read()


    vidGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    numberPlate = nPlateCascade.detectMultiScale(vidGray, 1.1, 4)

    for (x,y,w,h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),5)
            cv2.putText(frame,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            frameRoi = frame[y:y+h,x:x+w]
            cv2.imshow("ROI",frameRoi)

    cv2.imshow("Result",frame)
    if cv2.waitKey(1) & 0XFF == ord("s"):
        cv2.imwrite("scanned/NoPlate_"+str(count)+".jpg",frameRoi)
        cv2.rectangle(frame,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",frame)
        cv2.waitKey(500)

        count += 1
        break
