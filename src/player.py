# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room = 'outside', items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def take_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)

    def set_current_room(self, room):
        self.current_room = room

    def get_current_room(self):
        return self.current_room

    def __str__(self): # for humans
        p = f"Sir {self.name}\n"

        for i in self.items:
            p += f"    {i}\n"

        return p

    def __repr__(self): # for programmers
        return f'Player({repr(self.name)},{repr(self.items)})'