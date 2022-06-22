import os
import pyautogui
import time

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
    while slides_count < 8:  # Assuming there are 10 slides, adjust this according to your presentation
        time.sleep(5)  # Assuming each slide lasts for 5 seconds, adjust this as needed
        pyautogui.press('right')  # Navigate to the next slide
        slides_count += 1

    # Close PowerPoint presentation (Alt + F4)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)  # Wait for PowerPoint to close


