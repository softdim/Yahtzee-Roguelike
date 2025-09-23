
def same_count(vals, ct=2):
    maxv = 0
    for v in vals:
        if v > maxv and vals.count(v) >= ct:
            maxv = v
    
    return maxv * ct

DEFAULT_PATTERNS = {
    "double trouble": lambda _gs, vals: same_count(vals, 2),
    "three-way": lambda _gs, vals: same_count(vals, 3),
    "double double": lambda _gs, vals: same_count(vals, 4),
    "yahtzee": lambda _gs, vals: same_count(vals, 5),
}