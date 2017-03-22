#! python3
# mouseNow.py - displays the mouse cursor's current position

import pyautogui
import time

print('press ctrl+C to quit')


while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)      #'\b'打印退格，需要配合flush=True使用。但问题是，由于退格太快，导致无法看到上一行print的内容。待解决。
