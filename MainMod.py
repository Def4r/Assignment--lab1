import time
import random
import sys
from time import sleep

def Introduction():
    Title = "||Welcome to Dungeon Hunters||"
    for char in Title:
        sleep(0.09)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(2)
    print("")

    ContinueGame = "Type 'PLAY' start the game skipping the intro and tutorial. Type 'LEARN' if you want to read the tutorial and intro of the game"
    for char in ContinueGame:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("")
    ContinuePrompt = str(input(":>"))
    
    if ContinuePrompt.lower() == "play":
        return "true"
    
    if ContinuePrompt.lower() == "learn":
        print("")
        TextI = "The objective of the game is to make it out of the dungeon ALIVE."
        for char in TextI:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(2)
        print("")
        TextII = "You will have to pick between a varity of characters. They all have different stats and attributes before you choose you character you will see a breif overview of them"
        for char in TextII:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        RougeSum = "Rouge: Fast, aglie and has access to double dice which allows them to travel faster but can't take hits and will die easily"
        print("")
        time.sleep(1)
        KnightSum = ""
        print("")
        time.sleep(1)
        TankSum = ""
        print("")
        time.sleep(1)
        MageSum = ""
        print("")
        time.sleep(1)
        DifficultyChars = ""
        print("")
        time.sleep(2)

        TextIII = "Now the game will start first you will pick your character then the game i will begin."
        for char in TextIII:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        return "true"

def characterSection():
    if Introduction() == "true":
        TextIV = "Pick you character | Type ....."
        for char in TextIV:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        PickChar = str(input(":>"))

Introduction()
characterSection()