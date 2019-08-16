# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def __str__(self):
        wrapper = textwrap.TextWrapper(width=50)
        word_list = wrapper.wrap(text=self.description)
        description = f"  "
        for line in word_list:
            description += line + '\n'
        return description

    def get_moves(self):
        valid_moves = []
        if self.n_to:
            valid_moves.append('[n - to move North]')
        if self.s_to:
            valid_moves.append('[s - to move South]')
        if self.e_to:
            valid_moves.append('[e - to move East]')
        if self.w_to:
            valid_moves.append('[w - to move West]')
        return valid_moves

    def get_items(self):
        if self.items:
            print(
                f"The items available in {self.name} are: \n")
            for item in self.items:
                print(item)
        else:
            print(f"There are no items in the room {self.name}.\n")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None
