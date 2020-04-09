# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

    def moveTo(self, direction):
        if direction == 'n':
            if self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
            else:
                print("Can't go to the North...")
        elif direction == 's':
            if self.current_room.s_to != None:
                self.current_room = self.current_room.s_to
            else:
                print("Can't go to the South...")
        elif direction == 'e':
            if self.current_room.e_to != None:
                self.current_room = self.current_room.e_to
            else:
                print("Can't go to the East...")
        elif direction == 'w':
            if self.current_room.w_to != None:
                self.current_room = self.current_room.w_to
            else:
                print("Can't go to the West...")

    def displayRoom(self):
        print("##################################################################")
        print(f'Currently In: {self.current_room.name}')
        print("##################################################################")
        print(f"# {self.current_room.description}")
        print("##################################################################")
        print("Items in this room:")
        self.current_room.displayItems()
        print("##################################################################")

    def displayInventory(self):
        print("##################################################################")
        print(f"{self.name}'s Inventory:")
        for item in self.items:
            print(item)
        print("##################################################################")

    def addItem(self, item):
        exists = False
        for roomItem in self.current_room.items:
            if item == roomItem.name:
                self.items.append(roomItem)
                roomItem.onTake()
                self.current_room.removeItem(roomItem)
                exists = True
                break
        if not exists:
            print(f"{item} is not in here.")

    def dropItem(self, item):
        exists = False
        for inventoryItem in self.items:
            if item == inventoryItem.name:
                self.items.remove(inventoryItem)
                inventoryItem.onDrop()
                self.current_room.addItems(inventoryItem)
                exists = True
                break
        if not exists:
            print(f"{self.name} does not have that {item}.")