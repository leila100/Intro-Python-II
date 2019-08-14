# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, initial_position):
        self.name = name
        self.current_position = initial_position
        self.inventory = []

    def __str__(self):
        return f"\n******* {self.name} is currently in room {self.current_position.name} *******\n"

    def move(self, position):
        if getattr(self.current_position, f'{position}_to'):
            self.current_position = getattr(
                self.current_position, f'{position}_to')
            print(self)
            print(self.current_position)
            self.current_position.get_items()
        else:
            print(
                '\nxxxxxxx You can not go that way. Please enter a valid move. xxxxxxx\n')

    def pick_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None
