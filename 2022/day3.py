from aoc import AdventOfCode as AOC
AocBot = AOC('3','2022')
input = AocBot.data

# 97,122,65,90
# sl,su ,ul,uu

# Part 1
def p1(submit=False):
    total = 0

    for line in input:
        fp,sp = set(line[:len(line)//2]), set(line[len(line)//2:]) # First half, second half
        for c in fp: # for char in first half
            if c in sp: # is the char in the second half
                if ord(c) < 93: # is the char uppercase
                    total += ((ord(c) - 64) + 26) # Uppercase characters
                else:
                    total += (ord(c) - 96) # lowercase characters

    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    print(sum([[((ord(c)-64+26) if ord(c)<93 else (ord(c)-96)) for c in set(line[:len(line)//2]) if c in set(line[len(line)//2:])][0] for line in input]))
    print(sum([[((ord(c)-64+26) if ord(c)<93 else (ord(c)-96)) for c in set(group[0]) if ( c in set(group[1]) and (c in set(group[2])))][0] for group in [input[i:i+3] for i in range(0, len(input), 3)]]))

# Part 2
def p2(submit=False):
    total = 0
    group = []

    for line in input:
        group.append(line)
        if len(group) == 3:
            for c in set(group[0]):
                if (c in set(group[1])) and (c in set(group[2])):
                    if ord(c) < 93:
                        total += ((ord(c) - 64) + 26)
                    else:
                        total += (ord(c) - 96)
            group = []

    if submit: AocBot.submit('2', total)
    else: print(total)

p1(submit=False)
p2(submit=False)

onels()