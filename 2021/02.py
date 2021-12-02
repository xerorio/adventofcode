# part 1
def part_1():
	instructions = []
	position = [0, 0]

	with open('02.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			instructions.append(line.split(' '))
	
	for instruction in instructions:
		# how much to move by
		move_by = int(instruction[1][:2])
		if instruction[0] == 'forward':
			position[0] += move_by
		elif instruction[0] == 'up':
			position[1] -= move_by
		elif instruction[0] == 'down':
			position[1] += move_by

	print(position[0] * position[1])

# part_1()
# Answer: 1427868


# part 2
def part_2():
	instructions = []
	position = [0, 0]
	aim = 0

	with open('02.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			instructions.append(line.split(' '))
	
	for instruction in instructions:
		move = int(instruction[1][:2])
		if instruction[0] == 'forward':
			position[0] += move
			position[1] += (aim * move)
		elif instruction[0] == 'up':
			aim -= move
		elif instruction[0] == 'down':
			aim += move

	print(position[0] * position[1])

# part_2()
# Answer: 1568138742