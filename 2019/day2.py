from aoc import AdventOfCode as AOC
AocBot = AOC('2','2019')


# Part 1
def p1(submit=False):

    input = [int(f) for f in AocBot.data[0].split(',')]
    input[1] = 12
    input[2] = 2

    for i in range(0, len(input), 4):
        if input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
        elif input[i] == 99:
            break
    
    ansr = input[0]
    if submit: AocBot.submit('1', ansr)
    else: print(ansr)



# Part 2
def p2(submit=False,ansr=False):

    for x in range(100):
        for y in range(100):
            input = [int(f) for f in AocBot.data[0].split(',')]
            input[1] = x
            input[2] = y

            for i in range(0, len(input), 4):
                if input[i] == 1:
                    input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
                elif input[i] == 2:
                    input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
                elif input[i] == 99:
                    break

            if input[0] == 19690720:
                ansr = 100 * x + y
            
            if ansr: break
        if ansr: break

    if submit: AocBot.submit('2', ansr)
    else: print(ansr)

p1(submit=False)
p2(submit=False)