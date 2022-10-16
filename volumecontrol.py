import cv2 as cv
import time
import HandTrackingModule as htm
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volrange = volume.GetVolumeRange()
minVol = volrange[0]
maxVol = volrange[1]
volume.SetMasterVolumeLevel(0, None)
pTime = 0
cTime = 0
cap = cv.VideoCapture(0)

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw = False)

    if len(lmlist)!=0 :
        x1,y1 = lmlist[4][1] , lmlist[4][2]
        x2,y2 = lmlist[8][1] , lmlist[8][2]
        xc,yc = (x1+x2)//2 , (y1 + y2)//2
        cv.circle(img,(x2,y2),7,(255,0,255),cv.FILLED)
        cv.circle(img,(x1,y1),7,(255,0,255),cv.FILLED)
        cv.circle(img,(xc,yc),9,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        length = math.hypot(x2 - x1,y2 - y1)
        vol = np.interp(length ,[50,300],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol,None)
        if(length <50) :
            cv.circle(img, (xc, yc), 9, (0, 255, 0), cv.FILLED)


    cv.imshow("Image", cv.flip(img,1))
    cv.waitKey(1)