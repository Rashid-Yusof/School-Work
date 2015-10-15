from map import rooms
from items import *
from player import *
from gameparser import skip_words
import string

def display_room(room):
    print('')
    print(room['name'].upper())
    print('')
    print(room['description'])
    print('')
    print_room_items(room)
    print('')
    
#display_room(rooms['Office'])

def print_menu_line(direction, leads_to):
    print('Go', direction.upper(), 'to', leads_to.upper())
    
#print_menu_line('east', 'Bathroom')

def exit_leads_to(exits, direction):
    room_id = exits[direction]
    room = rooms[room_id]
    return(room['name'])
        
#exit_leads_to(rooms['Reception']['exits'], 'south')

def print_menu(exits, room_items, inv_items):
    print ('You can:')
    
    for key in exits:
        print_menu_line(key, exit_leads_to(exits, key))
    for item in room_items:
        print ('TAKE',item['id'].upper(),'to take',item['name'].upper())
    for item in inv_items:
        print ('DROP', item['id'].upper(),'to drop',item['name'].upper())
    print('What do you want to do?')

#print_menu(rooms['Reception']['exits'],rooms['Reception']['items'],inventory )

def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    answer = normalise_input(input('> '))
    return answer       

def move(exits, direction):
    return rooms[exits[direction]]
    
        
#move(rooms['Reception']['exits'],'east')
        
def is_valid_exit(exits, user_input):
    if user_input in exits:
        return True
    else:
        return False
        
def remove_punct(text):
    for c in string.punctuation:
        text = text.replace(c, '')
    return text

#print (remove_punct('Hello, I am Rashid.@#$'))

def remove_spaces(text):
    text = text.lstrip()
    text = text.rstrip()
    return text
    
def filter_words(words, skip_words):
    new_list = []
    words = words.split()
    for word in words:
        if not word in skip_words:
            new_list.append(word)
    return ''.join(new_list)
    
#print (filter_words("help me please", ["me", "please"]))
    
def normalise_input(user_input):
    user_input = remove_punct(user_input)
    user_input = remove_spaces(user_input)
    user_input = filter_words(user_input, skip_words)
    return user_input.lower()
    
def list_of_items(items):
    new_list = []
    for item in items:
        new_list.append(item['name'])
    return ', '.join(new_list)
    
#print (list_of_items([item_money, item_handbook, item_laptop]))

def print_room_items(room):
    print ('There is' ,list_of_items(room['items']), 'here.')
    print ('\n')
    
#print_room_items(rooms["Office"])
    
def print_inventory_items(items):
    print ('You have',list_of_items(items) + '.')
    
#print_inventory_items(inventory)
    
def execute_go(direction):
    global current_room
    if direction in current_room['exits']:
        roomid = current_room['exits'][direction]
        current_room = rooms[roomid]
        return current_room
    else:
        print ("You cannot go there.")
        
print (current_room['exits']['south'])
print (execute_go('south'))
    
def execute_take(item_id):
    if item_id in current_room['items']:
        inventory = inventory.append(item_id)
        current_room['items'] = current_room['items'].remove(item_id)
    else:
        print ('You cannot take that')
        
def execute_drop(item_id):
    if not item_id in current_room['items']:
        inventory = inventory.remove(item_id)
        current_room['items'] = current_room['items'].append(item_id)
    else:
        print ('You cannot drop that')
    
def execute_command(command):

    if 0 == len(command):
        return
        
    command = command.split()

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")
        
def main():
    
    while True:
        display_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)    

#main()