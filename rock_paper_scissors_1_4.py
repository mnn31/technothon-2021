################
## TECHNOTHON Category 1 Round 2
## Manan Gupta
## Inventure Academy
## Question 4

# This program is a simulation of rock paper scissors game.
# user vs Computer. The computer picks randomly

import random

######### MAIN #########################
while True:
    player = input('{R}OCK, {P}APER, {S}CISSORS: ')
    ai = random.randint(1, 3)
    if player =='R':
        if ai == 1:
            print('rock vs rock: draw')
        if ai == 2:
            print('rock vs paper: Yoßu win!')
        if ai == 3:
            print('rock vs scissor: Better luck next time!')
    elif player =='P':
        if ai == 1:
            print('paper vs rock: You win!')
        if ai == 2:
            print('paper vs paper: draw')
        if ai == 3:
            print('paper vs scissor: Better luck next time!')

    elif player =='S':
        if ai == 1:
            print('scissor vs rock: Better luck next time!')
        if ai == 2:
            print('scissor vs paper: You win!')
        if ai == 3:
            print('scissor vs scissor: draw')

    else:
        print("Pick from the abbreviations in the curly brackets.")

    print('')
