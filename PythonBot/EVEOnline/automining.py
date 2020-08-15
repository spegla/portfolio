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
Undock_from_station = [1020,272]
select_mining_tab = [953,160]
select_mining_belt = [971,223]
select_minigbelt_worpto0 = [964,230]
#exit undock from space station
pyautogui.moveTo(Undock_from_station[0],Undock_from_station[1],2)
pyautogui.click()
time.sleep(15)
#go to mining  post
pyautogui.rightClick(select_mining_belt[0],select_mining_belt[1],2)
pyautogui.moveTo(select_minigbelt_worpto0[0],select_minigbelt_worpto0[1],2)
pyautogui.click()
time.sleep(10)
#mining asteroid belt
minig_asteroid1 = [966,242]
minig_asteroid2 = [966,262]
minig_asteroid3 = [966,282]
start_shield_hardener = [772,766]
start_afterburner = [824,763]
lock_target = [1023,83]
#get drones out
pyautogui.hotkey('Shift', 'f')
pyautogui.hotkey('Alt', 'F2')
pyautogui.hotkey('Alt', 'F3')
#MINING FIRST ASTEROID
pyautogui.doubleClick(minig_asteroid1[0],minig_asteroid1[1],2)
time.sleep(3)
pyautogui.moveTo(lock_target[0],lock_target[1]2)
time.sleep(1)
pyautogui.hotkey('F1')
#MINING SECOUND ASTEROID
pyautogui.doubleClick(minig_asteroid2[0],minig_asteroid2[1],2)
time.sleep(3)
pyautogui.moveTo(lock_target[0],lock_target[1]2)
time.sleep(1)
pyautogui.hotkey('F2')

#this is a time to full fill cargo 5000m3
#time.sleep(2479)
time.sleep(60)
#GO HOME
    #drow back your drones
pyautogui.hotkey('Shift', 'r')
time.sleep(1)
    #Dock to station
pyautogui.rightkey(230,296)
pyautogui.moveTo(262,304,2)
pyautogui.click()


