# Creates the dices for the game

import random

# Method for the dice

def dicesII():
   firstDice = random.randint(1, 6)
   secondDice = random.randint(1, 6)
   DualDice = firstDice + secondDice
   print("You rolled ", firstDice, " and ", secondDice, " which is ", DualDice)
   print("")
   return DualDice

dicesII()


