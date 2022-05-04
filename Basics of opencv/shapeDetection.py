import cv2
import numpy as np
from StackingImages import stackingImages

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters" , 640,240)
cv2.createTrackbar("Threshold1" , "Parameters" , 23,255,empty)
cv2.createTrackbar("Threshold2" , "Parameters" , 20,255,empty)
cv2.createTrackbar("Area" , "Parameters" , 50,300,empty)

def getContours(img , imgContour):
    contours , heirarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

    for c in contours:
        area = cv2.contourArea(c)
        areaMin = cv2.getTrackbarPos("Area" , "Parameters")
        if area > areaMin:
            print(area)
            cv2.drawContours(imgContour, contours, -1, (0, 255, 0), 7)
            peri = cv2.arcLength(c , True)
            approx = cv2.approxPolyDP(c , 0.02*peri , True)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(c , (x,y),(x+w,y+h),(255,0,0),5)

            cv2.putText(c , "Points: "+str(len(approx)) , (x+w+20,y+20) , cv2.FONT_HERSHEY_SIMPLEX , 0.7,(0,0,255),2)
            cv2.putText(c, "Area: " + str(int(area)), (x + w + 20, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 255), 2)


frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)


while True:
    success , img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img , (7,7) , 0)
    imgGray = cv2.cvtColor(imgBlur , cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1" , "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2" , "Parameters")
    imgCanny = cv2.Canny(imgGray , threshold1 ,threshold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny , kernel , iterations=1)
    getContours(imgDil , imgContour)
    imgStack = stackingImages(0.8, [[img, imgBlur, imgCanny ],[imgDil,imgContour,imgContour]])

    cv2.imshow("Result" , imgStack)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break