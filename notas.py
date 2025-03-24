import pyautogui
import time

time.sleep(5)

pyautogui.hotkey('command', 'space')
pyautogui.write('Editor de Texto')
pyautogui.press('enter')

time.sleep(3)

pyautogui.typewrite('Este é um exemplo de automação de notas com Python e PyAutoGUI.', interval=0.1)