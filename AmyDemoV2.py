import cv2
from gaze_tracking import GazeTracking
import time
import threading
import os
import pyautogui

def eye_tracking_and_presentation():
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

    cv2.destroyAllWindows()  # Close the OpenCV window after the loop ends

    print("Total time spent looking left:", total_left_time)
    print("Total time spent looking right:", total_right_time)


def open_powerpoint(file_path):
    os.startfile(file_path)
    time.sleep(2)  # Wait for PowerPoint to open

    # Maximize PowerPoint window (Windows shortcut: Alt + Space, then press x)
    pyautogui.hotkey('alt', 'space')
    pyautogui.press('x')
    time.sleep(2)  # Wait for window to maximize

    # Play presentation (F5)
    pyautogui.hotkey('f5')
    time.sleep(2)  # Wait for presentation to start

    # Wait for presentation to finish (you can adjust this time based on your presentation)
    slides_count = 0
    while slides_count < 6:  # Assuming there are 10 slides, adjust this according to your presentation
        time.sleep(3)  # Assuming each slide lasts for 5 seconds, adjust this as needed
        pyautogui.press('right')  # Navigate to the next slide
        slides_count += 1

    # Close PowerPoint presentation (Alt + F4)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)  # Wait for PowerPoint to close

if __name__ == "__main__":
    powerpoint_file = r"c:\Amy\TestCase.pptx"  # Change this to the path of your PowerPoint file

    # Create a thread for running eye tracking and presentation concurrently
    eye_tracking_thread = threading.Thread(target=eye_tracking_and_presentation)
    PPT_thread = threading.Thread(target=open_powerpoint, args=(powerpoint_file,))

    # Start the eye tracking and presentation thread
    eye_tracking_thread.start()
    PPT_thread.start()

    # Wait for the eye tracking thread to finish
    eye_tracking_thread.join()

    cv2.destroyAllWindows()
