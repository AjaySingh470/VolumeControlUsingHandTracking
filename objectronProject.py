import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(1)
mpDraw = mp.solutions.drawing_utils
mpObj = mp.solutions.objectron
objecTron = mpObj.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.99,
                            model_name='Cup')
while True:
    sucess,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = objecTron.process(imgRGB)
    imgRGB.flags.writeable = True

    if results.detected_objects:
        for detected_object in results.detected_objects:
            mpDraw.draw_landmarks(img,detected_object.landmarks_2d, mpObj.BOX_CONNECTIONS)
            # mpDraw.draw_axis(img,detected_object.rotation,detected_object.translation)
    imgRGB = cv.cvtColor(imgRGB,cv.COLOR_RGB2BGR)

    cv.imshow("camm",img)
    cv.waitKey(1)