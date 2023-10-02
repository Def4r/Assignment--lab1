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
   print("You rolled ", dice_1, " on Dice I")
   print("You rolled ", dice_2, " on Dice II") 
   print("")
   FinalDice = (input("Type 'I' or 'II' to pick the dice you want to use: "))
   
   if FinalDice == "I":
      print("You picked Dice I which rolled ", dice_1)
      return dice_1
   elif FinalDice == "I":
      print("You picked Dice I which rolled ", dice_2)
      return dice_2
   else:
      print("You didn't type 'I' or 'II'! We will randomly pick for you using a coinfilp")
      CoinFilp = random.randint(1,2)
      if CoinFilp == 1:
         print("We picked Dice I for you which is ", dice_1)
         return dice_1
      elif CoinFilp == 2:
         print("We picked Dice I for you whihc is ", dice_2)
         return dice_2





#diceI()
#dicesII()
pickDice()

