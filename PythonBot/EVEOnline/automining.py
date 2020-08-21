import pyautogui
import webbrowser   
import time, sys, random

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

for i in range(0,10000):
    time.sleep(2)

    #pyautogui.size()
    #FULL SCREEN

    #exit undock from space station
    Undock_from_station = [1030,172]
    pyautogui.moveTo(Undock_from_station[0],Undock_from_station[1],1)
    pyautogui.click()
    time.sleep(random.randint(15,20))
    #select mining TAB
    select_mining_tab = [937,162]
    pyautogui.moveTo(select_mining_tab[0],select_mining_tab[1],1)
    pyautogui.click()
    time.sleep(0.5)
    #go to mining  post
    select_mining_belt = [941,243]
    select_minigbelt_worpto0 = [964,230]
    pyautogui.doubleClick(select_mining_belt[0],select_mining_belt[1],1)
    pyautogui.keyDown('s')
    time.sleep(0.25)
    pyautogui.keyUp('s')
    time.sleep(35)
    # pyautogui.rightClick(select_mining_belt[0],select_mining_belt[1],1)
    # pyautogui.moveTo(select_minigbelt_worpto0[0],select_minigbelt_worpto0[1],1)
    # pyautogui.click()q
    select_mining_tab = [1068,162]
    pyautogui.moveTo(select_mining_tab[0],select_mining_tab[1],1)
    pyautogui.click()
    time.sleep(0.5)
    #mining asteroid belt
    minig_asteroid1 = [931,204]
    minig_asteroid2 = [931,224]
    minig_asteroid3 = [931,244]
    #start_shield_hardener = [772,766]
    #start_afterburner = [824,763]
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
    time.sleep(random.randint(20,25))
    pyautogui.moveTo(lock_target[0],lock_target[1],2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('F1')
    time.sleep(0.2)
    pyautogui.keyUp('F1')
    time.sleep(1)
    #MINING SECOUND ASTEROID
    pyautogui.moveTo(minig_asteroid2[0],minig_asteroid2[1],2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(lock_target[0],lock_target[1],2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(692,54,2)
    pyautogui.click()
    pyautogui.keyDown('F2')
    time.sleep(0.2)
    pyautogui.keyUp('F2')
    
    #deploy droness
    time.sleep(60)
    pyautogui.keyDown('shiftleft')
    pyautogui.press('f')
    pyautogui.keyUp('shiftleft') 

    #time to wait to full fill cargos
    time.sleep(130)
    #GO HOME
        #drow back your drones
    pyautogui.keyDown('shiftleft')
    pyautogui.press('r')
    pyautogui.keyUp('shiftleft') 
    time.sleep(3)
    pyautogui.keyDown('shiftleft')
    pyautogui.press('r')
    pyautogui.keyUp('shiftleft') 
    time.sleep(5)
    
        #Dock to station
    pyautogui.moveTo(211,363,1)
    pyautogui.rightClick()
    pyautogui.moveTo(240,373,1)
    pyautogui.click()
    pyautogui.keyDown('F1')
    time.sleep(0.2)
    pyautogui.keyUp('F1')
    time.sleep(0.5)
    pyautogui.keyDown('F2')
    time.sleep(0.2)
    pyautogui.keyUp('F2')
    time.sleep(random.randint(45,60))

        #Moving ORE TO HANGAR 
    pyautogui.moveTo(108,604,1) #select ship ore hangar
    pyautogui.click()
    pyautogui.moveTo(377,579,1) #rightclick in ore ship hangar
    pyautogui.rightClick()
    pyautogui.moveTo(406,588,1) #sellect all
    pyautogui.click()
    pyautogui.moveTo(264,597,1)
    pyautogui.dragTo(100,702,1,button='left')
