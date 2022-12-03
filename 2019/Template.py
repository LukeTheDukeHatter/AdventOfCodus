from aoc import AdventOfCode as AOC
AocBot = AOC('','2019')

input = [f for f in AocBot.data]


# Part 1
def p1(submit=False,ansr=False):


    if submit: AocBot.submit('1', ansr)
    else: print(ansr)

# Part 2
def p2(submit=False,ansr=False):

   
    if submit: AocBot.submit('2', ansr)
    else: print(ansr)


p1(submit=False)
p2(submit=False)