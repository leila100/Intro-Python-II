from items.item import Item


class Treasure_chest(Item):
    def __init__(self, name, description, value=0):
        super().__init__(name, description, value)
        self.value = value
        self.items = []
        self.open = False

    def add_item(self, item):
        self.items.append(item)
        self.value += item.value

    def remove_item(self, item):
        self.items.remove(item)
        self.value -= item.value

    def __str__(self):
        info = "\n"
        for item in self.items:
            info += item.name + "\n"
        return f"** {self.name} has a value of ${self.value}. It contains: " + info

    # if you type take chest, if chest is open, you take all the items in it
    def on_take(self, item):
        if self.open:
            if item in self.items:
                self.remove_item(item)
                print(f"You have picked up: {item.name}")
            else:
                print(f"Sorry, this item {item.name} is not in the chest.")
        else:
            print("Please open the chest first. You need a key to open the chest.")

    def on_drop(self, item):
        if self.open:
            self.remove_item(item)
            print(f"You have added {item.name} to the chest.")
        else:
            print("Please open the chest first. You need a key to open the chest.")

    # if you type open chest, it will try to open it
    def open(self):
        if not self.open:
            print("The chest is now open")
            self.open = True
        else:
            print("The chest is already open.")

    def close(self):
        if self.open:
            print("The chest is now closed")
            self.open = False
        else:
            print("The chest is already closed.")
