import pyautogui
import webbrowser   
import time, sys, random
pyautogui.FAILSAFE = True

time.sleep(3)
#get drones out

# pyautogui.hotkey('shift', 'f')
# pyautogui.hotkey('alt', 'F2')
# pyautogui.hotkey('alt', 'F3')
# time.sleep(1)
# pyautogui.hotkey('shift', 'r')
# pyautogui.keyDown('shiftleft')
# pyautogui.press('f')
# time.sleep(0.5)


pyautogui.keyDown('shiftleft')
pyautogui.press('f')
pyautogui.keyUp('shiftleft') 
time.sleep(0.5)
pyautogui.keyDown('altleft')
pyautogui.press('F2')
pyautogui.keyUp('altleft') 
time.sleep(0.5)
pyautogui.keyDown('altleft')
pyautogui.press('F3')
pyautogui.keyUp('altleft') 
time.sleep(0.5)
pyautogui.keyDown('shiftleft')
pyautogui.press('r')
pyautogui.keyUp('shiftleft') 
time.sleep(0.5)




