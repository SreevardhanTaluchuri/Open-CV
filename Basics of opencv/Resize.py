import cv2

path = "../Resources/lena.png"

img = cv2.imread(path)

cv2.imshow("Lena" , img)

cv2.waitKey(0)