from aoc import AdventOfCode as AOC
AocBot = AOC('1','2022')

input = AocBot.data

# Part 1
def p1(submit=False):
    data = [0 for i in range(AocBot.data.count('')+1)]
    data.append(0)
    index = 0
    for line in input:
        if line == '':
            index += 1
            continue
        data[index] += int(line)


    total = max(data)
    if submit: AocBot.submit('1', total)
    else: print(total)
        
def onels():
    print(max([sum([int(l) if l != '' else 0 for l in item.split('\n')]) for item in '\n'.join(input).split('\n\n')]))
    print(sum(sorted([sum([int(l) if l != '' else 0 for l in item.split('\n')]) for item in '\n'.join(input).split('\n\n')])[-3:]))

# Part 2
def p2(submit=False):

    data = [0 for i in range(AocBot.data.count('')+1)]
    index = 0
    for line in input:
        if line == '':
            index += 1
            continue
        data[index] += int(line)


    total = sum(sorted(data)[-3:])
    if submit: AocBot.submit('2', total)
    else: print(total)


def p1(submit=False):
    calories = [[]]

    # Read the input
    for line in input:
        try:
            if line == "":
                # If we encounter a blank line, start a new list for the next Elf
                calories.append([])
            else:
                # Add the number of calories for the current Elf
                calories[-1].append(int(line))
        except EOFError:
            # Stop reading input when we reach the end of the file
            break

    # Calculate the total calories for each Elf
    elf_calories = [sum(elf) for elf in calories]

    # Find the Elf with the most calories
    most_calories = max(elf_calories)

    # Print the result
    print(most_calories)


p1(submit=False)
p2(submit=False)
onels()





