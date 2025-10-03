DICE_STR = [l.strip() for l in open("dice_faces.txt").readlines()]

DICE_STRS = {}
for i in range(10):
    DICE_STRS[i] = DICE_STR[i*5:i*5+5]

def gen_dice_str(n):
    # check 
    s = DICE_STRS.get(n)
    if s: return s
    
    # top rows
    s = ".-------.\n|       |\n|"
    nstr = str(n)
    assert len(nstr) <= 7

    # number of spaces total
    nsp = 7 - len(nstr)
    # left spaces
    nlsp = nsp//2
    # right spaces
    nrsp = nsp - nlsp

    # |<insert left spaces><number><right spaces>|
    s += ' '*nlsp + nstr + ' '*nrsp
    s += "|\n|       |\n'-------'"
    return s.split('\n')

# ns = [dice1.value, dice2.value, ...]
def dice_row_str(ns:list):
    s = " "
    # generate all of the the dice
    strs = [gen_dice_str(n) for n in ns]
    for y in range(5):
        for x in range(len(ns)):
            part = strs[x][y] + ' '
            s += part
        s += '\n '
    
    return s[:-2]

def gen_held_str(held:list):
    s = ""
    i = 0
    for h in held:
        i += 1
        buff = "##" if h else ".."
        s += f"  {buff}[{i}]{buff} "
    return s

def gen_table(items, ncol, colw, rowNDigits=2):
    s = ""

    # print the top row letters
    s += " "*rowNDigits + " | "
    underline = ""
    for i in range(ncol):
        s += chr(ord('A') + i) + ' '*colw
        underline += '-' * colw
        if i != ncol - 1:
            s += '| '
            underline += '-+-'
    s += '\n'+'-'*rowNDigits+'-+-' + underline + '\n'

    i = 0
    y = 1
    
    while i < len(items):
        # row number
        rowNum = str(y)
        rowNum = " " * (rowNDigits - len(rowNum)) + rowNum
        s += rowNum + ' | '
        for x in range(ncol):
            if i >= len(items):
                break

            item = items[i]
            part1, part2 = item
            nsp = colw - len(part1) - len(part2)
            s += part1 + '.' * nsp + part2
            if x != ncol - 1:
                s += ' | '
            i += 1
        s += '\n'
        y += 1
    
    return s

# takes in A1 and outputs 0
def xy_to_idx(x:str, y:str, ncol):
    u = ord(x.upper()) - ord('A')
    v = int(y) - 1
    return v * ncol + u

if __name__ == "__main__":
    from dice import *
    from patterns import DATA

    items = [
        (key.upper(), str(randint(0, 27))) for key in DATA.keys()
    ]
    print(items)

    print(gen_table(items, 3, 40))
    print(dice_row_str([1, 2, 3, 4, 5]))
    print(gen_held_str([True, False, True, True, False]))