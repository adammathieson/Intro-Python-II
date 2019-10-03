# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, adj_room ={'n':'','e':'','s':'','w':''}, items = []):
        self.name = name
        self.description = description
        self.adj_room = adj_room
        self.items = items

    def add_item(self, item):
        """Adds an item to this Room items list"""
        self.items.append(item)

        
    def remove_item(self, item):
        self.items.remove(item)

    def set_adj_room(self, dir, room):
        newRoom = {dir:room}
        self.adj_room.update(newRoom)
        # print(self.adj_room)

    def get_adj_room(self):
        rooms = []
        for i in self.adj_room.items():
            rooms.append(i)
        return rooms
        # return self.adj_room
        # for k, v in i in self.adj_room.items():
        #     return f"{v}"
            

    def __str__(self):  # for human consumption
        r = f"{self.name}--  {self.description}\n"

        for i in self.items:
            r += f"    {i}\n"
        return r

    def __repr__(self):  # for programmer consumption
        #return f'Store("{self.store_type}")'
        return f'Room({repr(self.name)},{repr(self.description)},{repr(self.items)})'