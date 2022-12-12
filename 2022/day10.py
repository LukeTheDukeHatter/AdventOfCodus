from aoc import AdventOfCode as AOC
AocBot = AOC('10','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
    total = {20:0,60:0,100:0,140:0,180:0,220:0}
    cycles = 0
    regx = 1
    tocheck = [20,60,100,140,180,220]

    for line in input:

        if line == 'noop':
            cycles += 1
            if cycles in tocheck: total[cycles] = regx * cycles

        elif line.startswith('addx'):
            cycles += 1
            if cycles in tocheck: total[cycles] = regx * cycles            
            cycles += 1
            if cycles in tocheck: total[cycles] = regx * cycles
            regx += int(line.split(' ')[-1])

    total = sum(list(total.values()))
    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    ...
    
# Part 2
def p2(submit=False):
    total = ''
    cycles = 0
    regx = 1
    crtscreen =[]

    for line in input:
        crtscreen.append('#' if (cycles%40==regx-1 or cycles%40==regx or cycles%40==regx+1) else '.')

        if line == 'noop':
            cycles += 1
        elif line.startswith('addx'):
            cycles += 1
            crtscreen.append('#' if (cycles%40==regx-1 or cycles%40==regx or cycles%40==regx+1) else '.')
            cycles += 1
            regx += int(line.split(' ')[-1])

    for i in range(0,len(crtscreen),40): print(''.join(crtscreen[i:i+40]))
    if submit: AocBot.submit('2', total)
    else: print(total)

p1(submit=False)
p2(submit=False)
onels()