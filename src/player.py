# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room = 'outside', items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self): # for humans
        p = f"Player (name:) {self.name}\n"


        for i in self.items:
            p += f"    {i}\n"

        return p

    def __repr__(self): # for programmers
        return f'Player({repr(self.name)},{repr(self.items)})'