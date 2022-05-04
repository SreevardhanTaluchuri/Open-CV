import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture(0)
while True:
    timer = cv2.getTickCount()
    success , img = cap.read()
    img = detector.findPose(img)
    lmlist , bbox = detector.findPosition(img)
    # print(bbox['bbox'])
    x,y,w,h = int(bbox['bbox'][0]),int(bbox['bbox'][1]),int(bbox['bbox'][2]),int(bbox['bbox'][3])
    x,y,w,h = x,y,w-50,h-50
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3, 1)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    # track(img, bbox['bbox'])
    # print("Hello")
    cv2.imshow('Image...',img)
    cv2.waitKey(1)