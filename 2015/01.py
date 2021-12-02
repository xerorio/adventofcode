# part 1
def part_1():
	floor = 0
	file = ''

	with open('01.txt', 'r') as f:
		file = f.read()

	for character in file:
		if character == '(':
			floor += 1
		elif character == ')':
			floor -= 1

	print(floor)

# part_1()
# Answer: 232


# part 2
def part_2():
	floor = 0
	file = ''

	with open('01.txt', 'r') as f:
		file = f.read()

	for i in range(0, len(file)):
		if file[i] == '(':
			floor += 1
		elif file[i] == ')':
			floor -= 1

		if floor == -1:
			print(i + 1)
			return

# part_2()
# Answer: 1783