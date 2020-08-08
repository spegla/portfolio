import pyautogui
#import pydirectinput
import webbrowser   
import time, sys, random

DELAY_BETWEEN_COMMANDS = 0.5


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True
time.sleep(2)

#pytautogui.press('space')
StartQuest = [1080,810]
PureGoldBar = [57,736]
ExplorerArea = [773,584]
CollectLootGold = [1006,821]
SkipLoot = [1086,837] 
DismisALL = [481,539] 
CollectLoot = [500,656]
GuildEventReward = [1124,58]


for donerequest in range (0,3):
    pyautogui.click(CollectLootGold)
    time.sleep(5)
    pyautogui.click(SkipLoot)
    time.sleep(10)
    pyautogui.click(DismisALL)
    time.sleep(5)
    pyautogui.click(CollectLoot)
    time.sleep(5)
    pyautogui.click(GuildEventReward)
    time.sleep(1)

for repeat in range(0,20):
    pyautogui.click(StartQuest)
    time.sleep(1)
    pyautogui.click(PureGoldBar)
    time.sleep(1)
    pyautogui.click(ExplorerArea)
    #time.sleep(7200) 
    
    pyautogui.click(x=1010,y=225)
    x=11
    for countime in range(0,10):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        y = x-1
        print(y,"-","Countdown:", result)
        time.sleep(1080)
        x= y
    
    #3600 jedan sat
