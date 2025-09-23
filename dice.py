from random import randint, choice

# rolls a dice of n sides
def roll(n):
    return randint(1, n)

# base die class, all dice inherit from this one
class Die:
    # gs = gamestate, sides = number of sides on the dice
    def __init__(self, gs, sides = 6):
        self.gs = gs
        self.sides = sides
        
        # if held it will not roll
        self.held = False

        # rolled value
        self.value = None
    
    def roll(self):
        self.value = roll(self.sides)

# always rolls 1
class SnakeEyes(Die):
    def roll(self):
        self.value = 1

# regular die with 20 sides
class D20(Die):
    def __init__(self, gs):
        super().__init__(gs, 20)
