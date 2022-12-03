from aoc import AdventOfCode as AOC
AocBot = AOC('1','2022')

input = AocBot.data

# Part 1
def p1(submit=False):
    data = [0 for i in range(AocBot.data.count('')+1)]
    data.append(0)
    index = 0
    for line in input:
        if line == '':
            index += 1
            continue
        data[index] += int(line)


    total = max(data)
    if submit: AocBot.submit('1', total)
    else: print(total)
        

# Part 2
def p2(submit=False):

    data = [0 for i in range(AocBot.data.count('')+1)]
    index = 0
    for line in input:
        if line == '':
            index += 1
            continue
        data[index] += int(line)


    total = sum(sorted(data)[-3:])
    if submit: AocBot.submit('2', total)
    else: print(total)

# p1(submit=False)
p2()




