import cv2
import numpy as np

def stackingImages(scale , imgArray):
    rows = len(imgArray)
    col = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0] , list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0,rows):
            for y in range(0,col):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y] , (0,0) , None , scale , scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y] , (imgArray[0][0].shape[1] , imgArray[0][0].shape[0]) , None , scale , scale)
                if len(imgArray[x][y].shape) ==2 :
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y] , cv2.COLOR_GRAY2BGR)
        imgBlank = np.zeros((height , width , 3) , np.uint8)
        hor = [imgBlank]*rows
        hor_con = [imgBlank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x],(0,0),None,scale,scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x],(imgArray[0].shape[1] , imgArray[0].shape[0]) , None , scale , scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x] , cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver






kernel = np.zeros((5,5) , np.uint8)

path = "../Resources/lena.png"
img = cv2.imread(path)
imgGrey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey , (7,7),0)
imgCanny = cv2.Canny(imgBlur , 100,200)
imgDilation = cv2.dilate(imgCanny , kernel , iterations=2)
imgEroded = cv2.erode(imgDilation , kernel , iterations=2 )
StackedImages = stackingImages(0.8 , [[img , imgBlur , imgCanny] , [imgEroded , imgGrey , imgDilation]])
cv2.imshow("Image...",StackedImages)

# cv2.imshow("Image...",img)
# cv2.imshow("Image Grey...",imgGrey)
# cv2.imshow("Image Blur" , imgBlur)
# cv2.imshow("Image Canny" , imgCanny)
# cv2.imshow("Image Dilation...",imgDilation)
# cv2.imshow("Image Erroded...",imgEroded)

cv2.waitKey(0)
