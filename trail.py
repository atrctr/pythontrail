#!/usr/bin/env python3

import random
import string

# Global variables

Day = 1
People = 10
SupplyDays = 14 # 1 gets used per day
Money = 100
Distance = 0
Destination = 1000 # miles 
BaseSpeed = 20 # miles per day

# Intro sequence

print("\n\tPython Trail of Tears\n\nYou win by reaching the Destination,\n1000 miles away from home. Good luck!")

# Main game loop
while Distance < Destination:

    # Show all status information
    print("\n### DAY",Day,"###########################")
    print("Travelled",Distance,"miles")
    print("Survivors:",People,"\tSupplies:",SupplyDays,"\tMoney:",Money,"\n")

    # If everyone is dead, game over
    if People <= 0:
        print("GAME OVER: All surivors are dead.")
        break

    # Normal ordinary turn when proceed with the loop
    if People > 0:

        Day = Day + 1
        Speed = BaseSpeed
        Distance = Distance + Speed
        if SupplyDays > 0:
            SupplyDays = SupplyDays - 1
        elif SupplyDays <= 0:
            People = People - 1


# If on day 365 some is still alive...
if People > 0:
    print("Day",Day)
    print("VICTORY")

# Game end
input("\n\tPress ENTER to exit")
quit()
