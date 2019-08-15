from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# create items
sword = Item("sword", "A mighty silver night sword!")
rock = Item("rock", "Just a regular rock.")
key = Item("key", "A regular key. What door or chest will it open?")
chest = Item("chest", "Treasure chest. Do you have the key to open it?")

# Add items to room
room["treasure"].items.append(chest)
room["overlook"].items.append(key)
room["outside"].items.append(rock)
room["treasure"].items.append(sword)

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player1 = Player("player1", room['outside'])

# print(player1)
# items = player1.current_position.get_items()
# if items:
#     print(
#         f"The items available in {player1.current_position.name} are: " + items + '\n')
# else:
#     print("There are no items in this room.\n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = ('n', 's', 'e', 'w')
print(player1)
print(player1.current_position)
player1.current_position.get_items()
while True:
    current_position = player1.current_position
    moves = current_position.get_moves()
    moves = " ".join(moves)
    cmd = input("\nPlease enter one of these directions:\n 1- " +
                moves + "\n 2- take/drop item_name - to take or drop an item. \n 3- Enter q to quit.\n ->  ")
    action = cmd.split()
    if len(action) == 1:
        if action[0] in valid_directions:
            player1.move(action[0])
        elif action[0] == 'q':
            print("--------- Thank you for playing! ---------")
            break
        else:
            print("xxxx Invalid entry xxxx")
    elif len(action) == 2:
        verb = action[0]
        item = action[1]
        if verb != "take" and verb != "drop":
            print(
                "xxxxxxx Please enter one of the valid options (take or drop), or q to quit xxxxxxx")
        else:
            player1.action(verb, item)
