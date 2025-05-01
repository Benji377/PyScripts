"""
Title: Get Screen
Description: Creates a screenshot of a specified area
Author: Benji377
Created: 01.11.2023
Last Updated: 01.11.2023

Usage:
    No parameters

Dependencies:
    - cv2
    - mss
    - numpy
    (Install with: pip install cv2 mss numpy)

Notes:
    - This script is standalone and does not require other files from the repo.
    - Adjust any parameters or constants at the top of the script as needed.
"""


import cv2
import mss
import numpy as np


def display_screenshot(monitor):
    with mss.mss() as sct:
        # Capture the screen
        screenshot = sct.grab(monitor)

        # Convert the screenshot to a NumPy array
        img = np.array(screenshot)

        # Display the screenshot in a new window
        cv2.imshow("Screenshot", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


MONITOR_LEFT = {"top": 485, "left": 1300, "width": 100, "height": 40}
MONITOR_RIGHT = {"top": 485, "left": 1480, "width": 100, "height": 40}
MONITOR_DEATH = {"top": 450, "left": 1430, "width": 1, "height": 1}
MONITOR_LUMBERJACK = {"top": 610, "left": 1300, "width": 100, "height": 30}

display_screenshot(MONITOR_LEFT)
