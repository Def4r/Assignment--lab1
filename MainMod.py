import time
import random
import sys
import CharacterMod as CM
import DiceMod
from time import sleep
from sys import stdout

CharPick = 0
NewCharHP = 0
NewCharSpeed = 0
NewCharShield = 0
NewCharAttack = 0
NewCharLH = 0
NowStage_HP = 0 
NowStage_Attack = 0
NowStage_Speed = 0

ErrorText = "ERROR :["
GameLoseText = "YOU LOSE !!"
GameWinText = "YOU WON !!"


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
            for char in PickRougeText:
                sleep(0.04)
                stdout.write(char)
                stdout.flush()
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

def characterCreation():
    if CharPick == 1:
        NewCharHP == CM.RougeCharHP
        NewCharSpeed == CM.RougeCharSpeed
        NewCharAttack == CM.RougeCharAttack
        NewCharShield == CM.RougeCharShield
        NewCharLH == CM.RougeCharLuckHit
    elif CharPick == 2:
        NewCharHP
        NewCharSpeed == CM.KnightCharSpeed
        NewCharAttack == CM.KnightCharAttack
        NewCharShield == CM.KnightCharShield
        NewCharLH == CM.KnightCharLuckHit
    elif CharPick == 3:
        NewCharHP == CM.MageCharHP
        NewCharSpeed == CM.MageCharSpeed
        NewCharAttack == CM.MageCharAttack
        NewCharShield == CM.MageCharShield
        NewCharLH == CM.MageCharLuckHit
    elif CharPick == 4:
        NewCharHP == CM.TankCharHP
        NewCharSpeed == CM.TankCharSpeed
        NewCharAttack == CM.TankCharAttack
        NewCharShield == CM.TankCharShield
        NewCharLH == CM.TankCharLuckHit

def playerLose():
    if NewCharHP == 0:
        for char in GameLoseText:
            sleep(0.04)
            stdout.write(char)
            stdout.flush()
        sleep(2)
        exit()

def stage1():

    NowStage_HP == CM.Stage1HP
    NowStage_Attack == CM.Stage1Attack
    NowStage_Speed == CM.Stage1Speed
    
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

    while stage1run == 1:
        if input("Press Enter to roll your dice") == "":
            if CharPick == 1:
                DiceMod.dicesII
                TextVII
                

        


    



#use the class from character mod 
        

#Introduction()
characterSection()
stage1()