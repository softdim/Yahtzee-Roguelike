from dice import *
from patterns import *

# GameState holds all of the data for the current game
class GameState:
    def __init__(self, ndice=5, patterns = PATTERNS):
        self.ndice = ndice
        self.dice = [Die(self) for _ in range(ndice)]
        self.patterns = patterns
        self.score = 0
    

    def roll(self):
        for die in self.dice:
            if not die.held:
                die.roll()
    
    def update(self):
        self.roll()

    @property
    def values(self):
        return [d.value for d in self.dice]

def main():
    gs = GameState()
    active = False
    while active:
        gs.update()

if __name__ == "__main__":
    main()