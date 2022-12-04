import cv2
import mediapipe as mp
import pyautogui
import keyboard

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = (2048, 1280)
while True:
    pyautogui.FAILSAFE = False
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # print(landmarks[477].y - landmarks[475].y)
        if (left[0].y - left[1].y) < 0.020:
            pyautogui.click()
        # if (landmarks[477].y - landmarks[475].y) < 0.034:
        #     pyautogui.rightClick()
    if keyboard.is_pressed("q"):
        break
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)