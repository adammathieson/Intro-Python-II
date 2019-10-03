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

# for i in room:
#     for i in i:

# print(room['outside'])

# for k, v in room.items():
#     print("{} {}".format(k, v))

# import textwrap
# print(textwrap.fill("Treasure Chamber, You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", width=50))

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

room['outside'].set_adj_room('n', 'foyer')
room['foyer'].set_adj_room('s', 'outside')
room['foyer'].set_adj_room('n', 'overlook')
room['foyer'].set_adj_room('e', 'narrow')
room['overlook'].set_adj_room('s', 'foyer')
room['narrow'].set_adj_room('w', 'foyer')
room['narrow'].set_adj_room('n', 'treasure')
room['treasure'].set_adj_room('s', 'narrow')

print("----->", room['outside'])
# print(room['foyer'].get_adj_room())
foyer = room['foyer']
print(foyer)
print(foyer.get_adj_room())
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("🧙‍♂️ Enter your player name ")
player = Player(player_name)

# print(player1.get_current_room())
# player1.take_item('Hammer')
# player1.take_item('Shield')
print(player)
current = room[player.get_current_room()]
print("---->", current)
choices = current.get_adj_room()
print(choices)



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
