class Item:
    def __init__(self, name, description, value=0):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"** {self.name}: {self.description}. value: {self.value}"

    def on_take(self):
        print(f"\nYou have picked up {self.name}")

    def on_drop(self):
        print(f"\nYou have dropped {self.name}")
