from room import Room
from player import Player

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

#
# Main
#


def getValidMoves(room):
    valid_moves = []
    if room.n_to:
        valid_moves.append('[n - to move North]')
    if room.s_to:
        valid_moves.append('[s - to move South]')
    if room.e_to:
        valid_moves.append('[e - to move East]')
    if room.w_to:
        valid_moves.append('[w - to move West]')
    return valid_moves


# Make a new player object that is currently in the 'outside' room.
player1 = Player("player1", room['outside'])
print(player1)
print(player1.current_position)

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
error_message = 'xxxxxxx You can not go that way. Please enter a valid move. xxxxxxx'
while True:
    valid_moves = getValidMoves(player1.current_position)
    valid_moves_str = ""
    for move in valid_moves:
        valid_moves_str += move + " "
    move = input("Please enter one of these moves:\n " +
                 valid_moves_str + ". Enter q to quit.\n")
    if move == 'n':
        if player1.current_position.n_to:
            player1.current_position = player1.current_position.n_to
        else:
            print(error_message)
    elif move == 's':
        if player1.current_position.s_to:
            player1.current_position = player1.current_position.s_to
        else:
            print(error_message)
    elif move == 'e':
        if player1.current_position.e_to:
            player1.current_position = player1.current_position.e_to
        else:
            print(error_message)
    elif move == 'w':
        if player1.current_position.w_to:
            player1.current_position = player1.current_position.w_to
        else:
            print(error_message)
    elif move == 'q':
        print("--------- Thank you for playing! ---------")
        break
    else:
        print("xxxxxxx Please enter one of the valid options, or q to quit xxxxxxx")
    print(player1)
    print(player1.current_position)
