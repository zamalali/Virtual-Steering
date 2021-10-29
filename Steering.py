import cv2 as cv
from pynput.keyboard import Key, Controller
import pyautogui
import pydirectinput
from cvzone.HandTrackingModule import HandDetector
import math
import keyboard
cap =  cv.VideoCapture(0)
# keyboard = Controller()
detector = HandDetector(detectionCon=0.8 , maxHands=2)
while True:
    isTrue , img = cap.read()
    hands = detector.findHands(img ,draw=False)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        cp1 = hand1["center"]
        type1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            cp2 = hand2["center"]
            type2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            length , info , img = detector.findDistance(lmList1[8] , lmList2[8] , img)
            lst = list(info)
            pydirectinput.keyDown("w")
            # print(lst[3])
            if lst[1] > 290 :
                cv.putText(img , "Left" , (75,80) , cv.FONT_HERSHEY_COMPLEX , fontScale=2 , color= (0,0,255) , thickness= 3)
                pydirectinput.press("d")
            elif lst[1] < 230 :
                cv.putText(img , "Rght" , (75,80) , cv.FONT_HERSHEY_COMPLEX , fontScale=2 , color= (0,0,255) , thickness= 3)
                pydirectinput.press("a")
    else:
        continue
    cv.imshow("Webcam" , img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
