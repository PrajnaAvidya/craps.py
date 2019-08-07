#!/usr/bin/env python3
"""craps simulator"""

# TODO calculate total ev/return for all bets instead of just result
# TODO export in a format that can be easily graphed

import random
import array

sessions = 1000
points = 50
bet_amount = 10
history = []
best_result = -999999
worst_result = 999999

def PlaySession():
    pl = 0
    global best_result
    global worst_result
    for game in range(1, points+1):
        #print('Playing game {0}'.format(game))
        pl += PlayGame(bet_amount)
    if pl > best_result:
        best_result = pl
    if pl < worst_result:
        worst_result = pl
    print('Session result: {0:+d}'.format(pl))
    return pl

def PlayGame(bet):
    roll = RollDice()
    if roll[2] == 7 or roll[2] == 11:
        #print('WIN come out')
        return bet
    elif roll[2] == 2 or roll[2] == 3 or roll[2] == 12:
        #print('LOSE come out')
        return -bet

    point = roll[2]
    #print('Point is {0}'.format(roll[2]))
    sidebet = 0
    payout = 1

    if point == 4 or point == 10:
        sidebet = bet * 3
        payout = 2
    elif point == 5 or point == 9:
        sidebet = bet * 4
        payout = 3/2
    elif point == 6 or point == 8:
        sidebet = bet * 5
        payout = 6/5

    rollpoint = 0
    while rollpoint != 7:
        roll = RollDice()
        rollpoint = roll[2]
        if rollpoint == point:
            #print('WIN roll')
            return bet + (sidebet * payout)

    #print('LOSE roll')
    return -bet - sidebet

def RollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #print('Rolled {0}'.format(dice1+dice2))
    return array.array('I', [dice1, dice2, dice1+dice2])

# todo bet amount
print('Playing {0} sessions\n'.format(sessions))

for session in range(1, sessions+1):
    pl = PlaySession()
    history.append(pl)

average_result = sum(history)/len(history)

print('\nAverage p/l for {0} sessions of {1} points with {2} pass bet and full odds: {3:+d}'.format(sessions, points, bet_amount, average_result))
print('Best result is {0:+d}'.format(best_result))
print('Worst result is {0:+d}'.format(worst_result))
