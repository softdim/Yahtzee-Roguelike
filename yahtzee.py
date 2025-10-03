from dice import *
from patterns import PATTERNS
from cli import dice_row_str

# GameState holds all of the data for the current game
class GameState:
    def __init__(self, ndice=5, patterns=PATTERNS):
        self.ndice = ndice
        self.dice = [Die(self) for _ in range(ndice)]
        self.patterns = patterns
        self.score = 0
        self.roll_count = 0

    def roll(self):
        for die in self.dice:
            if not die.held:
                die.roll()
        self.roll_count += 1

    @property
    def values(self):
        return [d.value for d in self.dice]

    def reset_holds(self):
        for d in self.dice:
            d.held = False
        self.roll_count = 0


def main():
    gs = GameState()
    rounds = 13  # like Yahtzee
    for r in range(rounds):
        gs.reset_holds()
        print(f"\n--- Round {r+1} ---")

        # Up to 3 rolls
        while gs.roll_count < 3:
            gs.roll()
            print(dice_row_str(gs.values))

            if gs.roll_count == 3:
                break

            action = input("Hold dice? (e.g. '1 3' to hold dice 1 & 3, ENTER to reroll all, 's' to score): ")
            if action.lower() == "s":
                break
            elif action.strip():
                try:
                    hold_idxs = [int(x)-1 for x in action.split()]
                    for i, d in enumerate(gs.dice):
                        d.held = (i in hold_idxs)
                except ValueError:
                    print("Invalid input.")

        # After rolling, pick a scoring pattern
        print("Available patterns:")
        for name, fn in gs.patterns.items():
            score = fn(gs.values)
            print(f" {name:15} -> {score}")

        choice = input("Choose a pattern: ").strip()
        if choice in gs.patterns:
            score = gs.patterns[choice](gs.values)
            gs.score += score
            print(f"Scored {score} on {choice}. Total: {gs.score}")
        else:
            print("Invalid pattern, scoring 0.")

    print(f"\nFinal Score: {gs.score}")


if __name__ == "__main__":
    main()
