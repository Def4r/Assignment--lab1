# Creates the dices for the game

import random

# Method for the dice

def dices():
   firstDice = random.randint(1, 6)
   secondDice = random.randint(1, 6)
   DualDice = firstDice + secondDice
   print("You rolled ", firstDice, " and ", secondDice, " which is ", DualDice)
   return DualDice

dices()


