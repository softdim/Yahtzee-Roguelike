
# gs = gamestate, vals = list of rolled dice values
def chance(gs, vals):
    return sum(vals)

# ct = number of dice that have to be the same
def same_count(vals, ct):
    maxv = 0
    for v in vals:
        if v > maxv and vals.count(v) >= ct:
            maxv = v
    
    return maxv * ct

def sum_of(vals, val):
    return val * vals.count(val)

def my_house(vals):
    a = vals[0]
    b = None
    for v in vals:
        if v != a:
            b = v

    if not b: return 0

    na, nb = vals.count(a), vals.count(b)
    if (a == 2 and b == 3) or (b == 2 and a == 3):
        return 25

def sequence(vals, minct):
    for i in range(len(vals)):
        ct = 0
        last = vals[i]
        for j in range(i, len(vals)-1):
            if last + 1 == vals[j+1]:
                ct += 1
        if ct >= minct:
            return minct * 10
    return 0
    

# "pattern name": pattern_function
# PATTERNS["pattern name"](gamestate.values)
DATA = {
    "double trouble": {
        "pattern": lambda vals: same_count(vals, 2),
        "hint": "Add up two of the same dice.",
    },
    "a charm": {
        "pattern": lambda vals: same_count(vals, 2),
        "hint": "Add up three of the same dice.",
    },
    "double double": {
        "pattern": lambda vals: same_count(vals, 2),
        "hint": "Add up four of the same dice.",
    },
    "high stakes": {
        "pattern": lambda vals: 50 if vals.count(vals[0]) == len(vals) else 0,
        "hint": "All of the dice are the same for 50 points.",
    },
    "dots": {
        "pattern": lambda vals: sum_of(vals, 1),
        "hint": "Add up your ones.",
    },
    "pairs": {
        "pattern": lambda vals: sum_of(vals, 2),
        "hint": "Add up your twos.",
    },
    "trips": {
        "pattern": lambda vals: sum_of(vals, 3),
        "hint": "Add up your threes.",
    },
    "quads": {
        "pattern": lambda vals: sum_of(vals, 4),
        "hint": "Add up your fours.",
    },
    "quints": {
        "pattern": lambda vals: sum_of(vals, 5),
        "hint": "Add up your fives.",
    },
    "hexes": {
        "pattern": lambda vals: sum_of(vals, 6),
        "hint": "Add up your sixes.",
    },
    "double charm": {
        "pattern": my_house,
        "hint": "Double trouble and a charm for 25 points.",
    },
    "partial sequence": {
        "pattern": lambda vals: sequence(vals, 4),
        "hint": "Four numbers in a sequence for 40 points.",
    },
    "full sequence": {
        "pattern": lambda vals: sequence(vals, 5),
        "hint": "Five numbers in a sequence for 50 points.",
    },
}

PATTERNS = {}
for k, v in DATA.items():
    PATTERNS[k] = v["pattern"]

if __name__ == "__main__":
    print(PATTERNS['double trouble'](None, [2, 3, 2, 4, 4]))