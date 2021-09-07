import cv2
from cvzone.HandTrackingModule import HandDetector
import random

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

magenta = (255, 0, 255)
colorR = magenta
cx, cy = 100, 100
width, height = 100, 100
offset = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    if lmList:

        # l,_,_ = detector.findDistance(8,12,img)
        l, _, _ = detector.findDistance(4, 8, img)
        cursor = lmList[8]
        if (
            l < 40
            and cx - width // 2 < cursor[0] < cx + width // 2
            and cy - height // 2 < cursor[1] < cy + height // 2
        ):
            colorR = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            offset += 100
            cx, cy = cursor  # drag
        else:
            colorR = magenta
            offset = 0
    cv2.rectangle(
        img,
        (cx - width // 2, cy - height // 2),
        (offset + cx + width // 2, offset + cy + height // 2),
        colorR,
        cv2.FILLED,
    )
    cv2.imshow("Image", img)
    cv2.waitKey(1)
