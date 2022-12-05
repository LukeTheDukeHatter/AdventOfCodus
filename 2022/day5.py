from aoc import AdventOfCode as AOC
AocBot = AOC('5','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
    initial = {
        1:[x for x in 'BSVZGPW'],
        2:[x for x in 'JVBCZF'],
        3:[x for x in 'VLMHNZDC'],
        4:[x for x in 'LDMZPFJB'],
        5:[x for x in 'VFCGJBQH'],
        6:[x for x in 'GFQTSLB'],
        7:[x for x in 'LGCZV'],
        8:[x for x in 'NLG'],
        9:[x for x in 'JFHC']}
    total = ""
    for line in input:
        count,fp,sp = line.replace('move ','').replace(' from ',':').replace(' to ',':').split(':')
        count,fp,sp = int(count),int(fp),int(sp)
        for i in range(count):
            initial[sp].append(initial[fp].pop())

    for i in range(1,10):
        total += initial[i][-1]

    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    print('' if ((initial := [[c for c in x] for x in ['BSVZGPW','JVBCZF','VLMHNZDC','LDMZPFJB','VFCGJBQH','GFQTSLB','LGCZV','NLG','JFHC']]) == 'Ball' or [print(''.join([i[-1] for i in initial])) for x in 'a' if [[initial[int(sp)-1].append(initial[int(fp)-1].pop()) for i in range(int(ct))] for ct,fp,sp in [l.replace('move ','').replace(' from ',':').replace(' to ',':').split(':') for l in input] for runonce in [1]]==0 or True]) else '',end='')
    print('' if ((initial := [[c for c in x] for x in ['BSVZGPW','JVBCZF','VLMHNZDC','LDMZPFJB','VFCGJBQH','GFQTSLB','LGCZV','NLG','JFHC']]) == 'Ball' or [print(''.join([i[-1] for i in initial])) for x in 'a' if [[initial[int(sp)-1].append(i) for i in [initial[int(fp)-1].pop() for pp in range(count)][::-1]] for ct,fp,sp in [l.replace('move ','').replace(' from ',':').replace(' to ',':').split(':') for l in input] for runonce in [1]]==0 or True]) else '',end='')


    

# Part 2
def p2(submit=False):
    initial = {
        1:[x for x in 'BSVZGPW'],
        2:[x for x in 'JVBCZF'],
        3:[x for x in 'VLMHNZDC'],
        4:[x for x in 'LDMZPFJB'],
        5:[x for x in 'VFCGJBQH'],
        6:[x for x in 'GFQTSLB'],
        7:[x for x in 'LGCZV'],
        8:[x for x in 'NLG'],
        9:[x for x in 'JFHC']
    }
    total = ""
    for line in input:
        count,fp,sp = line.replace('move ','').replace(' from ',':').replace(' to ',':').split(':')
        count,fp,sp = int(count),int(fp),int(sp)
        for i in initial[fp][-count:]:
            initial[sp].append(i)
        for i in range(count):
            initial[fp].pop()

    for i in range(1,10):
        total += initial[i][-1]

    if submit: AocBot.submit('2', total)
    else: print(total)

p1(submit=False)
# p2(submit=False)
onels()
