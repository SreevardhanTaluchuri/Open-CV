import cv2
import numpy as np

counter = 0
circles = []

def mousePoints(event , x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(x,y)

img = cv2.imread("../Resources/cards.jpg")

while True:
    if counter ==4:
        width , height = 250,350
        pts1 = np.float32([circles[0], circles[1] ,circles[2] , circles[3] ])
        pts2 = np.float32([[0,0] , [width,0] , [ 0,height ] , [width , height]])
        matrix = cv2.getPerspectiveTransform(pts1 , pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width , height))
        cv2.imshow('Image Warp...', imgOutput)


    for x in range(0,4):
        cv2.circle(img , (circles[x][0] , circles[x][1]),3,(0,255,0) , cv2.FILLED)

cv2.imshow('Image...',img)
cv2.setMouseCallback("Image...",mousePoints)
cv2.waitKey(0)