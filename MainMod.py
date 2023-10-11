import time
import random
import sys
import CharacterMod as CM
import DiceMod 
from DiceMod import diceI
from DiceMod import dicesII
from DiceMod import pickDice
from time import sleep
from sys import stdout

CharPick = 0
DiceRolled = 0
DistanceRan = 0



ErrorText = "ERROR :["
GameLoseText = "YOU LOSE !!"
GameWinText = "YOU WON !!"
RollDiceText = "Type 'roll' to roll your dice"


run = time.perf_counter()
while time.perf_counter() - run < 5:
    LuckHit = random.randint(1,100)


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
        TextI = "The objective of the game is to make it out of the dungeon ALIVE. There will be 3 stages you will have to defeat in order to escape the dungeon. This game is dice based and will determine how the game will end up playing. If you roll an even number you attack, if you roll an odd you will have to run and may take a hit."
        for char in TextI:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(2)
        print("")
        TextII = "You will have to pick between a varity of characters. They all have different stats and attributes before you choose your character here's a breif overview of them"
        for char in TextII:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(1)
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
            for char in PickRougeText:
                sleep(0.04)
                stdout.write(char)
                stdout.flush()
            CharPick =+ 1
        elif PickChar.lower() == "Knight":
            PickKnightText = ("You have picked |The Knight|")
            CharPick =+ 2
        elif PickChar.lower() == "Mage":
            PickMageText = ("You picked |The Mage|")
            CharPick =+ 3
        elif PickChar.lower() == "Tank":
            PickTankText = ("You picked |The Tank|")
            CharPick =+ 4

if CharPick == 1:
    NewCharHP = CM.RougeCharHP
    NewCharAttack = CM.RougeCharAttack
    NewCharShield = CM.RougeCharShield
    NewCharLH = CM.RougeCharLuckHit
elif CharPick == 2:

def playerLose():
    if NewCharHP == 0:
        for char in GameLoseText:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(2)
        exit()

def stage1():

    NowStage_HP = CM.Stage1HP
    NowStage_Attack = CM.Stage1Attack
    NowStage_Speed = CM.Stage1Speed
    
    TextV = "Stage 1"
    for char in TextV:
        sleep(0.04)
        stdout.write(char)
        stdout.flush()
    print("")
    sleep(0.5)
    TextVI = "You are fighting the guardian of the dungeon... He looks over at you ready for combat"
    for char in TextVI:
        sleep(0.04)
        stdout.write(char)
        stdout.flush()
    print("")
    
    stage1run = 1

    CharPickTest = 1

    while stage1run == 1:
        print(RollDiceText)
        sleep(0.5)
        DiceRollPromptI = input(":>")
        if DiceRollPromptI.lower() == "roll":
            if CharPickTest == 1:
                NumRollI = dicesII()
                print("You rolled a", NumRollI)
            if NumRollI % 2 == 0:
                sleep(1)
                print("You also rolled an even number so you got a hit")
                sleep(2)
                if(LuckHit < 88 and LuckHit > 0):
                    NowStage_HP = NowStage_HP - CM.RougeCharHP * 2
                    print("You got LUCKY_HIT you dealt double damage!!")
                    sleep(2)
                    print("Guardian only has", NowStage_HP,"more hitpoints")
                else:
                    print("You damaged the Guardian. They only have ", NowStage_HP, " more hitpoints")
            elif NumRollI % 2 != 0:
                sleep(1)
                print("You also rolled an odd number you have to run")
                sleep(2)
                if(NowStage_Speed * random.randint(2, 5) > NumRollI):
                    CM.RougeCharHP == CM.RougeCharHP - NowStage_Attack
                    print("The Guradian got you and you also got hit. You took ", NowStage_Attack, " Damage points")
                    #as the rouge you lose 


            if CharPick == 2 or 3 or 4:
                NumRollII = dicesII()
                print("You rolled ", NumRollII)
    


#note fix up the character creator again. and test program 'check indens if it doesnt work'
        

#Introduction()
characterSection()
stage1()