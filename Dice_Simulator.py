import random

def dice_roll(min,max):
    while True:
        
        number=random.randint(min,max)
        print('The dice is rolling!!....')
        print("Result....",number)
        choice=input('Want To Roll Again(y/n)....')
        if choice=='n' or choice=='N':
            break
dice_roll(1,6)
