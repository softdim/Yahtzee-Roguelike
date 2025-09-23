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

def dice_row_str(ns):
    s = ""
    strs = [gen_dice_str(n) for n in ns]
    for y in range(5):
        for x in range(len(ns)):
            part = strs[x][y]
            s += part
        s += '\n'
    
    return s
    

if __name__ == "__main__":
    print(dice_row_str([0, 1, 5, 27]))