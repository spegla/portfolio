import pyautogui
#import pydirectinput
import webbrowser   
import time, sys, random



for all in range(0,5):
    
    #pydirectinput.moveTo(100, 150)
    #pyautogui.mouseDown(1000,735)
    #pyautogui.click(x=1008, y=742)
    time.sleep(1)
    ######## finish crafted item #############
    #finish crafted item
    for PickupCraft in range(0,10):
        pyautogui.click(x=1008, y=742)
        time.sleep(1)
        #Collect click if have
        pyautogui.click(478,636)
        #new stuff confirmation
        pyautogui.click(x=580,y=786)
        #time.sleep(1)
    ##########################################    

    ######## sell & surcharge item #############
    #seller first contact
    #pyautogui.click(x=698,y=235)
    pyautogui.click(x=674,y=201)
    time.sleep(1)
    for sell in range(0,7):
        #small talk
        pyautogui.click(x=359,y=506)
        #suggest
        pyautogui.click(x=405,y=443)
        time.sleep(1)
        #surcharge
        pyautogui.click(x=782,y=520)
        time.sleep(1)
        #sell/buy
        pyautogui.click(x=760,y=570)
        #
        
        #time.sleep(1)
    ##########################################
    #Random & if statement
    RandomCraft.random(1,1,10)
    if RandomCraft = 
    ######## Craft new item  #############
    for craft in range(0,5):
        # craft 
        #odaberem craft
        pyautogui.click(x=1076,y=738)
        time.sleep(1)
        #odaberem bow
        pyautogui.click(x=236,y=805)
        time.sleep(1)
        #5 time click for crafting
        pyautogui.click(x=434,y=682)
        
    ##########################################
    #blanko
    pyautogui.click(x=871,y=550)
    time.sleep(70)
    
