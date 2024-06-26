"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from datetime import time
import time
from ppt import PPTPlay



# Function to minimize the window
def minimize_window(window_name):
    # Check if using Windows OS
    if cv2.__version__.startswith('4') and hasattr(cv2, 'window'):
        cv2.namedWindow(window_name)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        # For Linux or macOS
        cv2.resizeWindow(window_name, 1, 1)
        cv2.moveWindow(window_name, -1920, -1080)


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

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    #minimize_window("Demo")

    #pptx_file = "c:\Amy\TestCase.pptx"  # Replace with your PowerPoint file path
    #ppt_player = PPTPlay(pptx_file)
    #ppt_player.start()
    #time.sleep(10)
    #ppt_player.stop()

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
print("Total time spent looking left:", total_left_time)
print("Total time spent looking right:", total_right_time)
