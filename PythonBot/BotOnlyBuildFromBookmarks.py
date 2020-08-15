import pyautogui
import sys, time, random

DELAY_BETWEEN_COMMANDS = 0.5
pyautogui.FAILSAFE = True

time.sleep(2)
#definision coordinate
#zvezdica
star = [911,830]
BookmarkButton = [209,838]
SomewhereRight = [1039,353]
Collect = [998,775]
CollectafterCollect = [481,659] # collect after collect
StartPositionCrafting = [65,753]


pyautogui.click(SomewhereRight)

for Crafting in range(0,150):
    for collect in range(0,10):
        pyautogui.click(Collect)
        time.sleep(0.2)
        pyautogui.click(CollectafterCollect)
    for SomewhereRight in range(0,3):
        pyautogui.click(1039,353)
    pyautogui.press('space')
    RandomCraft = random.randint(1,6)
    pyautogui.click(star)        
    pyautogui.click(BookmarkButton)
    for craft in range(0,6):    
        if RandomCraft == 1:
            #pyautogui.click(star)        
            #pyautogui.click(BookmarkButton)
            pyautogui.click(StartPositionCrafting[0],StartPositionCrafting[1])
        elif RandomCraft ==2:
            #pyautogui.click(star)        
            #pyautogui.click(BookmarkButton)
            pyautogui.click(StartPositionCrafting[0]+120,StartPositionCrafting[1])
        elif RandomCraft ==3:
            #pyautogui.click(star)        
            #pyautogui.click(BookmarkButton)
            pyautogui.click(StartPositionCrafting[0]+240,StartPositionCrafting[1])
        else:
            #pyautogui.click(star)        
            #pyautogui.click(BookmarkButton)
            pyautogui.click(StartPositionCrafting[0]+360,StartPositionCrafting[1])
    for SomewhereRight in range(0,3):
        pyautogui.click(1039,353)
    x=30
    for countime in range(0,x):
    #while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        y = x-1
        print(y,"-","Countdown:", result)
        time.sleep(10)
        x=y