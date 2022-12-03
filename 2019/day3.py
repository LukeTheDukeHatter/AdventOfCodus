from aoc import AdventOfCode as AOC
AocBot = AOC('3','2019')

input = [f for f in AocBot.data]

def manhattan_distance(x1:int, y1:int, x2:int, y2:int) -> int: return (abs(x1 - x2) + abs(y1 - y2))

# Part 1
def p1(submit=False,ansr=False):
    valid = []
    data = {}

    for line in input:
        x,y=0,0
        for instruction in line.split(','):
            if instruction[0] == 'U':
                for i in range(int(instruction[1:])):
                    y+=1
                    if (x,y) not in data:
                        data[(x,y)] = 1
                    else:
                        valid.append((x,y))
                        data[(x,y)] += 1
            elif instruction[0] == 'D':
                for i in range(int(instruction[1:])):
                    y-=1
                    if (x,y) not in data:
                        data[(x,y)] = 1
                    else:
                        valid.append((x,y))
                        data[(x,y)] += 1
            elif instruction[0] == 'R':
                for i in range(int(instruction[1:])):
                    x+=1
                    if (x,y) not in data:
                        data[(x,y)] = 1
                    else:
                        valid.append((x,y))
                        data[(x,y)] += 1
            elif instruction[0] == 'L':
                for i in range(int(instruction[1:])):
                    x-=1
                    if (x,y) not in data:
                        data[(x,y)] = 1
                    else:
                        valid.append((x,y))
                        data[(x,y)] += 1

    dataset = [manhattan_distance(0,0,x,y) for (x,y) in valid]
    ansr = min(dataset)


    if submit: AocBot.submit('1', ansr)
    else: print(ansr)

# Part 2
def p2(submit=False,ansr=False):

    if submit: AocBot.submit('2', ansr)
    else: print(ansr)


p1(submit=False)
p2(submit=False)