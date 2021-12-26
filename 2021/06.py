# part 1
def part_1():
	with open('06.txt', 'r') as f:
		init_fishes = [int(x) for x in f.read().split(',')]

	def simulate_day(fishys):
		new_fishys = fishys.copy()
		counter = 0
		for i in range(len(new_fishys)):
			if new_fishys[i] != 0:
				new_fishys[i] -= 1
			else:
				new_fishys[i] = 6
				counter += 1
		for i in range(counter):
			new_fishys.append(8)
		return new_fishys

	latest_day = simulate_day(init_fishes)
	for _ in range(79): # iterate for 79 days, first one is done above
		if _ != 79:
			latest_day = simulate_day(latest_day)
	print(len(latest_day))

# part_1()


# part 2
def part_2():
	with open('06.txt', 'r') as f:
		initial_fishys = [int(x) for x in f.read().split(',')]

	todays_fish = {
		'0': 0,
		'1': 0,
		'2': 0,
		'3': 0,
		'4': 0,
		'5': 0,
		'6': 0,
		'7': 0,
		'8': 0
	}

	def simulate_day(fishys):
		next_day = {
			'0': fishys['1'],
			'1': fishys['2'],
			'2': fishys['3'],
			'3': fishys['4'],
			'4': fishys['5'],
			'5': fishys['6'],
			'6': fishys['7'] + fishys['0'],
			'7': fishys['8'],
			'8': fishys['0']
		}
		return next_day

	# first day
	for i in range(9):
		todays_fish[f'{i}'] = initial_fishys.count(i)

	latest_day = simulate_day(todays_fish)
	for _ in range(255): # iterate for 255 days, first one is done above
		if _ != 255:
			latest_day = simulate_day(latest_day)
	
	print(sum(latest_day.values()))

# part_2()