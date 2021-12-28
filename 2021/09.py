# part 1
def part_1():
	numbers = []

	with open('09.txt', 'r') as f:
		numbers_r = [x.strip() for x in f.readlines()]
		for i in range(len(numbers_r)):
			row = []
			for n in numbers_r[i]:
				row.append(int(n))
			numbers.append(row)

	row_length_index = len(numbers[0]) - 1
	num_rows_index = len(numbers) - 1
	counter = 0

	for y in range(num_rows_index + 1):
		for x in range(row_length_index + 1):
			if numbers[y][x] == 9: # if the number is nine, it can't be less than others around it
				pass
			elif y == 0 and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y+1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y == num_rows_index and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y == 0 and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y == num_rows_index and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y == 0 and x != 0 and x != row_length_index:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y == num_rows_index and x != 0 and x != row_length_index:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y != 0 and y != num_rows_index and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1
			elif y != 0 and y != num_rows_index and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1
			else: # middle of the grid, not edges or corners
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					counter += numbers[y][x]
					counter += 1

	print(counter)

# part_1()


# part 2
def part_2():
	numbers = []

	with open('09eg.txt', 'r') as f:
		numbers_r = [x.strip() for x in f.readlines()]
		for i in range(len(numbers_r)):
			row = []
			for n in numbers_r[i]:
				row.append(int(n))
			numbers.append(row)

	row_length_index = len(numbers[0]) - 1
	num_rows_index = len(numbers) - 1
	low_points = []

	# calculate low points
	for y in range(num_rows_index + 1):
		for x in range(row_length_index + 1):
			if numbers[y][x] == 9: # if the number is nine, it can't be less than others around it
				pass
			elif y == 0 and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y+1][x]:
					low_points.append((y, x))
			elif y == num_rows_index and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))
			elif y == 0 and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x]:
					low_points.append((y, x))
			elif y == num_rows_index and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))
			elif y == 0 and x != 0 and x != row_length_index:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x]:
					low_points.append((y, x))
			elif y == num_rows_index and x != 0 and x != row_length_index:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))
			elif y != 0 and y != num_rows_index and x == 0:
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))
			elif y != 0 and y != num_rows_index and x == row_length_index:
				if numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))
			else: # middle of the grid, not edges or corners
				if numbers[y][x] < numbers[y][x+1] and numbers[y][x] < numbers[y][x-1] and numbers[y][x] < numbers[y+1][x] and numbers[y][x] < numbers[y-1][x]:
					low_points.append((y, x))

	print(low_points)

part_2()