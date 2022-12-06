from aoc import AdventOfCode as AOC
AocBot = AOC('6','2022')
line = AocBot.data

# Part 1
def p1(submit=False):
    total = 0
    for i in range(len(line)):
        if len(set(line[i:i+4])) == 4:
            total = i + 4 # Accounts for 0 index, and should be checking index of last character in 4 char string
            break
                

    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    print([i+4 for i in range(len(line)) if len(set(line[i:i+4])) == 4][0])
    print([i+14 for i in range(len(line)) if len(set(line[i:i+14])) == 14][0])
    ...
# Part 2
def p2(submit=False):
    total = 0
    for i in range(len(line)):
        if len(set(line[i:i+14])) == 14:
            total = i + 14 # Accounts for 0 index, and should be checking index of last character in 4 char string
            break

    if submit: AocBot.submit('2', total)
    else: print(total)

p1(submit=False)
p2(submit=False)
onels()