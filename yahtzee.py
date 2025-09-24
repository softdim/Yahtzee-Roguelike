from dice import *
from patterns import *

# GameState holds all of the data for the current game
class GameState:
    # ndice = number of dice
    # patterns = patterns that can be claimed as the game progresses
    def __init__(self, ndice=5, patterns = DEFAULT_PATTERNS):
        self.ndice = ndice
        self.dice = [Die(self) for _ in range(ndice)]
        self.patterns = patterns
        self.score = 0
    
    # rolls all the dice that are not currently held
    def roll(self):
        for die in self.dice:
            if not die.held:
                die.roll()
    
    # run every time after the player takes an action
    def update(self):
        self.roll()

    # gs.values = [dice1.value, ...]
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