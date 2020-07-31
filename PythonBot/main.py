import pyautogui
import time

def main():
    # initalized PyAutoGUI
   pyautogui.FAILSAFE = True
    
    #Countdown timer
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("go")
    
    # Do anything
    pyautogui.keyDown('2')   
    time.sleep(2)
    pyautogui.keyDown('2')
        
    
    
if __name__ == __main__:
    main()