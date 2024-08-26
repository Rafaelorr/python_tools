from pyautogui import click
from time import sleep
clicks = int(input('hoeveel clicks wil je ? '))
print('druk ctrl + c om de loop te stopen')
sleep(0.8)
for i in range(clicks):
    click()
    sleep(0.1)
