import cv2
import numpy as np

circles = np.zeros((4,2) , np.int)
count = 0


def mousePoints(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[count] = x,y
        count = count + 1
        print(circles)


img = cv2.imread("Resources/image.png")
while True:

    if(count ==4):
        width , height = 250,350
        pts1 = np.float32([circles[0] , circles[1] ,circles[2] , circles[3]])
        pts2 = np.float32([[0,0] , [width,0] , [0,height] , [width,height]])
        matrix = cv2.getPerspectiveTransform(pts1 , pts2)
        imgOutput = cv2.warpPerspective(img, matrix , (width , height))
        cv2.imshow("Image...." , imgOutput)

    for x in range(0,4):
        cv2.circle(img , (circles[x][0],circles[x][1]) , 5 , (0,0,255) , cv2.FILLED)

    cv2.imshow("Image...." , img)
    cv2.setMouseCallback("Image....",mousePoints)
    cv2.waitKey(1)