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
    MainTAb = [497,16]
    SecoundTAB = [632,14]
    SecoundTABClose = [727,15]

    time.sleep(2)
    pyautogui.moveTo(MainTAb[0],MainTAb[1],1)
    pyautogui.click()

    pyautogui.moveTo(294,169,1) #Mainmenu Earn money
    pyautogui.moveTo(291,557,1) #click to web site hits 
    pyautogui.moveTo(278,588,1) #click to website hits when one more have
    pyautogui.moveTo(564,717,1) #click here to loadd more
    time.sleep(1)
    
    pyautogui.moveTo(216,470,1)
    pyautogui.click()
    pyautogui.moveTo(211,485,1)
    pyautogui.click()
    pyautogui.moveTo(211,510,1)
    pyautogui.click()
    time.sleep(21)
    Visit = [210,486]
    pyautogui.moveTo(Visit[0],Visit[1],1)
    pyautogui.click()
    time.sleep(22)
    pyautogui.moveTo(SecoundTABClose[0],SecoundTABClose[1],0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(669,163,1)
    pyautogui.click()
