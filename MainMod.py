import time
import random
import sys
import CharacterMod 
from CharacterMod import Rouge
import DiceMod
from time import sleep
from sys import stdout

CharPick = 0
NewCharHP = 0

ErrorText = "ERROR :["

def main():
    return True

def Introduction():
    Title = "||Welcome to Dungeon Hunters||"
    for char in Title:
        sleep(0.07)
        stdout.write(char)
        stdout.flush()

    sleep(2)
    print("")

    ContinueGame = "Type 'START' to Play the game"
    for char in ContinueGame:
        sleep(0.04)
        stdout.write(char)
        stdout.flush()

    print("")
    ContinuePrompt = str(input(":>"))
    
    if ContinuePrompt.lower() == "start":
        print("")
        TextI = "The objective of the game is to make it out of the dungeon ALIVE. There will be 3 stages you will have to defeat in order to escape the dungeon. This game is dice based and will determine how the game will end up playing."
        for char in TextI:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(2)
        print("")
        TextII = "You will have to pick between a varity of characters. They all have different stats and attributes before you choose you character you will see a breif overview of them"
        for char in TextII:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        print("")
        RougeSum = "Rouge: Fast, aglie and has access to double dice which allows them to travel faster but can't take hits and will die easily"
        print("")
        sleep(1)
        KnightSum = ""
        print("")
        sleep(1)
        TankSum = ""
        print("")
        sleep(1)
        MageSum = ""
        print("")
        sleep(1)
        DifficultyChars = ""
        print("")
        sleep(2)

        TextIII = "Now the game will begin. Have Fun :]"
        for char in TextIII:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        print("")
        sleep(2)
        return "true"
    else:
        for char in ErrorText:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(2)
        exit()

def characterSection():
    if Introduction() == "true":
        TextIV = "Pick you character | Type ....."
        for char in TextIV:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        print("")
        PickChar = str(input(":>"))
        if PickChar.lower() == "Rouge":
            PickRougeText = ("You have picked |The Rouge|")
            CharPick == 1
        elif PickChar.lower() == "Knight":
            PickKnightText = ("You have picked |The Knight|")
            CharPick == 2
        elif PickChar.lower() == "Mage":
            PickMageText = ("You picked |The Mage|")
            CharPick == 3
        elif PickChar.lower() == "Tank":
            PickTankText = ("You picked |The Tank|")
            CharPick == 4
        elif PickChar.lower() == "EasyMode":
            PickChosenOneText = ("You picked |The Chosen One| Easy |")
            CharPick == 5
        elif PickChar.lower() == "Nightmare":
            PickNightmareText = ("You picked |Nightmare| Goodluck |")
            CharPick == 6

def characterCreation():
    if CharPick == 1:
        NewCharHP == 
#use the class from character mod 
        

#Introduction()
characterSection()