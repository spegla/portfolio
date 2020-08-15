import pyautogui
import webbrowser   
import time, sys, random
pyautogui.FAILSAFE = True

time.sleep(3)
#get drones out
#pyautogui.hotkey('Shift', 'f')
#pyautogui.hotkey('Alt', 'F2')
#pyautogui.hotkey('Alt', 'F3')
pyautogui.keyDown('shiftleft')
pyautogui.press('f')
time.sleep(0.5)

pyautogui.keyDown('altleft')
pyautogui.press('F2')
time.sleep(0.5)
pyautogui.keyDown('altleft')
pyautogui.press('F3')
time.sleep(0.5)
pyautogui.keyDown('shiftleft')
pyautogui.press('r')
time.sleep(0.5)