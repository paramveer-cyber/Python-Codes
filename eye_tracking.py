import cv2
import pyautogui
import keyboard
import mediapipe

cam = cv2.VideoCapture(0)
face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = (1920, 1080)
while True:
    pyautogui.FAILSAFE = False
    filler, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            val_x = int(landmark.x * frame_width)
            val_y = int(landmark.y * frame_height)
            cv2.circle(frame, (val_x, val_y), 3, (255, 0, 0))
            if id == 1:
                display_x = screen_w * landmark.x * 1.2
                display_y = screen_h * landmark.y * 1.5
                pyautogui.moveTo(display_x, display_y) 
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            val_x = int(landmark.x * frame_width)
            val_y = int(landmark.y * frame_height)
            cv2.circle(frame, (val_x, val_y), 3, (0, 100, 100))
            # print(landmarks[477].y - landmarks[475].y)
        if (left[0].y - left[1].y) < 0.020: #variable dist
            pyautogui.click()
        # if (landmarks[477].y - landmarks[475].y) < 0.034:
        #     pyautogui.rightClick()*
    if keyboard.is_pressed("q"):
        break
    cv2.imshow('Eye Tracker', frame)
    cv2.waitKey(1)