from aoc import AdventOfCode as AOC
AocBot = AOC('2','2022')
input = AocBot.data

Defeat = {'A':'Y','B':'Z','C':'X'}
Draw = {'A':'X','B':'Y','C':'Z'}
Win = {'A':'Z','B':'X','C':'Y'}
Scores = {'X':1,'Y':2,'Z':3}

# Part 1
def p1(submit=False):
    total = 0

    for line in input:
        p1,p2 = line.split(' ')
        if p2 == Defeat[p1]:
            total += 6
        elif p2 == Draw[p1]:
            total += 3
        else:
            total += 0
        total += Scores[p2]

    if submit: AocBot.submit('1', total)
    else: print(total)

def onels(): 
    print(sum([({'X':1,'Y':2,'Z':3}[p2]+6) if p2 == {'A':'Y','B':'Z','C':'X'}[p1] else (3+{'X':1,'Y':2,'Z':3}[p2] if p2 == {'A':'X','B':'Y','C':'Z'}[p1] else 0+{'X':1,'Y':2,'Z':3}[p2]) for p1,p2 in [l.split(' ') for l in input]]))
    print(sum([{'X':1,'Y':2,'Z':3}[{'A':'Z','B':'X','C':'Y'}[p1]] if p2 == 'X' else 3+{'X':1,'Y':2,'Z':3}[{'A':'X','B':'Y','C':'Z'}[p1]] if p2 == 'Y' else 6+{'X':1,'Y':2,'Z':3}[{'A':'Y','B':'Z','C':'X'}[p1]] for p1,p2 in [l.split(' ') for l in input]]))
    

# Part 2
def p2(submit=False):
    total = 0
    for line in input:
        p1,p2 = line.split(' ')
        if p2 == 'X':
            total += Scores[Win[p1]]
        elif p2 == 'Y':
            total += 3
            total += Scores[Draw[p1]]
        else:
            total += 6
            total += Scores[Defeat[p1]]

    if submit: AocBot.submit('2', total)
    else: print(total)

# p1(submit=False
# p2(submit=False)
onels()