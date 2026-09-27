from platform import python_branch
import pyautogui, webbrowser
from time import sleep
webbrowser.open('https://web.whatsapp.com/send?phone=+codigonumerotelefonico')
sleep(60)
with open('mensaje.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
