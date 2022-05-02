import cv2 as cv2

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    cv2.imshow('Img...',img)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

 