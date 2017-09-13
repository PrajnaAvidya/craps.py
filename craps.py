#!/usr/bin/env python3
"""craps simulator"""

# TODO calculate total ev/return for all bets instead of just result
# TODO export in a format that can be easily graphed

import random
import array

sessions = 10
games = 50
bankroll = 0
starting_bankroll = 1000
bet_amount = 10
history = []

def PlaySession():
    global bankroll
    for game in range(1, games+1):
        #print('Bankroll is {0}'.format(bankroll))
        #print('Playing game {0}'.format(game))
        bankroll += PlayGame(bet_amount)
        if (bankroll <= 0):
            #print('BUSTED')
            break

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
        sidebet = bet * 3;
        payout = 2;
    elif point == 5 or point == 9:
        sidebet = bet * 4;
        payout = 3/2;
    elif point == 6 or point == 8:
        sidebet = bet * 5;
        payout = 6/5;

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

for session in range(1, sessions+1):
    bankroll = starting_bankroll
    print('Starting Session {0}'.format(session))
    PlaySession()
    #print('Session ending bankroll is {0}'.format(bankroll))
    history.append(bankroll)

average_result = sum(history)/len(history)
print('Average result is {0}'.format(average_result))
