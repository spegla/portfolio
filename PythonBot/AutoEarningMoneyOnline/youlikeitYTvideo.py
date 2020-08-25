import pyautogui
import sys,time,random

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True
pyautogui.FAILSAFE = True

for i in range(1,100000):
    #menu
    MainTAb = [140,12]
    SecoundTAB = [340,12]
    SecoundTABClose = [470,22]
    
    
    time.sleep(1)
    pyautogui.moveTo(MainTAb[0],MainTAb[1],1)
    pyautogui.click()

    pyautogui.moveTo(295,187,1) # Go to Menu Earn Points
    pyautogui.moveTo(291,340,1) # Go to Youtube
    pyautogui.moveTo(448,342,1) # Go to Youtube Views
    pyautogui.click()
    time.sleep(3)
    
    pyautogui.moveTo(574,557,0.5) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(574,571,0.5) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(574,550,0.5) # click on visit sometimes move down or up
    pyautogui.click()
    #time.sleep(170)
    
    x=17
    for countime in range(0,x):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        y = x-1
        print(y,"-","Countdown:", result)
        time.sleep(10)
        x= y
