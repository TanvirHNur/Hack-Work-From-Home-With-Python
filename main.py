# install pip install pyautogui

import pyautogui
import time
pyautogui.FAILSAFF = False
while True:
    time.sleep(200)
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 5)

       for i in range (0, 3):
           pyautogui.press('shift') t