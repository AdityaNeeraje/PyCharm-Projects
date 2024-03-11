import cv2
import mediapipe as mp
import time
from sign_language_letters import translate

# # Testing for Camera existence and quality
# cap = cv2.VideoCapture(0)
# pTime = 0
# while True:
#     success, image = cap.read()
#     imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     cTime = time.time()
#     fps = 1/(cTime - pTime)
#     pTime = cTime
#     cv2.putText(image, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
#     cv2.imshow("Test", image)
#     cv2.waitKey(1)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success, image = cap.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        print(results.multi_handedness)
        for handLms in results.multi_hand_landmarks:
            landmark_xcors = []
            landmark_ycors = []
            landmark_zcors = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy, z = round(lm.x*w, 3), round(lm.y*h, 3), round(lm.z, 3)
                cv2.circle(image, (int(cx),int(cy)), 3, (255,0,255), cv2.FILLED)
                landmark_xcors.append(cx)
                landmark_ycors.append(cy)
                landmark_zcors.append(z)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            translate(landmark_xcors, landmark_ycors, landmark_zcors, MessageToDict(results.multi_handedness[0]).label)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(image,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Hand Landmark Detector", image)
    cv2.waitKey(100)
