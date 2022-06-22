
import cv2
from gaze_tracking import GazeTracking
from datetime import time
import time
from ppt import PPTPlay

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
start_time = time.time()
total_left_time = 0
total_right_time = 0
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
        total_right_time += time.time() - start_time
    elif gaze.is_left():
        text = "Looking left"
        total_left_time += time.time() - start_time
    elif gaze.is_center():
        text = "Looking center"
    start_time = time.time()

    cv2.putText(frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
print("Total time spent looking left:", total_left_time)
print("Total time spent looking right:", total_right_time)
