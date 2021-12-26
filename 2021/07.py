# part 1
def part_1():
	with open('07.txt', 'r') as f:
		crab_positions = [int(x) for x in f.read().split(',')]

	fuels = []
	for i in range(len(crab_positions)+1):
		fuel = 0
		for j in crab_positions:
			fuel += abs(j-i)
		fuels.append(fuel)

	print(min(fuels))

# part_1()


# part 2
def part_2():
	with open('07.txt', 'r') as f:
		crab_positions = [int(x) for x in f.read().split(',')]

	fuels = []
	for i in range(len(crab_positions)+1):
		fuel = 0
		for j in crab_positions:
			difference = abs(j-i)
			fuel += ((difference*(difference+1))/2)
		fuels.append(fuel)

	print(min(fuels))

# part_2()