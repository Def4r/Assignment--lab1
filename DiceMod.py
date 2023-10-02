# Creates the dices for the game

import random

# Methods for the dices

def diceI():
   onlyDice = random.randomint(1,6)
   print("You rolled ", onlyDice)
   print("")
   return onlyDice

def dicesII():
   firstDice = random.randint(1, 6)
   secondDice = random.randint(1, 6)
   DualDice = firstDice + secondDice
   print("You rolled ", firstDice, " and ", secondDice, " which is ", DualDice)
   print("")
   return DualDice

diceI()
dicesII()


