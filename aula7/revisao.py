import pyautogui 
import pyscreeze

#mover
#pyautogui.moveTo (1184, 1052, duration=.5)
#pyautogui.moveRel(-100, 0, duration=.5)
#pyautogui.moveRel(0, -100, duration=.5)

#arrastar
#pyautogui.moveTo(257, 100, duration=.5)
#pyautogui.dragTo(27, 19, duration=.5)
#pyautogui.dragRel(27, 19, duration=.5)

#clicar 
#pyautogui.click(57,17, duration=.5)
#pyautogui. click(554, 481, duration=.5, clicks=2)
##Localizar um item na tela 
btnxy = pyautogui.locateCenterOnScreen('./aula7/btn_edit.png')
pyautogui.click(btnxy, duration=.5)



#rolar bolinha 