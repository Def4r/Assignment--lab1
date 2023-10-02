# Creates the dices for the game

import random

# Methods for the dices

def diceI():
   onlyDice = random.randint(1,6)
   print("You rolled ", onlyDice)
   print("")
   return onlyDice

def dicesII():
   firstDice = random.randint(1, 6)
   secondDice = random.randint(1, 6)
   DualDice = firstDice + secondDice
   print("You rolled a ", firstDice, " and a ", secondDice, " which is ", DualDice)
   print("")
   return DualDice

def pickDice():
   dice_1 = random.randint(1,6)
   dice_2 = random.randint(1,6)
   FinalDice = int(input("You rolled a ", dice_1, " and a ", dice_2, "Type 1 to pick Dice 1 roll or Type 2 to pick Dice 2 roll: " ))
   if FinalDice == 1:
      print("You picked Dice 1 which rolled ", dice_1)
      return dice_1
   if FinalDice == 2:
      print("You picked Dice 2 which rolled ", dice_2)
      return dice_2

#diceI()
#dicesII()
pickDice()

