import pyautogui
#import pydirectinput
import webbrowser   
import time
import sys

#pydirectinput.moveTo(100, 150)
#pyautogui.mouseDown(1000,735)
#pyautogui.click(x=1008, y=742)
time.sleep(1)
######## finish crafted item #############
#finish crafted item
for PickupCraft in range(0,5):
    pyautogui.click(x=1008, y=742)
    time.sleep(1)
    #Collect clik if have
    pyautogui.click(478,636)
    #time.sleep(1)
##########################################    

######## sell & surcharge item #############
pyautogui.click(x=698,y=235)
for sell in range(0,5):
    pyautogui.click(x=782,y=520)
    #time.sleep(1)
    pyautogui.click(x=760,y=570)
    time.sleep(1)
##########################################
#pyautogui.click(x=1000, y=735)
Position = pyautogui.position()
print(Position)