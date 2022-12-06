from aoc import AdventOfCode as AOC
AocBot = AOC('4','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
	total = 0

	for line in input:
		fh,sh = line.split(',')
		fh1,fh2 = fh.split('-')
		sh1,sh2 = sh.split('-')
		fh1,fh2,sh1,sh2 = int(fh1),int(fh2),int(sh1),int(sh2)

		if ((len(list(range(fh1,fh2+1))) > len(list(range(sh1,sh2+1)))) and (sh1 >= fh1 and sh2 <= fh2)):
			total += 1
		elif fh1 >= sh1 and fh2 <= sh2:
			total += 1

	if submit: AocBot.submit('1', total)
	else: print(total)
        
def onels():
	print(sum([1 if (len(list(range(fh1,fh2+1))) > len(list(range(sh1,sh2+1)))) and (sh1 >= fh1 and sh2 <= fh2) else 1 if fh1 >= sh1 and fh2 <= sh2 else 0 for fh1,fh2,sh1,sh2 in [(int(t1[0]),int(t1[1]),int(t2[0]),int(t2[1])) for t1,t2 in [((fh.split('-')),(sh.split('-'))) for fh,sh in [line.split(',') for line in input]]]]))
	print(sum([sum(list(set([1 if x in list(range(sh1,sh2+1)) else 0 for x in list(range(fh1,fh2+1))]))) for fh1,fh2,sh1,sh2 in [(int(t1[0]),int(t1[1]),int(t2[0]),int(t2[1])) for t1,t2 in [((fh.split('-')),(sh.split('-'))) for fh,sh in [line.split(',') for line in input]]]]))
	# Check if its > 1, and set to one, use a set to turn into a 1 and a 0

# Part 2
def p2(submit=False):
	total = 0
	for line in input:
		fh,sh = line.split(',')
		fh1,fh2 = fh.split('-')
		sh1,sh2 = sh.split('-')
		fh1,fh2,sh1,sh2 = int(fh1),int(fh2),int(sh1),int(sh2)

		p1 = list(range(fh1,fh2+1))
		p2 = list(range(sh1,sh2+1))

		for x in p1:
			if x in p2:
				total += 1
				break

	if submit: AocBot.submit('2', total)
	else: print(total)

p1(submit=False)
p2(submit=False)
onels()

# Part 1
# 448 Correct