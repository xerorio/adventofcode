# part 1
def part_1():
	rows_og = []

	with open('03.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			rows_og.append(line.strip())

	gamma_rate = ''
	epsilon_rate = ''
	columns = []

	for i in range(12):
		next_column = ''
		for j in range(len(rows_og)):
			next_column += rows_og[j][i]
		columns.append(next_column)

	for n in columns:
		if n.count('0') > 500:
			gamma_rate += '0'
		else:
			gamma_rate += '1'

	for n in columns:
		if n.count('0') > 500:
			epsilon_rate += '1'
		else:
			epsilon_rate += '0'

	print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# part_1()


# part 2
def part_2():
	oxygen_rating = ''
	co2_rating = ''

	rows_og = []

	with open('03.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			rows_og.append(line.strip())

	rows = rows_og.copy()

	for j in range(12):
		num_of_zeros = 0
		num_of_ones = 0
		for i in range(len(rows_og)):
			if rows_og[i][j] == '0':
				num_of_zeros += 1
			else:
				num_of_ones += 1

		if num_of_zeros > num_of_ones:
			rows_og = list(filter(lambda x: x[j] == '0', rows_og))
		else:
			rows_og = list(filter(lambda x: x[j] == '1', rows_og))

		if len(rows_og) == 1:
			break

	oxygen_rating = int(rows_og[0], 2)

	for j in range(12):
		num_of_zeros = 0
		num_of_ones = 0
		for i in range(len(rows)):
			if rows[i][j] == '0':
				num_of_zeros += 1
			else:
				num_of_ones += 1

		if num_of_zeros > num_of_ones:
			rows = list(filter(lambda x: x[j] == '1', rows))
		else:
			rows = list(filter(lambda x: x[j] == '0', rows))

		if len(rows) == 1:
			break

	co2_rating = int(rows[0], 2)

	print(oxygen_rating * co2_rating)

# part_2()