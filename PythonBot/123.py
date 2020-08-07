import pyautogui 
import time
from time import sleep

pyautogui.FAILSAFE = True
#pyautogui.FAILSAFE = False

time.sleep(1)
#pyautogui.moveTo(785, 719, duration = 0.2)
for a in range(0,3):
    
    for i in range(0,3):
        pyautogui.moveTo(1000,45, duration = 0.1)
        pyautogui.dragRel(-785,-719, duration = 0.5)

    pyautogui.moveTo(785, 719, duration = 0.2)
    pyautogui.dragRel(0,-360, duration = 1)
    pyautogui.dragRel(334,0, duration = 1)
#pyautogui.dragRel(-100, 0, duration = 1) 
#pyautogui.dragRel(0, -100, duration = 1) 
#pyautogui.dragRel(100, 0, duration = 1)
#print(pyautogui.size()) 

