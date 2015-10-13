import random

player = {'name' : 'Sheldor', 'health': 100, 'experience' : 0 , 'mana' : 50,
          'alive': True, 'inventory' : []}
          
player['inventory'].append('Sword of Azeroth')

def print_player(player):
    for key in player:
        print (key ,'is', player[key])

def compute_experience(damage):
    return random.randrange(0,damage*2)

def take_damage(player, damage):
    player['health'] -= damage
    player['experience'] += compute_experience(damage)
    if player['health'] <= 0:
        player['alive'] = False
    return player
    
while player['alive'] == True:
    take_damage(player, 20)
    print_player(player)
    
