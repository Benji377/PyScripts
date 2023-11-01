import pyautogui

try:
    while True:
        # Get the current mouse coordinates
        x, y = pyautogui.position()
        print(f'Mouse coordinates: X={x}, Y={y}', end='\r')
except KeyboardInterrupt:
    print('\nScript terminated.')
