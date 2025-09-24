DICE_STR = r'''
.-------.
|       |
|       |
|       |
'-------'
.-------.
|       |
|   O   |
|       |
'-------'
.-------.
| O     |
|       |
|     O |
'-------'
.-------.
| O     |
|   O   |
|     O |
'-------'
.-------.
| O   O |
|       |
| O   O |
'-------'
.-------.
| O   O |
|   O   |
| O   O |
'-------'
.-------.
| O   O |
| O   O |
| O   O |
'-------'
.-------.
| O   O |
| O O O |
| O   O |
'-------'
.-------.
| O O O |
| O   O |
| O O O |
'-------'
.-------.
| O O O |
| O O O |
| O O O |
'-------'
'''[1:-1].split('\n')

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


if __name__ == "__main__":
    from dice import *

    items = [
        (str(randint(0, 1000)), str(randint(0, 100000))) for _ in range(100)
    ]

    print(gen_table(items, 4, 15))