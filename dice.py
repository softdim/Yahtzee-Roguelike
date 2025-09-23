from random import randint, choice

# rolls a dice of n sides
def roll(n):
    return randint(1, n)

class Die:
    def __init__(self, gs, sides = 6):
        self.gs = gs
        self.sides = sides
        self.held = False
        self.value = None

    def roll(self):
        self.value = roll(self.sides)

class SnakeEyes(Die):
    def roll(self):
        self.value = 1

class Doubles(Die):
    def roll(self):
        super().roll()
        choice(self.gs.dice).value = self.value