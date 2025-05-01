"""
Title: Get Pointer Coordinates
Description: Prints your cursor screen coordinates in real-time
Author: Benji377
Created: 01.11.2023
Last Updated: 01.11.2023

Usage:
    No parameters

Dependencies:
    - pyautogui
    (Install with: pip install pyautogui)

Notes:
    - This script is standalone and does not require other files from the repo.
    - Adjust any parameters or constants at the top of the script as needed.
"""


import pyautogui

try:
    while True:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        print(f'Mouse coordinates: X={x}, Y={y}', end='\r')
except KeyboardInterrupt:
    print('\nScript terminated.')
