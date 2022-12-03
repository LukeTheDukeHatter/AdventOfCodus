from aoc import AdventOfCode as AOC
AocBot = AOC('1','2019')

input = AocBot.data

# Part 1
def p1(submit=False):
    total = 0
    for line in input:
        total += int(line)//3-2
    print(total)
    if submit: AocBot.submit('1', total)

# Part 2
def p2(submit=False):
    total = 0
    for line in input:
        val = int(line)
        while val > 0:
            val = val//3-2
            if val > 0:
                total += val
    print(total)
    if submit: AocBot.submit('2', total)

p1()
p2()