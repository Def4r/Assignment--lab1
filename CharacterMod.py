# CharHP - Amount of health point that character can take before the game ends. This will not regenerate ever.
# CharSpeed  - This is one of the most important stats in this game. It decides what dice you will use in the game. This can massively change the game.
# CharShield - This is similar to you CharHP but it regenerates 1 point per turn this will be your first set of defense.
# CharAttack - How much Attack point you deal to other mobs in the game.
# CharLuckHit - Changes the chance that your character can double hit. Higher the number the more lucky you are to get a double hit. having 0 doesn't mean you don't have any but you would just have the default amount
# There will also be difficulty characters that you can pick that would make the game easier or harder. They have over turned stats to make that experience. 

def Rouge():
    CharHP = 1
    CharSpeed = "dicesII"
    CharShield = 0
    CharAttack = 1
    CharLuckHit = 2

def Tank():
    CharHP = 2
    CharSpeed = "dicesI"
    CharShield = 2
    CharAttack = 1
    CCharLuckHit = 0

def Mage():
    CharHP = 1
    CharSpeed = "pickDices"
    CharShield = 2
    CharAttack = 1
    CharLuckHit = 2

def Knight():
    CharHP = 2
    CharSpeed = "pickDices"
    CharShield = 1
    CharAttack = 2
    CharLuckHit = 1

def Nightmare():
    CharHP = 1
    CharSpeed = "dicesI"
    CharShield = 0
    CharAttack = 1
    CharLuckHit = 0

def ChosenOne():
    CharHp = 2
    CharSpeed = "dicesII"
    CharShield = 2
    CharAttack = 2
    CharLuckyHit = 2