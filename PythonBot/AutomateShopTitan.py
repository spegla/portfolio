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
for CeoCiklusOd250Minuta in range(0,150):
    #time.sleep(1)
    Reconnect = [574,502]
    ClickToStartSell = [694,166]
    ClickToSmallTalk = [373,521]
    ClickToSuggest = [414,462]
    ClickToSell = [764,586]
    
    PickupCraft = [1010,766]
    PickupConfirmCollect = [484,656]
    BluePrintConfirm = [570,819]
    
    #Ovde mozemo da zamenimo sa button space
    # CliclToStartCraft = [1078,754]
    Weapon  = [965,837]
    Armor = [1018,841]
    Potion = [1073,839]
    
    
    WeaponKnife = [113,834]
    WeaponKnifeIcePick = [681,709]
    WeaponKnifeSwiftBlade = [551,709]
    WeaponKnifeStealthKnife = [420,709]
    WeaponKnifeBalisong = [290,709]
    
    WeaponBow = [237,836]
    WeaponBowWlmwood =[550,730]
    WeaponBowReflexBow = [430,730]
    WeaponBowCompoundBow = [300,730]
    
    ArmorMetal = [30,830]
    ArmorMetalBreatPlate = [550,750]
    ArmorMetalIronMail = [430,750]
    ArmorMetalScaleArmor = [310,750]
    
        
    ##############START POSITION##################
    for a in range(0,3):
    
        for i in range(0,3):
            pyautogui.moveTo(1000,45, duration = 0.1)
            pyautogui.dragRel(-785,-719, duration = 0.5)

        pyautogui.moveTo(785, 719, duration = 0.2)
        pyautogui.dragRel(0,-360, duration = 1)
        pyautogui.dragRel(334,0, duration = 1)
    ##############START POSITION##################
    
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
        time.sleep(.2)
        pyautogui.click(ClickToSmallTalk)
        time.sleep(.2)
        pyautogui.click(ClickToSuggest)
        time.sleep(.2)
        pyautogui.click(ClickToSell)
        time.sleep(.2)
        #pyautogui.click(x=1096,y=450)
        
    ######## crafting #############
    pyautogui.click(x=1096,y=450)
    RandomCraftType = random.randint(1,3)
    RandomCraftWeapon = random.randint(1,3)
    if RandomCraftType == 2:
        ######## Craft new item Bow #############
        #pyautogui.click(CliclToStartCraft)
        pyautogui.press('space')
        for WCraft in range(0,6):
            if RandomCraftWeapon == 2:
                #for craftweapon in range(0,5):
                    pyautogui.click(Weapon)
                    pyautogui.click(WeaponBow)
                    pyautogui.click(WeaponBowWlmwood)
            elif RandomCraftWeapon >2:
                #for craftweapon in range(0,5):
                    pyautogui.click(Weapon)
                    pyautogui.click(WeaponBow)
                    pyautogui.click(WeaponBowReflexBow)
            #pyautogui.click(CliclToStartCraft)
            else:
                pyautogui.click(Weapon)
                pyautogui.click(WeaponBow)
                pyautogui.click(WeaponBowCompoundBow)
        ##########################################
    elif RandomCraftType > 2:
        ######## Craft new item Knifes #############
        #pyautogui.click(CliclToStartCraft)
        pyautogui.press('space')
        
        for WCraft in range(0,6):
            if RandomCraftWeapon == 2:
                #for craftweapon in range(0,6):
                    pyautogui.click(Weapon)
                    pyautogui.click(WeaponKnife)
                    pyautogui.click(WeaponKnifeIcePick)
            elif RandomCraftWeapon >2:
                #for craftweapon in range(0,6):
                    pyautogui.click(Weapon)
                    pyautogui.click(WeaponKnife)
                    pyautogui.click(WeaponKnifeSwiftBlade)
            #pyautogui.click(CliclToStartCraft)
            else:
                pyautogui.click(Weapon)
                pyautogui.click(WeaponKnife)
                pyautogui.click(WeaponKnifeStealthKnife)
        ##########################################
    else:
        ######## Craft new item swords  #############
        #pyautogui.click(CliclToStartCraft)
        pyautogui.press('space')
        for WCraft in range(0,6):
            if RandomCraftWeapon == 2:
                #for craftweapon in range(0,5):
                    pyautogui.click(Armor)
                    pyautogui.click(ArmorMetal)
                    pyautogui.click(ArmorMetalBreatPlate)
            elif RandomCraftWeapon >2:
                #for craftweapon in range(0,5):
                    pyautogui.click(Armor)
                    pyautogui.click(ArmorMetal)
                    pyautogui.click(ArmorMetalIronMail)
            #pyautogui.click(CliclToStartCraft)
            else:
                pyautogui.click(Armor)
                pyautogui.click(ArmorMetal)
                pyautogui.click(ArmorMetalScaleArmor)
        ##########################################    
    
    pyautogui.click(x=1096,y=450)
    #time.sleep(420)
    x=11
    for countime in range(0,10):
    #while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        y = x-1
        print(y,"-","Countdown:", result)
        time.sleep(44)
        x= y
    
    


