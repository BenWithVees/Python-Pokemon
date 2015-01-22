import random
import sys
bulb = "Bulbasaur"
char = "Charmander"
sqrt = "Squirtle"

pidgeyHP = 80

pokemon = input("A wild Pidgey appears! Who would you like to send out?: (Bulbasaur/Charmander/Squirtle) ")

i =0

while i == 0:
    if pokemon == bulb:
        print('Go,', bulb + '!')
        pokeHP = 100
        i += 1
    elif pokemon == char:
        print('Go,', char + '!')
        pokeHP = 110
        i+=1
    elif pokemon == sqrt:
        print('Go,', sqrt + '!')
        pokeHP = 95
        i+=1
    else:
        pokemon = input("You do not have " + pokemon + ". Please pick Bulbasaur/Charmander/Squirtle: ")

def bulbAttackList(x):
    bulbMov = input('Select a move: (Vine Whip/Razor Leaf/Headbutt/Pound) ')
    global pidgeyHP
    i = 0
    while i == 0:
        if x == "Vine Whip":
            pidgeyHP -= random.randint(10, 15)
            i += 1
        elif x == "Razor Leaf":
            pidgeyHP -= random.randint(20, 24)
            i += 1
        elif x == "Headbutt":
            pidgeyHP -= random.randint(13, 15)
            i += 1
        elif x == "Pound":
            pidgeyHP -= random.randint(8, 30)
            i += 1
        else:
            print("You do not have that attack. Please pick another: ")
    return pidgeyHP

def charAttackList(x):
    global pidgeyHP
    i = 0
    while i == 0:
        if x == 'Ember':
            pidgeyHP -= random.randint(13, 18)
            i += 1
        elif x == 'Scratch':
            pidgeyHP -= random.randint(10, 14)
            i += 1
        elif x == 'Metal Claw':
            pidgeyHP -= random.randint(10, 20)
            i += 1
        elif x == "Flamethrower":
            pidgeyHP -= random.randint(20, 23)
            i += 1
        else:
            print("You do not have that attack. Please pick another: ")
    return pidgeyHP
        
def sqrtAttackList(x):
    global pidgeyHP
    i = 0
    while i == 0:
        if x == 'Water Gun':
            pidgeyHP -= random.randint(8, 20)
            i += 1
        if x == 'Bubblebeam':
            pidgeyHP -= random.randint(6, 23)
            i += 1
        if x == 'Return':
            pidgeyHP -= random.randint(5, 37)
            i += 1
        if x == 'Tackle':
            pidgeyHP -= random.randint(10, 15)
            i += 1
        else:
            print("You do not have that attack. Please pick another: ")
    return pidgeyHP
    
def pidgeyAttackList(x):
    global pokeHP
    if x == "Gust":
        pokeHP -= random.randint(10, 15)
    elif x == "Peck":
        pokeHP -= random.randint(8, 10)
    elif x == "Quick Attack":
        pokeHP -= random.randint(10, 15)
    return pokeHP

def pidgeyBot():
    global pokemon
    global pokeHP
    global pidgeyHP
    if pidgeyHP > 0:            
        print('Pidgey used', randomPidgey,'\n')
        pidgeyAttackList(randomPidgey)
    if pokeHP <= 0:
        print(pokemon, 'fainted!')
    else:
        print(pokemon, 'has', pokeHP, 'HP left\n')

pidgeyList = ["Gust", "Peck", "Quick Attack"]
sqrtList = ['Water Gun', 'Bubblebeam', 'Return', 'Tackle']
charList = ['Ember', 'Scratch', 'Metal Claw', 'Flamethrower']
bulbMove = ["Vine Whip", "Razor Leaf", "Headbutt", "Pound"]
selectMove = input("What would you like to do? (Attack/Run): ")
randomPidgey = pidgeyList[random.randint(0, 2)]

while True:
    if selectMove.lower() == 'run':
        print('Got away safely!')
    while pidgeyHP > 0 and pokeHP > 0:
        randomPidgey = pidgeyList[random.randint(0, 2)]
        if selectMove.lower() == 'attack':
            if pokemon == bulb:
                if pokeHP > 0:
                    if bulbMov in bulbMove:
                        print('Bulbasaur used', bulbMov + '!\n')
                        bulbAttackList(bulbMov)
                        if pidgeyHP <= 0:
                            print("Pidgey fainted!")
                        else:
                            print("Pidgey now has", pidgeyHP, 'HP left.\n')
                            pidgeyBot()
                    else:
                        i = 0
                        
                            
            elif pokemon == char:
                charMove = input('Select a move: (Ember/Scratch/Metal Claw/Flamethrower) ')
                if pokeHP > 0:
                    if charMove in charList:
                        print('Charmander used', charMove + '!\n')
                        charAttackList(charMove)
                        if pidgeyHP <= 0:
                            print("Pidgey fainted!")
                        else:
                            print("Pidgey now has", pidgeyHP, 'HP left.\n')
                            pidgeyBot()
            elif pokemon == sqrt:
                sqrtMove = input('Select a move: (Water Gun/Bubblebeam/Return/Tackle) ')
                if pokeHP > 0:
                    if sqrtMove in sqrtList:
                        print('Squirtle used', sqrtMove + '!\n')
                        sqrtAttackList(sqrtMove)
                        if pidgeyHP <= 0:
                            print("Pidgey fainted!")
                        else:
                            print("Pidgey now has", pidgeyHP, 'HP left.\n')
                            pidgeyBot()
            
