################
## TECHNOTHON Category 1 Round 2
## Question 4

# This program is a simulation of rock paper scissors game.
# user vs Computer. The computer picks randomly

import random

# This gets the number based on the players choice
def get_num(player):
    if player == 'R':
        plnum = 0
    elif player == 'P':
        plnum = 1
    elif player == 'S':
        plnum = 2
    else:
        plnum = -1
    return plnum

# This gets the computer's choice to be compared with player's choice
def get_comp():
    li = ['ROCK', 'PAPER', 'SCISSORS']
    comp_num = random.randint(0,2)
    comp_str = li[comp_num]
    print('The computer played:', comp_str)
    return comp_num




def comp_won(old_score):
    print('The Computer won. Score -1')
    old_score -= 1
    return old_score

def plr_won(old_score):
    print('You won! Score +1')
    old_score += 1
    return old_score




    
# Comparing the score of the player with that of the computer's.
def play_rps(player, score):
    pl_num = get_num(player)
    # If the user didn't choose an option, an error is printed.
    if pl_num == -1:
        print("Error. Pick from the abbreviations in the curly brackets")
    else:
        comp_num = get_comp()
        if (pl_num == 0 and comp_num == 2) or (comp_num == 0 and pl_num == 2):
            if comp_num == 0:
                score = comp_won(score)
            else:
                score = plr_won(score)
        elif pl_num > comp_num:
            score = plr_won(score)
        elif pl_num < comp_num:
            score = comp_won(score)
        elif pl_num == comp_num:
            print('Draw')
    print('Your score is', score)
    return score



######### MAIN #########################
scr = 0
while True:
    plr = input('{R}OCK, {P}APER, {S}CISSORS: ')
    scr = play_rps(plr, scr)
