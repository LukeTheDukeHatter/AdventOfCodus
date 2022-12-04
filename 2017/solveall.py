from aoc import AdventOfCode as AOC






# Day 1
AocBot = AOC('1','2017')
input = AocBot.data

def d1p1(): return sum([int(input[i]) for i in range(len(input)) if input[i] == input[(i+1)%len(input)]])
def d1p2(): return sum([int(input[i]) for i in range(len(input)) if input[i] == input[(i+(len(input)//2))%len(input)]])

AocBot.submit('1',d1p1())
AocBot.submit('2',d1p2())

# Day 2
AocBot = AOC('2','2017')
input = AocBot.data

def d2p1(): return sum([max(i)-min(i) for i in [[int(f) for f in l.split(' ')] for l in input]])
def d2p2(): return sum([[p[0] for p in [[x//y for y in [int(f) for f in line.split(' ')] if (x % y == 0 and x != y)] for x in [int(f) for f in line.split(' ')]] if p != []][0] for line in input])

AocBot.submit('1',d2p1())
AocBot.submit('2',d2p2())

# Day 3

AocBot = AOC('3','2017')
input = AocBot.data

AocBot.submit('1',)
AocBot.submit('2',)