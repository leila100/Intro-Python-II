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

    def action(self, verb, item):
        if verb == "take":
            # Check if room contains the item
            take_item = self.current_position.get_item(item)
            if take_item:
                # If item exists i the room
                # Add item to inventory
                self.pick_item(take_item)
                # remove item from room
                self.current_position.remove_item(take_item)
                print(f"\n{self.name} added {take_item.name} to their inventory.")
            else:
                # if item is not in the room
                print("\nSorry, this item is not in the room.")
        elif verb == "drop":
            # Check that the player has the item in the inventory
            drop_item = self.get_item(item)
            if drop_item:
                # if item is in inventory
                # Remove item from inventory
                self.drop_item(drop_item)
                # Add item to room
                self.current_position.add_item(drop_item)
                print(
                    f"\n{self.name} removed {drop_item.name} from their inventory.")
            else:
                # if item not in inventory
                print("\nSorry, this item is not in the inventory.")
        else:
            print(
                "xxxxxxx Please enter one of the valid options (take or drop) xxxxxxx")
