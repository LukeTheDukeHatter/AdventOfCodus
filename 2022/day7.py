from aoc import AdventOfCode as AOC

import os


AocBot = AOC('7','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
    # total = []
    # for line in input:
    #     if line.startswith('$ cd'):
    #         total.append(line[2:])
    #     elif line.startswith('$ ls'):
    #         continue
    #     elif line.startswith('dir'):
    #         total.append('mk'+line)
    #     else:
    #         total.append(f"echo \" \" > {line.split(' ')[0]}.txt")

    # with open('./Day7FAroundFindOutFolder/runme.sh','w') as f:
    #     for x in total:
    #         f.write(x+'\n')

    total = 0

    for root,dirs,files in os.walk('/Day7FAroundFindOutFolder'):
        for file in files:
            if file.endswith('.txt'):
                total += int(file.split('.')[0])
                
    


    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    ...

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