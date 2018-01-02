#!/usr/bin/env python3

# Welcome to Python Trail I guess

import random
import string

# Global variables

Day = 1
People = 10
SupplyDays = 14
Money = 100

# Intro sequence

print("\n\tPython Trail of Tears")

# Main game loop
while Day < 365:
    # Normal ordinary turn when everyone is alive
    if People > 0:
        print("\n### DAY",Day,"###")
        print("Survivors:",People,"\tSupplies:",SupplyDays,"\tMoney:",Money)
        Day = Day + 1
        if SupplyDays > 0:
            SupplyDays = SupplyDays - 1
        elif SupplyDays <= 0:
            People = People - 1
    # Everyone is dead.
    if People <= 0:
        print("GAME OVER\nEveryone has died.")
        break

# If on day 365 some is still alive...
if People > 0:
    print("Day",Day)
    print("VICTORY")


# Game end
print("\n\tEnd of game")
input("\n\tPress ENTER to exit")
quit()
