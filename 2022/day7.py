from aoc import AdventOfCode as AOC

import os


AocBot = AOC('7','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
     total = []
     for line in input:
         if line.startswith('$ cd'):
             total.append(line[2:])
         elif line.startswith('$ ls'):
             continue
         elif line.startswith('dir'):
             total.append('mk'+line)
         else:
             total.append(f"echo \" \" > {line.split(' ')[0]}.txt")

     with open('./Day7FAroundFindOutFolder/runme.sh','w') as f:
         for x in total:
             f.write(x+'\n')


    # [open('./Day7FAroundFindOutFolder/runme.sh','a+').write(x+'\n') for x in [line[2:] if line.startswith('$ cd') else 'mk'+line if line.startswith('dir') else f"echo \" \" > {line.split(' ')[0]}.txt" for line in input if not line.startswith('$ ls')]]
    # lest = [os.path.join(root, file).replace('./Day7FAroundFindOutFolder/','').replace('.txt','') for root,f,file in [(root,first,files) for root,first,files in os.walk(path)] if print(file)]



    #path = './Day7FAroundFindOutFolder'
    #lest = []
    #for root, dirs, files in os.walk(path):
    #    for file in files:
    #        if file.endswith(".txt"):
    #            lest.append(os.path.join(root, file).replace('./Day7FAroundFindOutFolder/','').replace('.txt',''))


    #data = {}
    
    #for x in lest: 
    #    for p in x.split('/')[:-1]:
    #        if p in data: data[p] += int(x.split('/')[-1])
    #        else: data[p] = int(x.split('/')[-1])

    #total = 0

    #for k,v in data.items():
    #    if v <= 100000:
    #        total += v

    #if submit: AocBot.submit('1', total)
    #else: print(total)
        
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

# Solution for part one: 1915606
# Solution for part two: 5025657
