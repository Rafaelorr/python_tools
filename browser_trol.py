from webbrowser import open
from random import randint
from time import sleep

while True:
  sleep(4000)
  if randint(1,999999999999999999999999999999999999) < 2:
    open(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",new=0)
    sleep(200)
  sleep(200)
