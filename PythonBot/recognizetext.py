import webbrowser
import pyautogui
import sys
import time
#/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png

print('press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
    

#pyautogui.locateOnScreen('googlelogo_color_272x92dp.png', region=(0,0, 300, 400))