from aoc import AdventOfCode as AOC
AocBot = AOC('1','2017')
input = AocBot.data

# Part 1
def p1(submit=False):
    total = 0


    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            total += int(input[i])
        
    if input[-1] == input[0]:
        total += int(input[0])

    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    print(sum([int(input[i]) for i in range(len(input)) if input[i] == input[(i+1)%len(input)]]))
    print(sum([int(input[i]) for i in range(len(input)) if input[i] == input[(i+(len(input)//2))%len(input)]]))

# Part 2
def p2(submit=False):
    total = 0
    for line in input:
        ...

    if submit: AocBot.submit('2', total)
    else: print(total)

p1(submit=False)
p2(submit=False)
onels()