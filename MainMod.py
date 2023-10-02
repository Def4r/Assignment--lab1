import time
import random

def Introduction():
    print("Welcome to Dungeon Hunters")
    time.sleep(2)
    ContinueGame = str(input("Type 'PLAY' start the game skipping the intro and tutorial. Type 'LEARN' if you want to read the tutorial and intro of the game "))
    
    if ContinueGame.lower() == "play":
        return 1
    if ContinueGame.lower() == "learn":
        print("The objective of the game is to make it out of the dungeon")