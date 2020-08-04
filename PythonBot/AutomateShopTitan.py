import pyautogui
#import pydirectinput
import webbrowser   
import time, sys, random

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True
time.sleep(1)
for CeoCiklusOd250Minuta in range(0,20):
    #time.sleep(1)
    ClickToStartSell = [687,136]
    ClickToSmallTalk = [373,521]
    ClickToSuggest = [414,462]
    ClickToSell = [764,586]
    
    PickupCraft = [1010,766]
    PickupConfirmCollect = [484,656]
    BluePrintConfirm = [570,819]
    Reconnect = [574,502]
    
    CliclToStartCraft = [1078,754]
    Weapon  = [965,837]
    Armor = [1018,841]
    Potion = [1073,839]
    WeaponKnife = [113,834]
    
    WeaponKnifeIcePick = [687,732]
    WeaponKnifeSwiftBlade = [557,709]
    WeaponBow = [237,836]
    WeaponBowWlmwood =[447,736]
    
    ######## finish crafted item  #############
    pyautogui.click(Reconnect)
    for PickupCr in range(0,10):
        pyautogui.click(PickupCraft)
        pyautogui.click(PickupConfirmCollect)
        pyautogui.click(BluePrintConfirm)
        time.sleep(.15)
    ##########################################
    ######## sell & surcharge item #############
    for selling in range(0,10):
        pyautogui.click(ClickToStartSell)
        time.sleep(.15)
        pyautogui.click(ClickToSmallTalk)
        time.sleep(.15)
        pyautogui.click(ClickToSuggest)
        time.sleep(.15)
        pyautogui.click(ClickToSell)
        time.sleep(.15)
    # ######## crafting #############
    # RandomCraft = random.randint(1,3)
    
    # if RandomCraft == 2:
    #     ######## Craft new item Bow #############
    #     pyautogui.click(CliclToStartCraft)
    #     for BowCraft in range(0,5):
    #         #pyautogui.click(CliclToStartCraft)
    #         pyautogui.click(Weapon)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponBow)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponBowWlmwood)
    #         time.sleep(0.2)
    #     ##########################################
    # elif RandomCraft > 2:
    #     ######## Craft new item Knifes #############
    #     pyautogui.click(CliclToStartCraft)
    #     for KnifeCraft in range(0,5):
    #         #pyautogui.click(CliclToStartCraft)
    #         pyautogui.click(Weapon)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponKnife)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponKnifeIcePick)
    #         time.sleep(0.2)
    #     ##########################################
    # else:
    #     ######## Craft new item swords  #############
    #     pyautogui.click(CliclToStartCraft)
    #     for KnifeCraft in range(0,5):
    #         #pyautogui.click(CliclToStartCraft)
    #         pyautogui.click(Weapon)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponKnife)
    #         time.sleep(0.2)
    #         pyautogui.click(WeaponKnifeSwiftBlade)
    #         time.sleep(0.2)
    #     ##########################################    
    
    #pyautogui.click(x=871,y=400)
    time.sleep(100)
