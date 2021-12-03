# part 1
def part_1():
	dimensions = []
	total_square_feet = 0

	with open('02.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			dimensions.append(list(map(int, line.strip().split('x'))))

	for box in dimensions:
		box_paper = 0
		box_paper += (2 * box[0] * box[1])
		box_paper += (2 * box[0] * box[2])
		box_paper += (2 * box[1] * box[2])

		if max(box) == box[0]:
			box_paper += (box[1] * box[2])
		elif max(box) == box[1]:
			box_paper += (box[0] * box[2])
		else:
			box_paper += (box[0] * box[1])

		total_square_feet += box_paper

	print(total_square_feet)

# part_1()


# part 2
def part_2():
	dimensions = []
	ribbon = []
	total_square_feet = 0

	with open('02.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			dimensions.append(list(map(int, line.strip().split('x'))))

	for box in dimensions:
		ribbon_length = 0

		if max(box) == box[0]:
			ribbon_length += (2 * box[1]) + (2 * box[2])
		elif max(box) == box[1]:
			ribbon_length += (2 * box[0]) + (2 * box[2])
		else:
			ribbon_length += (2 * box[0]) + (2 * box[1])

		volume = box[0] * box[1] * box[2]

		total_square_feet += ribbon_length + volume

	print(total_square_feet)

# part_2()