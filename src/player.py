# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_position):
        self.name = name
        self.current_position = current_position
        self.inventory = []

    def __str__(self):
        return f"******* {self.name} is currently in room {self.current_position.name} *******"

    def pick_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None
