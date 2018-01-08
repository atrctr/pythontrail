#!/usr/bin/env python3

import random
import string
import events

# Global variables
Day = 1 
Destination = 1000 # you win once it is 0
BaseSpeed = 20 # miles per day
# Starting conditions
Weather = 'clear'
Terrain = 'plains'
People = 10 # you loose when it hits 0
SupplyDays = 14 # 1 gets used per day, at 0 one person dies every day
Money = 100

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

    Weather = weather(Weather) # Determine today's weather
    Terrain = terrain(Terrain) # Determine the terrain
    Speed = SpeedCalc(Weather,Terrain)  # Determine speed based on weather and terrain
    
    # SUPPLIES 
    if SupplyDays > 0: # If you have supplies, consume 1 days worth
        SupplyDays = SupplyDays - 1 
    elif SupplyDays <= 0:   # If no supplies, one person DIES.
        People = People - 1
        Speed = 0.5 * Speed # Speed is halved if you are starving.

    # Calculate remaining distance
    Destination = Destination - Speed   

    # Show all status information
    print("\n\n### DAY",Day,"###")
    print("Survivors:",People,"\tSupplies:",SupplyDays,"\tMoney:",Money,"\nWeather:",Weather,"\tTerrain:",Terrain)
        
    # If everyone is dead, game over
    if People <= 0:
        print("\nGAME OVER: All surivors are dead.")
        break
    # Normal ordinary turn when proceed with the loop
    elif People > 0:
        theEvent = events.GetEvent() # Fetch the random event
            
        print("Travelled",Speed,"miles today -",Destination,"miles left.\n")
        theEvent.display()
        
        Day = Day + 1   # Progress the day counter

# VICTORY - any survivors and Destination reached
if People > 0:
    print("Day",Day)
    print("VICTORY")

# Game end
input("\n\tPress ENTER to exit")
quit()
