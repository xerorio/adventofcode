# part 1
def part_1():
	num_of_increases = 0

	with open('01.txt', 'r') as f:
		file = f.read()
		lines = file.split('\n')

		for i in range(1, len(lines)):
			if int(lines[i]) > int(lines[i-1]):
				num_of_increases += 1
		
		print(num_of_increases)

# part_1()
# Answer: 1154


# part 2
def part_2():
	num_of_increases = 0
	list_of_sums = []

	with open('01.txt', 'r') as f:
		file = f.read()
		lines = file.split('\n')

		for i in range(0, len(lines)-2):
			next_sum = (int(lines[i]))+(int(lines[i+1]))+(int(lines[i+2]))
			list_of_sums.append(next_sum)

		for j in range(1, len(list_of_sums)):
			if int(list_of_sums[j]) > int(list_of_sums[j-1]):
				num_of_increases += 1
		
		print(num_of_increases)

# part_2()
# Answer: 1127