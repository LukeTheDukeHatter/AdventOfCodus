from aoc import AdventOfCode as AOC
AocBot = AOC('8','2022')
input = AocBot.data

# Part 1
def p1(submit=False):
    total = 0
    grid = [[int(x) for x in y] for y in input]

    testgrid = [[{'num':x, 'vis':True} for x in y] for y in input]

    for cy in range(1, len(grid)-1):
        for cx in range(1, len(grid[0])-1):
            yvis = True
            yvisn = True
            xvis = True
            xvisn = True
            
            for dy in range(0,len(grid)):
                if (cy+dy) >= 0 and (cy+dy) < len(grid)-1:
                    if grid[cy+dy][cx] >= grid[cy][cx]:
                        yvis = False

            for dy in range(-len(grid),0):
                if (cy+dy) >= 0 and (cy+dy) < len(grid)-1:
                    if grid[cy+dy][cx] >= grid[cy][cx]:
                        yvisn = False


            for dx in range(0, len(grid[0])):
                if (cx+dx) >= 0 and (cx+dx) < len(grid[0])-1:
                    if grid[cy][cx+dx] >= grid[cy][cx]:
                        xvis = False

            for dx in range(-len(grid[0]),0):
                if (cx+dx) >= 0 and (cx+dx) < len(grid[0])-1:
                    if grid[cy][cx+dx] >= grid[cy][cx]:
                        xvisn = False

            if yvis or yvisn or xvis or xvisn:
                total += 1
            else:
                testgrid[cy][cx]['vis'] = False

        
    for cy in range(len(testgrid)):
        for cx in range(len(testgrid[0])):
            if testgrid[cy][cx]['vis']:
                print("\033[1;31;40m"+testgrid[cy][cx]['num'], end='')
            else:
                print("\033[1;32;40m"+testgrid[cy][cx]['num'], end='')
        print()
            

    total += 2*len(grid) + 2*len(grid[0]) - 4

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

# 9438 High
# 4029 High
# 3929 High
# 1244 Incorrect




from aoc import AdventOfCode as AOC
AocBot = AOC('8','2022')
input = AocBot.data

from collections import namedtuple
class Tree(namedtuple('Tree', 'x y h')): pass

forest = [*map(list,input)]
forest = {(x,y):Tree(x,y,h) for y,row in enumerate(forest) for x,h in enumerate(row)}
H,W = max(forest)

for t in forest.values():
    t.v = (
        all(t.h>forest[x,t.y].h for x in range(0,t.x)) or
        all(t.h>forest[x,t.y].h for x in range(t.x+1,W+1)) or
        all(t.h>forest[t.x,y].h for y in range(0,t.y)) or
        all(t.h>forest[t.x,y].h for y in range(t.y+1,H+1)))
    t.s = (
        next((l for l,y in enumerate(range(0,t.y)[::-1],1) if t.h<=forest[t.x,y].h),t.y) *
        next((l for l,y in enumerate(range(t.y+1,H+1),1) if t.h<=forest[t.x,y].h),H-t.y) *
        next((l for l,x in enumerate(range(0,t.x)[::-1],1) if t.h<=forest[x,t.y].h),t.x) *
        next((l for l,x in enumerate(range(t.x+1,W+1),1) if t.h<=forest[x,t.y].h),W-t.x))

print('part1', sum(t.v for t in forest.values()))
print('part2', max(forest.values(),key=lambda t:t.s).s)