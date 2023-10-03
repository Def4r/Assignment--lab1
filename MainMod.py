import time
import random
import sys
from time import sleep

def Introduction():
    Title = "Welcome to Dungeon Hunters"
    for char in Title:
        sleep(0.1)
        sys.stdou.write(char)
        sys.stdou.flush
    time.sleep(2)
    ContinueGame = str(input("Type 'PLAY' start the game skipping the intro and tutorial. Type 'LEARN' if you want to read the tutorial and intro of the game "))
    
    if ContinueGame.lower() == "play":
        return 1
    if ContinueGame.lower() == "learn":
        print("The objective of the game is to make it out of the dungeon ALIVE.")
        time.sleep(2)
        print("You will have to pick between a varity of characters. They all have different stats and attributes before you choose you character you will see a breif overview of them")