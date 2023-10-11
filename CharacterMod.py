# CharHP - Amount of health point that character can take before the game ends. This will not regenerate ever.
# CharSpeed  - This is one of the most important stats in this game. It decides what dice you will use in the game. This can massively change the game.
# CharShield - This is similar to you CharHP but it regenerates 1 point per turn this will be your first set of defense.
# CharAttack - How much Attack point you deal to other mobs in the game.
# CharLuckHit - Changes the chance that your character can double hit. Higher the number the more lucky you are to get a double hit. having 0 doesn't mean you don't have any but you would just have the default amount
# There will also be difficulty characters that you can pick that would make the game easier or harder. They have over turned stats to make that experience. 

#Each stage will have a single fight the player will need to complete here I will example the stats
#Stage_HP - The overall health the Boss can take
#Stage_Attack - How much damage they can deal to you each turn.
#Stage_Speed - If you do decide to run this would be how fast they can catch you getting a free hit. The number would be multipled by a random number [2 - 5] to get the true distance.

#Stats for the rouge:
RougeCharHP = 1
RougeCharSpeed = "dicesII"
RougeCharShield = 0
RougeCharAttack = 1
RougeCharLuckHit = 2

#Stats for the Tank:
TankCharHP = 2
TankCharSpeed = "dicesI"
TankCharShield = 2
TankCharAttack = 1
TankCharLuckHit = 0

#Stats for the Mage:
MageCharHP = 1
MageCharSpeed = "dicesI"
MageCharShield = 2
MageCharAttack = 1
MageCharLuckHit = 2

#Stats for the Knight
KnightCharHP = 2
KnightCharSpeed = "DicesI"
KnightCharShield = 1
KnightCharAttack = 2
KnightCharLuckHit = 1

#Stage 1 Boss Fight Stats
Stage1HP = 4
Stage1Attack = 1
Stage1Speed = 1

#Stage 2 Boss fight stats | Can't be used 
Stage2HP = 6
Stage2Attack = 2
Stage2Speed = 2

#Stage 3 Boss fight stats
# Was deleted

#Only rouge is being used 