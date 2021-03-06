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


# Create items -- initialize

maps = Item("maps", "To give you clues")
telescope = Item("telescope", "To look out")
compass = Item("compass", "To find your way")
lantern = Item("lantern", "To provide some light")
chest = Item("chest", "Once held the treasure")

room['foyer'].addItems(maps, telescope)
room['overlook'].addItems(telescope, compass)
room['narrow'].addItems(lantern, maps)
room['treasure'].addItems(chest, maps)

#
# Main
#
username = input("What is your name? ")

# Make a new player object that is currently in the 'outside' room.
player = Player(username, room['outside'])

# Write a loop that:
while True:
    player.displayRoom()

    user = input("[n] North\t[s] South\t[e] East\t[w] West\n[i] Inventory\n[take item]\t [drop item]\n[q] Quit\n Input: ").lower()

    inputs = user.split()

    directions = ('n', 's', 'e', 'w')

# * Waits for user input and decides what to do.
# If the user enters "q", quit the game.
    if len(inputs) == 1:
        if inputs[0] == 'q':
            break
    # If the user enters a cardinal direction, attempt to move to the room there.
        elif inputs[0] in directions:
            player.moveTo(inputs[0])
        elif inputs[0] == 'i':
            player.displayInventory()

    elif len(inputs) == 2:
        if inputs[0] == "get" or inputs[0] == "take":
            player.addItem(inputs[1])
        elif inputs[0] == "drop":
            player.dropItem(inputs[1])
    # Print an error message if the movement isn't allowed.
    else:
        print('Command not valid.')

    print("\n\n\n")








