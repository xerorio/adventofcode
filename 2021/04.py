# part 1
def part_1():
	from copy import deepcopy

	og = []
	bingo_numbers = []

	with open('041.txt', 'r') as f:
		for i in f.read().split(','):
			bingo_numbers.append(int(i))

	with open('042.txt', 'r') as f:
		og = [b.split('\n') for b in f.read().split('\n\n')]
		for i in range(len(og)):
			for j in range(len(og[i])):
				og[i][j] = list(map(int, og[i][j].split()))
	
	boards = deepcopy(og)

	def win(board):
		if ('', '', '', '', '') in board or ('', '', '', '', '') in list(zip(*board)):
			return True
		return False
	
	winner = []
	latest_num = 0

	num_iterator = iter(bingo_numbers)

	playing = True

	while playing:
		latest_num = next(num_iterator)
		# boards
		for i in range(len(boards)):
			# then go through each row
			for j in range(len(boards[i])):
				# then each number in a row
				for k in range(len(boards[i][j])):
					if boards[i][j][k] == latest_num:
						boards[i][j][k] = ''
			if win(boards[i]):
				winner = boards[i]
				playing = False
				break
	
	unmarked_sum = 0
	for r in winner:
		for n in r:
			if n != '':
				unmarked_sum += n
	
	print(unmarked_sum * latest_num)

# part_1()


# part 2
def part_2():
	from copy import deepcopy

	og = []
	bingo_numbers = []

	with open('041.txt', 'r') as f:
		for i in f.read().split(','):
			bingo_numbers.append(int(i))

	with open('042.txt', 'r') as f:
		og = [b.split('\n') for b in f.read().split('\n\n')]
		for i in range(len(og)):
			for j in range(len(og[i])):
				og[i][j] = list(map(int, og[i][j].split()))
	
	boards = deepcopy(og)

	def win(board):
		if ('', '', '', '', '') in board or ('', '', '', '', '') in list(zip(*board)):
			return True
		return False
	
	loser = []
	latest_num = 0

	num_iterator = iter(bingo_numbers)

	playing = True

	while playing:
		try:
			number = next(num_iterator)
		except:
			break
		# boards
		for i in range(len(boards)):
			# then go through each row
			for j in range(len(boards[i])):
				# then each number in a row
				for k in range(len(boards[i][j])):
					if boards[i][j][k] == number:
						boards[i][j][k] = ''
		for i in range(len(boards)):
			if not win(boards[i]):
				playing = True
				loser = boards[i]
				break
			else:
				playing = False
	
	unmarked_sum = 0
	for r in loser:
		for n in r:
			if n != '':
				unmarked_sum += n
	print(loser)
	print(unmarked_sum * latest_num)

# part_2()