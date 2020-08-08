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

for repeat inrange(0,20):
    pyautogui.click(StartQuest)
    time.sleep(1)
    pyautogui.click(PureGoldBar)
    time.sleep(1)
    pyautogui.click(ExplorerArea)
    time.sleep(7200)
    
    tratatata da li ce izmena da se vidi
