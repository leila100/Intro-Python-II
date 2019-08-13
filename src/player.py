# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_position):
        self.name = name
        self.current_position = current_position

    def __str__(self):
        return f"******* {self.name} is currently in room {self.current_position.name}"
