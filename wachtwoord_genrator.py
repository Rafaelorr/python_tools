from random import randint,choice
from string import ascii_uppercase

def sterk_wachwoord():
  wachtwoord = ''
  wachtwoord_items = []
  wachtwoord_items.append(choice(['snelle']))
  wachtwoord_items.append(choice(['blauwe']))
  wachtwoord_items.append(choice(['panda']))

  for i in range(randint(1,4)):
    wachtwoord_items.append(choice(ascii_uppercase))

  wachtwoord_items.append(str(randint(1,99999)))

  for wachtwoord_item in wachtwoord_items:
    wachtwoord += str(wachtwoord_item)
  return wachtwoord

print(sterk_wachwoord())