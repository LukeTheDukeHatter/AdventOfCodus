from aoc import AdventOfCode as AOC

AocBot = AOC('1','2022')
input = AocBot.data
print(f"## Day 1 ##*nPart 1: {max([sum([int(l) if l != '' else 0 for l in item.split('*n')]) for item in '*n'.join(input).split('*n*n')])}*nPart 2: {sum(sorted([sum([int(l) if l != '' else 0 for l in item.split('*n')]) for item in '*n'.join(input).split('*n*n')])[-3:])}*n".replace('*n','\n'))

AocBot = AOC('2','2022')
input = AocBot.data
print(f"## Day 2 ##*nPart 1: {sum([({'X':1,'Y':2,'Z':3}[p2]+6) if p2 == {'A':'Y','B':'Z','C':'X'}[p1] else (3+{'X':1,'Y':2,'Z':3}[p2] if p2 == {'A':'X','B':'Y','C':'Z'}[p1] else 0+{'X':1,'Y':2,'Z':3}[p2]) for p1,p2 in [l.split(' ') for l in input]])}*nPart 2: {sum([{'X':1,'Y':2,'Z':3}[{'A':'Z','B':'X','C':'Y'}[p1]] if p2 == 'X' else 3+{'X':1,'Y':2,'Z':3}[{'A':'X','B':'Y','C':'Z'}[p1]] if p2 == 'Y' else 6+{'X':1,'Y':2,'Z':3}[{'A':'Y','B':'Z','C':'X'}[p1]] for p1,p2 in [l.split(' ') for l in input]])}*n".replace('*n','\n'))

AocBot = AOC('3','2022')
input = AocBot.data
print(f"## Day 3 ##*nPart 1: {sum([[((ord(c)-64+26) if ord(c)<93 else (ord(c)-96)) for c in set(line[:len(line)//2]) if c in set(line[len(line)//2:])][0] for line in input])}*nPart 2: {sum([[((ord(c)-64+26) if ord(c)<93 else (ord(c)-96)) for c in set(group[0]) if ( c in set(group[1]) and (c in set(group[2])))][0] for group in [input[i:i+3] for i in range(0, len(input), 3)]])}*n".replace('*n','\n'))

AocBot = AOC('4','2022')
input = AocBot.data
print(f"## Day 4 ##*nPart 1: {sum([1 if (len(list(range(fh1,fh2+1))) > len(list(range(sh1,sh2+1)))) and (sh1 >= fh1 and sh2 <= fh2) else 1 if fh1 >= sh1 and fh2 <= sh2 else 0 for fh1,fh2,sh1,sh2 in [(int(t1[0]),int(t1[1]),int(t2[0]),int(t2[1])) for t1,t2 in [((fh.split('-')),(sh.split('-'))) for fh,sh in [line.split(',') for line in input]]]])}*nPart 2: {sum([sum(list(set([1 if x in list(range(sh1,sh2+1)) else 0 for x in list(range(fh1,fh2+1))]))) for fh1,fh2,sh1,sh2 in [(int(t1[0]),int(t1[1]),int(t2[0]),int(t2[1])) for t1,t2 in [((fh.split('-')),(sh.split('-'))) for fh,sh in [line.split(',') for line in input]]]])}*n".replace('*n','\n'))

AocBot = AOC('5','2022')
input = AocBot.data
print(f"## Day 5 ##*nPart 1: {'' if ((initial := [[c for c in x] for x in ['BSVZGPW','JVBCZF','VLMHNZDC','LDMZPFJB','VFCGJBQH','GFQTSLB','LGCZV','NLG','JFHC']]) == 'Ball' or ['' for x in 'a' if [[initial[int(sp)-1].append(initial[int(fp)-1].pop()) for i in range(int(ct))] for ct,fp,sp in [l.replace('move ','').replace(' from ',':').replace(' to ',':').split(':') for l in input] for runonce in [1]]==0 or True])and False else ''.join([i[-1] for i in initial])}*nPart 2: {'' if ((initial := [[c for c in x] for x in ['BSVZGPW','JVBCZF','VLMHNZDC','LDMZPFJB','VFCGJBQH','GFQTSLB','LGCZV','NLG','JFHC']]) == 'Ball' or ['' for x in 'a' if [[initial[int(sp)-1].append(i) for i in [initial[int(fp)-1].pop() for pp in range(int(ct))][::-1]] for ct,fp,sp in [l.replace('move ','').replace(' from ',':').replace(' to ',':').split(':') for l in input] for runonce in [1]]==0 or True])and False else ''.join([i[-1] for i in initial])}*n".replace('*n','\n'))

AocBot = AOC('6','2022')
input = AocBot.data
print(f"## Day 6 ##*nPart 1: {[i+4 for i in range(len(input)) if len(set(input[i:i+4])) == 4][0]}*nPart 2: {[i+14 for i in range(len(input)) if len(set(input[i:i+14])) == 14][0]}*n".replace('*n','\n'))
