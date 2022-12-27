stacks = ['BSVZGPW', 'JVBCZF', 'VLMHNZDC', 'LDMZPFJB', 'VFCGJBQH', 'GFQTSLB', 'LGCZV', 'NLG', 'JFHC']

# part 1

# instruction format: [number of boxes to move, from this stack (1), to this stack (2)]
def part_1_move_boxes(s, instruction):
    for i in range(instruction[0]):
        s[instruction[2] - 1] += s[instruction[1] - 1][-1]
        s[instruction[1] - 1] = s[instruction[1] - 2][:-1]

def part_1():
    instructions = []
    with open('05.txt', 'r') as f:
        puzzle_input = f.readlines()
        for i in range(10, len(puzzle_input)):
            next_instruction = puzzle_input[i].strip('\n').split(' ')
            instructions.append([int(next_instruction[1]), int(next_instruction[3]), int(next_instruction[5])])
    for i in instructions:
        part_1_move_boxes(stacks, i)
    output = ''
    for i in range(1, 10):
        output += stacks[i][-1]
    print(output)

# part_1()


# part 2

# instruction format: [number of boxes to move, from this stack (1), to this stack (2)]
def part_2_move_boxes(s, instruction):
    s[instruction[2] - 1] += s[instruction[1] - 1][-instruction[0]:]
    s[instruction[1] - 1] = s[instruction[1] - 1][:-instruction[0]]

def part_2():
    instructions = []
    with open('05.txt', 'r') as f:
        puzzle_input = f.readlines()
        for i in range(10, len(puzzle_input)):
            next_instruction = puzzle_input[i].strip('\n').split(' ')
            instructions.append([int(next_instruction[1]), int(next_instruction[3]), int(next_instruction[5])])
    for i in instructions:
        part_2_move_boxes(stacks, i)
    output = ''
    for i in range(9):
        output += stacks[i][-1]
    print(output)

# part_2()
