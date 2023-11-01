import numpy as np
import time
import keyboard
import mss

# GAME: https://tbot.xyz/lumber/
# Tested in Splitscreen view side by side

# Define the initial side of the lumberjack and the screen capture region
monitor_left = {"top": 505, "left": 1360, "width": 5, "height": 15}
monitor_right = {"top": 505, "left": 1510, "width": 5, "height": 15}
monitor_death = {"top": 450, "left": 1430, "width": 1, "height": 1}
monitor_lumberjack = {"top": 620, "left": 1364, "width": 10, "height": 10}

LUMBERJACK_COLOR = np.array([61, 104, 148])
BRANCH_COLOR = np.array([161, 116, 56])


# Main automation loop
with mss.mss() as sct:
    # Prepare screen
    time.sleep(5)
    try:
        while sct.grab(monitor_death).pixel(0, 0) != (199, 240, 249):
            # Capture the screen
            lumberjack = sct.grab(monitor_lumberjack)

            # Convert the captured screenshot to a NumPy array
            lumb_img = np.array(lumberjack.pixels)

            if np.any(lumb_img == LUMBERJACK_COLOR):
                # Lumberjack is on the left side
                screen = sct.grab(monitor_left)
                if np.any(np.array(screen.pixels) == BRANCH_COLOR):
                    keyboard.press_and_release('right')  # Press and release the right arrow key
                else:
                    keyboard.press_and_release('left')  # Press and release the left arrow key
            else:
                # Lumberjack is on the right side
                screen = sct.grab(monitor_right)
                if np.any(np.array(screen.pixels) == BRANCH_COLOR):
                    keyboard.press_and_release('left')  # Press and release the left arrow key
                else:
                    keyboard.press_and_release('right')  # Press and release the right arrow key

            time.sleep(0.112)

    except KeyboardInterrupt:
        print("Script interrupted")
