import cv2
import numpy as np

kernel = np.ones((5,5) , np.uint8)

#Import an image
"""
img = cv2.imread("Resources/image.png")

cv2.imshow("Image " , img)

cv2.waitKey(0)
"""

#Import an video and Display it
"""
frameWidth = 640
frameHeight = 380

cap = cv2.VideoCapture("Resources/demo video.mp4")

while True:
    success , img = cap.read()
    img = cv2.resize(img , (frameWidth, frameHeight))
    cv2.imshow("Video " , img)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
"""

#Open an Webcam
"""
cap = cv2.VideoCapture(0)


while True:
    success , img = cap.read()
    cv2.imshow("Video" , img)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break
"""


#GreyScale
"""
img = cv2.imread("Resources/image.png")
imgGrey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("Image GreyScale " , imgGrey)
cv2.waitKey(0)
"""

#Blur
"""
img = cv2.imread("Resources/image.png")
imgBlur = cv2.GaussianBlur(img , (5,5), 0)
cv2.imshow("Image Blur " , imgBlur)
cv2.waitKey(0)
"""


#Edge Detection
"""
img = cv2.imread("Resources/image.png")
imgCanny = cv2.Canny(img ,50,50)
cv2.imshow("Image Canny " , imgCanny)
cv2.waitKey(0)
"""

#Dilation
"""
img = cv2.imread("Resources/image.png")
imgDilate = cv2.dilate(img , kernel , iterations= 1 )
cv2.imshow("Image Dilated " , imgDilate)
cv2.waitKey(0)
"""


#Erosion
img = cv2.imread("Resources/image.png")
imgErode = cv2.erode(img , kernel , iterations= 1 )
cv2.imshow("Image Erode " , imgErode)
cv2.waitKey(0)