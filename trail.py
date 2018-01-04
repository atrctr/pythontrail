#!/usr/bin/env python3

import random
import string

# Global variables
Day = 1 
People = 10 # you loose when it hits 0
SupplyDays = 14 # 1 gets used per day, at 0 one person dies every day
Money = 100
Destination = 1000 # you win once it is 0
BaseSpeed = 20 # miles per day

Weather = 'clear'

############ FUNCTIONS ######################
# WEATHER
def weather(PastWeather):
    chance = random.randint(0,1)
    if chance == 0:
        Weather = PastWeather
    else:
        woptions = ['sunny','overcast','rain','storm']
        Weather = random.choice(woptions)
    return Weather
    
# SPEED calculation based on weather and terrain
def SpeedCalc(weather):
    
    # Get the weather-based multiplier
    switcher = {
        'sunny' : 0.9,
        'overcast' : 1,
        'rain' : 0.75,
        'storm' : 0.5
    }
    weathermultiplier = switcher.get(weather, 1)
    
    # Actual speed is equal to base speed multiplied by modifiers from weather and terrain
    speed = BaseSpeed * weathermultiplier
    speed = int(speed)
    return speed


############ GAME ##########################
# Intro sequence
print("\n\tPython Trail of Tears\n\nYou win by reaching the Destination,\n",Destination,"miles away from here. Good luck!")

# MAIN LOOP
while Destination > 0:
    Weather = weather(Weather)
    Speed = SpeedCalc(Weather)
    # Show all status information
    print("\n### DAY",Day,"###########################")
    print("Survivors:",People,"\tSupplies:",SupplyDays,"\tMoney:",Money)

    print("Weather:",Weather)

    # If everyone is dead, game over
    if People <= 0:
        print("GAME OVER: All surivors are dead.")
        break

    # Normal ordinary turn when proceed with the loop
    if People > 0:
        Day = Day + 1
        Destination = Destination - Speed
        if SupplyDays > 0:
            SupplyDays = SupplyDays - 1
        elif SupplyDays <= 0:
            People = People - 1
        print("Travelled",Speed,"miles today.",Destination,"miles left.")

# VICTORY - any survivors and Destination reached
if People > 0:
    print("Day",Day)
    print("VICTORY")

# Game end
input("\n\tPress ENTER to exit")
quit()
