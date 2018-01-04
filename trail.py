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
Terrain = 'plains'

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

# TERRAIN
def terrain(PastTerrain):
    toptions = [PastTerrain,'plains','hills','mountains','forest']
    terrain = random.choice(toptions)
    return terrain
    
# SPEED calculation based on weather and terrain
def SpeedCalc(weather,terrain):
    
    # Get the weather-based multiplier
    switcher = {
        'sunny' : 0.9,
        'overcast' : 1,
        'rain' : 0.75,
        'storm' : 0.5
    }
    weather = switcher.get(weather, 1)
    
    # Get the terrain-based multiplier
    switcher = {
        'plains' : 1,
        'hills' : 0.75,
        'forest' : 0.8,
        'mountains' : 0.5
    }
    terrain = switcher.get(terrain, 1)
    
    # Actual speed is equal to base speed multiplied by modifiers from weather and terrain
    speed = BaseSpeed * weather * terrain
    speed = int(speed)
    return speed


############ GAME ##########################
# Intro sequence
print("\n\tPython Trail of Tears\n\nYou win by reaching the Destination,\n",Destination,"miles away from here. Good luck!")

# MAIN LOOP
while Destination > 0:
    Weather = weather(Weather)
    Terrain = terrain(Terrain)
    Speed = SpeedCalc(Weather,Terrain)
    # Show all status information
    print("\n# DAY",Day,"#################################")
    print("Survivors:",People,"\tSupplies:",SupplyDays,"\tMoney:",Money)

    print("Weather:",Weather,"\tTerrain:",Terrain)

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
