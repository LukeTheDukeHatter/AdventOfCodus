puzzle_input = 289326

def calculate_spiral_memory_value(puzzle_input):
    # Initialize the spiral memory with the first value
    spiral_memory = [[1]]

    # initialize the row and column to 0
    row = 0
    col = 0

    # Initialize the current number to 1
    current_number = 1

    # Initialize the number of steps to 0
    num_steps = 0

    while (current_number <= puzzle_input):
        # Calculate the next row and column
        if row == 0 and col == 0:
            row = 0
            col = 1
            num_steps = 1
        elif row == 0 and col == num_steps:
            row = num_steps
            col = num_steps
        elif row == num_steps and col == num_steps:
            col = num_steps - 1
        elif row == num_steps and col == num_steps - 1:
            row = num_steps - 1
        elif row == num_steps - 1 and col == num_steps - 1:
            col = 0
            num_steps += 1
        elif row == num_steps - 1 and col == 0:
            row = 0

        # Calculate the value for the current cell
        value = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i >= 0 and col + j >= 0 and row + i < len(spiral_memory) and col + j < len(spiral_memory[row + i]):
                    value += spiral_memory[row + i][col + j]

        # Append the value to the spiral memory
        if col == 0:
            spiral_memory.append([value])
        else:
            spiral_memory[row].append(value)

        # Increment the current number
        current_number = value

    # Calculate the distance from the cell to the access port
    distance = abs(row - 0) + abs(col - 0)

    return distance

# Get the distance from the cell to the access port
distance = calculate_spiral_memory_value(puzzle_input)

# Print the result
print(f"The number of steps required to carry the data from the square {puzzle_input} to the access port is {distance}.")