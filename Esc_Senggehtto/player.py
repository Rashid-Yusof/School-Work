from items import *
from map import rooms

inventory = []

wearing = []

def inventory_limit(inventory):
    if len(inventory) >= 6:
        print ("You are carrying too many items.")
    
# Start game at the reception
current_room = rooms["Bedroom"]
