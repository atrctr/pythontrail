#!/usr/bin/env python3

import random

# this deals with random events throughout the game.

# Define events
class Event(object):
    def __init__(self, what = None):
        self.name = "Generic event"
        self.description = what or "Generic description"
        
    def display(self):
        print(self.description)
        
    def effect(self):
        pass


Events = [
    # Simple events that do not affect the game
    Event('Nothing happened.'),
    Event('You see vultures following the caravan.'),
    Event('You pass a ruined settlement.'),
    Event('You encounter an abandoned camp.'),
    Event('A village filled with corpses. Better move on.')
    
    # TODO Interactive events
]

def GetEvent():
    event = random.choice(Events)
    return event
