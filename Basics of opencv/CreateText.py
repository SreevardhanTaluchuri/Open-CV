import cv2
import numpy as np

img = np.zeros((512,512,3) , np.uint8)

cv2.line(img,(0,0),(img.shape[1] , img.shape[0]) , (0,255,0) ,3 )
cv2.rectangle(img,(300,300) , (200,200) , (0,0,255) , cv2.FILLED )
cv2.putText(img,"Hello World!" , (50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL , 1,(255,0,0))
cv2.imshow("IMAGE..,",img)
cv2.waitKey(0)