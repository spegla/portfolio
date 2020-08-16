import pyautogui
import webbrowser   
import time, sys, random

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

time.sleep(3)

#pyautogui.size()
#FULL SCREEN

#exit undock from space station
Undock_from_station = [1020,272]
pyautogui.moveTo(Undock_from_station[0],Undock_from_station[1],1)
pyautogui.click()
time.sleep(random.randint(15,20))
#select mining TAB
select_mining_tab = [953,160]
pyautogui.moveTo(select_mining_tab[0],select_mining_tab[1],1)
pyautogui.click()
time.sleep(0.5)
#go to mining  post
select_mining_belt = [971,223]
select_minigbelt_worpto0 = [964,230]
pyautogui.doubleClick(select_mining_belt[0],select_mining_belt[1],1)
pyautogui.keyDown('s')
time.sleep(0.25)
pyautogui.keyUp('s')
time.sleep(35)
# pyautogui.rightClick(select_mining_belt[0],select_mining_belt[1],1)
# pyautogui.moveTo(select_minigbelt_worpto0[0],select_minigbelt_worpto0[1],1)
# pyautogui.click()

#mining asteroid belt
minig_asteroid1 = [966,242]
minig_asteroid2 = [966,262]
minig_asteroid3 = [966,282]
start_shield_hardener = [772,766]
start_afterburner = [824,763]
lock_target = [1023,83]

#get drones out
pyautogui.keyDown('altleft')
pyautogui.press('F2')
pyautogui.keyUp('altleft') 
time.sleep(0.5)
pyautogui.keyDown('altleft')
pyautogui.press('F3')
pyautogui.keyUp('altleft') 
time.sleep(0.5)
#MINING FIRST ASTEROID
pyautogui.moveTo(minig_asteroid1[0],minig_asteroid1[1],2)
pyautogui.doubleClick()
time.sleep(0.5)
pyautogui.keyDown('w')
time.sleep(0.2)
pyautogui.keyUp('w')
time.sleep(random.randint(15,20))
pyautogui.leftClick(lock_target[0],lock_target[1],2)
time.sleep(0.5)
pyautogui.keyDown('F1')
time.sleep(0.2)
pyautogui.keyUp('F1')
time.sleep(0.5)
pyautogui.keyDown('F2')
time.sleep(0.2)
pyautogui.keyUp('F2')
#MINING SECOUND ASTEROID
# pyautogui.leftClick(minig_asteroid2[0],minig_asteroid2[1],2)
# time.sleep(3)
# pyautogui.moveTo(lock_target[0],lock_target[1],2)
# time.sleep(1)
# time.sleep(random.randint(15,20))
# pyautogui.hotkey('F2')
#this is a time to full fill cargo 5000m3
#time.sleep(2479)
#get drones out
pyautogui.keyDown('shiftleft')
pyautogui.press('f')
pyautogui.keyUp('shiftleft') 

#time to wait to full fill cargo
time.sleep(70)
#GO HOME
    #drow back your drones
pyautogui.keyDown('shiftleft')
pyautogui.press('r')
pyautogui.keyUp('shiftleft') 
time.sleep(1)
    #Dock to station
pyautogui.moveTo(230,294,0.5)
pyautogui.rightClick()
pyautogui.moveTo(259,304,0.5)
pyautogui.click()


#Moving ORE TO HANGAR 
time.sleep(random.randint(15,20))
Ore_Hold_position = [470,651]
pyautogui.moveTo(Ore_Hold_position,0.5)
pyautogui.rightClick()
Ore_Select_All = [507,622]
pyautogui.click(ore_select_all,0.5)
ORE_move = [264,597]
pyautogui.moveTo(ORE_move,0.5)
ORE_DragTo = [100,702]
pyautogui.dragTo(ORE_DragTo,1.5,button='left')