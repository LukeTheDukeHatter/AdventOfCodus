from aoc import AdventOfCode as AOC
AocBot = AOC('2','2017')
input = AocBot.data

# Part 1
def p1(submit=False):
	total = 0

	for line in input:
		...

	if submit: AocBot.submit('1', total)
	else: print(total)
    
def onels():
	print(sum([max(i)-min(i) for i in [[int(f) for f in l.split(' ')] for l in input]]))
	print(sum([[pp[0] for pp in [[x//y for y in [int(f) for f in line.split(' ')] if (x % y == 0 and x != y)] for x in [int(f) for f in line.split(' ')]] if pp != []][0] for line in input]))

# Part 2
def p2(submit=False):
	total = 0
	for line in input:
		ln = [int(f) for f in line.split(' ')]

		for x in ln:
			for y in ln:
				if x % y == 0 and x != y:
					total += x // y

		
		
	
	if submit: AocBot.submit('2', total)
	else: print(total)

p1(submit=False)
p2(submit=False)
onels()