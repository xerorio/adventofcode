# part 1
def part_1():
	houses = set()
	location = complex(0, 0)
	instructions = ''

	with open('03.txt', 'r') as f:
		instructions = f.read()

	for instruction in instructions:
		if instruction == '<':
			location -= complex(1, 0)
		elif instruction == '>':
			location += complex(1, 0)
		elif instruction == '^':
			location += complex(0, 1)
		else:
			location -= complex(0, 1)
		houses.add(location)

	print(len(houses))

part_1()
# Answer: 


# part 2
def part_2():
	pass

# part_2()
# Answer: 