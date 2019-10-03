# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        """Adds an item to this Room items list"""
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):  # for human consumption
        r = f"Room (name: {self.name} {self.description})\n"

        for i in self.items:
            r += f"    {i}\n"
        return r

    def __repr__(self):  # for programmer consumption
        #return f'Store("{self.store_type}")'
        return f'Room({repr(self.name)},{repr(self.description)},{repr(self.items)})'