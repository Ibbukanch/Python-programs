# Program Of Gambler
import random
stake=int(input("Enter the stake\n"))
goal=int(input("Enter the goal\n"))
trials=int(input("Enter the trials\n"))
bets=0
wins=0
# Traverse from 0 to trials
for i in range(trials):
    cash=stake                         # Initialize Stake to Cash
    while cash > 0 and cash < goal:
        bets=bets+1
        if random.random() < 0.5:
            cash = cash + 1
        else:
            cash = cash - 1
    if cash == goal:
        wins=wins + 1                  #If cash reached to goal then increment wins
x=100*wins/trials
a=100-x
# Printing percentage of Game won,loss.
print(str(wins) + " wins of " + str(trials))
print("Percent of games won = " + str(x))
print("Percent of game loss="+str(a))
print("Avg # bets           = " + str(bets / trials))

