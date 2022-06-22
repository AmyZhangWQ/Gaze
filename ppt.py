import pyautogui
import os
import time
import psutil

class PPTPlay:
    def __init__(self, pptx_file):
        self.pptx_file = pptx_file
        self.powerpoint_process = None

    def open_powerpoint(self):
        os.startfile(self.pptx_file)
        time.sleep(2)  # Wait for PowerPoint to open

    def close_ppt_window(self):
        pyautogui.hotkey('alt', 'f4')  # Simulate Alt + F4 to close PowerPoint window
        time.sleep(2)  # Wait for window to close

    def get_powerpoint_process(self):
        for proc in psutil.process_iter():
            if "POWERPNT.EXE" in proc.name():
                self.powerpoint_process = proc
                break

    def close_powerpoint(self):
        if self.powerpoint_process:
            self.powerpoint_process.terminate()
            self.powerpoint_process = None

    def play_presentation(self):
        # Press F5 to start slideshow
        pyautogui.press('f5')
        time.sleep(2)  # Wait for slideshow to start

        # Press the right arrow key to advance slides
        while True:
            pyautogui.press('right')
            time.sleep(2)  # Adjust this time according to your presentation speed

    def start(self):
        self.open_powerpoint()
        self.play_presentation()

    def stop(self):
        self.close_ppt_window()
        self.get_powerpoint_process()
        self.close_powerpoint()

