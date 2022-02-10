import cv2
import numpy as np

#Black Image
"""
black = np.zeros((512,512,3) , np.uint8)

print(black)
cv2.imshow("Black Image....",black)
cv2.waitKey(0)
"""

#Converting from black to blue
"""
black = np.zeros((512,512,3) , np.uint8)
black[:] = 255, 0,0
cv2.imshow("Blue Image" , black)
cv2.waitKey(0)
"""

#Draw a line 
"""
black = np.zeros((512,512,3) , np.uint8)

cv2.line(black , (0,0),(black.shape[1] , black.shape[1]) ,(0,0,255), 2)
cv2.imshow("Blue Image" , black)
cv2.waitKey(0)
"""

#Draw a rectangle
"""
cv2.rectangle(black , (0,0) , (100,200) , (0,0,255) , cv2.FILLED)
cv2.imshow("Blue Image" , black)
cv2.waitKey(0)
"""

#Draw a circle
"""
cv2.circle(black , (170,360) , 30 ,(255,0,0), cv2.FILLED)
cv2.imshow("Blue Image" , black)
cv2.waitKey(0)
"""

#Write Text
black = np.zeros((512,512,3) , np.uint8)
cv2.putText(black , "This is Black Background....." , (78,57),cv2.FONT_HERSHEY_SIMPLEX,2,(0,150,0))
cv2.imshow("Blue Image" , black)
cv2.waitKey(0)