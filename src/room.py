# Implement a class to hold room information. This should have name and
# description attributes.

from player import Player
class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    def __str__(self):
        return f' {self.name}\n\n{self.description}'

    def room_inventory(self):
        if self.items is None:
            print('No items here')
        else:
            for item in self.items:
                print(f'there is a {item.name}')