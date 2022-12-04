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


# Part 1
# 448 Correct