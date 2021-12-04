# part 1
def part_1():
	bingo_numbers = []
	boards = []

	with open('041.txt', 'r') as f:
		bingo_numbers = f.read().split(',')

	with open('042.txt', 'r') as f:
		orginal_boards = f.read().split('\n\n')
		for b in orginal_boards:
			boards.append(list(row.split(' ') for row in b.split('\n')))

	# remove empty strings
	for b in boards:
		for r in b:
			while '' in r:
				r.remove('')

	# keep a record of original board
	boards_og = boards.copy()

	# get columns from boards
	for board in boards:
		cols = []
		for i in range(5):
			c = []
			for r in board:
				c.append(r[i])
			cols.append(c)
		print(cols)

	def solve_board(b: list) -> int:
		counter = 0
		for n in bingo_numbers:
			for row in b:
				if n in row:
					row.remove(n)
					print(row)
					counter += 1
				if row.count('') == 5:
					return counter
			for board in boards:
				cols = []
				for i in range(5):
					c = []
					for r in board:
						c.append(r[i])
					cols.append(c)

	# for b in boards:
	# 	print(f'{b}\n{solve_board(b)}')

part_1()


# part 2
def part_2():
	pass

# part_2()