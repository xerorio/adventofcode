# part 1
def part_1():
	houses = set()
	location = complex(0, 0)
	instructions = ''

	with open('03.txt', 'r') as f:
		instructions = f.read()

	for instructions[i] in instructions:
		if instructions[i] == '<':
			location -= complex(1, 0)
		elif instructions[i] == '>':
			location += complex(1, 0)
		elif instructions[i] == '^':
			location += complex(0, 1)
		else:
			location -= complex(0, 1)
		houses.add(location)

	print(len(houses))

# part_1()


# part 2
def part_2():
	houses = set()
	santa_location = complex(0, 0)
	robo_santa_location = complex(0, 0)
	instructions = ''

	with open('03.txt', 'r') as f:
		instructions = f.read()

	for i in range(0, len(instructions), 2):
		if instructions[i] == '<':
			santa_location -= complex(1, 0)
		elif instructions[i] == '>':
			santa_location += complex(1, 0)
		elif instructions[i] == '^':
			santa_location += complex(0, 1)
		else:
			santa_location -= complex(0, 1)
		houses.add(santa_location)
	for i in range(1, len(instructions), 2):
		if instructions[i] == '<':
			robo_santa_location -= complex(1, 0)
		elif instructions[i] == '>':
			robo_santa_location += complex(1, 0)
		elif instructions[i] == '^':
			robo_santa_location += complex(0, 1)
		else:
			robo_santa_location -= complex(0, 1)
		houses.add(robo_santa_location)

	print(len(houses))

# part_2()