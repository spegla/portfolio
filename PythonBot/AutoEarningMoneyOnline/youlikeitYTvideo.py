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
    time.sleep(1)
    
    pyautogui.moveTo(215,460,0.2) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(215,477,0.2) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(215,493,0.2) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(212,519,0.2) # click on visit sometimes move down or up
    pyautogui.click()
    pyautogui.moveTo(207,514,0.2) # click on visit sometimes move down or up
    pyautogui.click()
    
    time.sleep(21)
    
    pyautogui.moveTo(SecoundTABClose[0],SecoundTABClose[1],1) # closing secound TAB
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(680,173) # closing button Leave when close secound tab
    pyautogui.click()
    time.sleep(0.5)
    
