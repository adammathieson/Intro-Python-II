# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.adj_room = []
        self.items = []

    def add_item(self, item):
        """Adds an item to this Room items list"""
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)

    def check_for_items(self):
        # for i in self.items:
        return self.items

    def set_adj_room(self, dir, room):
        newRoom = {dir:room}
        self.adj_room.append(newRoom)

    def get_adj_room(self):
        # rooms = []
        # for i in self.adj_room:
        #     for k, v in i.items():
        #         rooms.append({k, v}
        #     return rooms
        rooms = []
        for i in self.adj_room:
            rooms.append(i)
        return rooms

        # return self.adj_room
        # for k, v in i in self.adj_room.items():
        #     return f"{v}"
            

    def __str__(self):  # for human consumption
        r = f"{self.name}--  {self.description}\n"

        for i in self.items:
            r += f"    You see a {i} sitting nearby\n"
        return r

    def __repr__(self):  # for programmer consumption
        return f'Room({repr(self.name)},{repr(self.description)},{repr(self.items)})'