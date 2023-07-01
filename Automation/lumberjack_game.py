import pyautogui
import time
import keyboard
import win32api, win32con

# This is a small script to automatically play the lumberjack game (https://tbot.xyz/lumber/)
# If you want to use this, you will need to set the coordinates accordingly.
# You can quit the program at any time using the 'Q' key

def click_right():
    win32api.keybd_event(0x27, 0,0,0)
    win32api.keybd_event(0x27, 0,win32con.KEYEVENTF_KEYUP, 0)

def click_left():
    win32api.keybd_event(0x25, 0,0,0)
    win32api.keybd_event(0x25, 0,win32con.KEYEVENTF_KEYUP, 0)

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(1509, 535)[0] == 51:
        # Lumberjack is on the right side
        if pyautogui.pixel(1509, 518)[0] == 211:
            # Space above is free
            click_right()
        else:
            # Space above is occupied
            click_left()
    elif pyautogui.pixel(1367, 518)[0] == 211:
        # Space above is free
        click_left()
    else:
        click_right()
    time.sleep(0.15)
