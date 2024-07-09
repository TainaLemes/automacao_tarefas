import pyautogui

pyautogui.click(200,200,interval=0.5)
pyautogui.press('space')

while True:        
    print(pyautogui.pixel(232,460))
    if pyautogui.pixelMatchesColor(232,460,[83,83,83],70):
        pyautogui.press('space')

    elif pyautogui.pixelMatchesColor(232,92,[83,83,83],70):
        print(pyautogui.pixel(232,92))
        print(pyautogui.press)
        pyautogui.press('down')                       