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
        description = ""
        for line in word_list:
            description += line + '\n'
        return description

    def get_items(self):
        items = ""
        for item in self.items:
            items += "* " + item.name + " * "
        return items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None
