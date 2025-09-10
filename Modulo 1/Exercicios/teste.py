import pyautogui

for i in range(2):
    pyautogui.moveTo(100+10*i, 100+10*i, duration=60)
    pyautogui.moveTo(200+10*i, 100+10*i, duration=60)
    pyautogui.moveTo(200+10*i, 200+10*i, duration=60)
    pyautogui.moveTo(100+10*i, 200+10*i, duration=60)