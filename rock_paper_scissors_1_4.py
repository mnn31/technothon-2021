################
## TECHNOTHON Category 1 Round 2
## Question 4

# This program is a simulation of rock paper scissors game.
# user vs Computer. The computer picks randomly

import random

def get_num(player):
    if player == 'R':
        plnum = 0
    elif player == 'P':
        plnum = 1
    else:
        plnum = 2
    return plnum
        
def dry_rps(player):
    li = ['ROCK', 'PAPER', 'SCISSORS']
    comp_num = random.randint(0,2)

    comp_str = li[comp_num]
    print('The computer played:', comp_str)

    pl_num = get_num(player)
    if (pl_num == 0 and comp_num == 2) or (comp_num == 0 and pl_num == 2):
        if comp_num == 0:
            print('The Computer won.')
        else:
            print('You won!')
    elif pl_num > comp_num:
        print('You won!')
    elif pl_num < comp_num:
        print('The Computer won.')
    else:
        print('Draw')
    

def rps(player):
    li = ['ROCK', 'PAPER', 'SCISSORS']
    ai = random.randint(0,2)
    print(ai)

    comp_str = li[ai]
    print('The computer played:', comp_str)
    ai += 1
    if player =='R':
        if ai == 1:
            print('rock vs rock: draw')
        if ai == 2:
            print('rock vs paper: You win!')
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



######### MAIN #########################
while True:
    plr = input('{R}OCK, {P}APER, {S}CISSORS: ')
    dry_rps(plr)
