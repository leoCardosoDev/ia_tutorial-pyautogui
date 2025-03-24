import pyautogui

pyautogui.moveTo(100,100, duration=1)
pyautogui.moveTo(200,200, duration=2)
pyautogui.moveTo(240,310, duration=3)

pyautogui.click(240, 310)

pyautogui.write('Hello World!', interval=0.25)
pyautogui.press('enter')