from sre_parse import WHITESPACE
from tkinter import W
import cv2 as cv
import mediapipe as mp
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles

faceMesh = mpFaceMesh.FaceMesh( max_num_faces = 1, refine_landmarks=True)
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=2)
cap = cv.VideoCapture(0)

while True:
    success,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks :
        for faceLms in results.multi_face_landmarks :
            mpDraw.draw_landmarks(
                image=img,
                landmark_list=faceLms,
                connections=mpFaceMesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_tesselation_style())
            for i in range(0,468):
                pt1 = faceLms.landmark[i]
                ih,iw,ic = img.shape
                x = int(pt1.x*iw)
                y = int(pt1.y*ih)

                cv.circle(img, (x,y), 1, (255,0,0),1 )

    cv.imshow("cam",img)
    cv.waitKey(1)