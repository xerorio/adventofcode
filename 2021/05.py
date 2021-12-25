# part 1
def part_1():
	grid = [['.' for i in range(1000)] for i in range(1000)]
	data = []
	coords = []

	with open('05.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			data.append(line.strip().split(' -> '))
		for n in data:
			next_coord = []
			for c in n:
				next_coord.append(c.split(','))
			coords.append(next_coord)

	for coord in coords:
		if coord[0][0] == coord[1][0]: # if x coordinates are equal
			x = int(coord[0][0])
			y1 = int(coord[0][1])
			y2 = int(coord[1][1])
			if y1 > y2:
				for j in range(y2, y1+1):
					if grid[j][x] == '.':
						grid[j][x] = '1'
					else:
						grid[j][x] = str(int(grid[j][x]) + 1)
			else: # y2 is bigger than y1
				for j in range(y1, y2+1):
					if grid[j][x] == '.':
						grid[j][x] = '1'
					else:
						grid[j][x] = str(int(grid[j][x]) + 1)
		if coord[0][1] == coord[1][1]: # if y coordinates are equal
			y = int(coord[0][1])
			x1 = int(coord[0][0])
			x2 = int(coord[1][0])
			if x1 > x2:
				for j in range(x2, x1+1):
					if grid[y][j] == '.':
						grid[y][j] = '1'
					else:
						grid[y][j] = str(int(grid[y][j]) + 1)
			else: # y2 is bigger than y1
				for j in range(x1, x2+1):
					if grid[y][j] == '.':
						grid[y][j] = '1'
					else:
						grid[y][j] = str(int(grid[y][j]) + 1)

	counter = 0
	for i in range(len(grid)):
		for j in range(2, 11):
			counter += int(grid[i].count(str(j)))

	print(counter)

# part_1()


# part 2
def part_2():
	grid = [['.' for i in range(1000)] for i in range(1000)]
	data = []
	coords = []

	with open('05.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			data.append(line.strip().split(' -> '))
		for n in data:
			next_coord = []
			for c in n:
				next_coord.append(c.split(','))
			coords.append(next_coord)

	for coord in coords:
		x1 = int(coord[0][0])
		x2 = int(coord[1][0])
		y1 = int(coord[0][1])
		y2 = int(coord[1][1])
		if x1 == x2 and y1 == y2: # if coordinates are the same
			if grid[y1][x1] == '.':
				grid[y1][x1] = '1'
			else:
				grid[y1][x1] = str(int(grid[y1][x1]) + 1)
		elif x1 == x2: # if x coordinates are equal
			if y1 > y2:
				for j in range(y2, y1+1):
					if grid[j][x1] == '.':
						grid[j][x1] = '1'
					else:
						grid[j][x1] = str(int(grid[j][x1]) + 1)
			else: # y2 is bigger than y1
				for j in range(y1, y2+1):
					if grid[j][x1] == '.':
						grid[j][x1] = '1'
					else:
						grid[j][x1] = str(int(grid[j][x1]) + 1)
		elif y1 == y2: # if y coordinates are equal
			if x1 > x2:
				for j in range(x2, x1+1):
					if grid[y1][j] == '.':
						grid[y1][j] = '1'
					else:
						grid[y1][j] = str(int(grid[y1][j]) + 1)
			else: # y2 is bigger than y1
				for j in range(x1, x2+1):
					if grid[y1][j] == '.':
						grid[y1][j] = '1'
					else:
						grid[y1][j] = str(int(grid[y1][j]) + 1)
		# if 45 deg line exists
		elif abs(x1-x2) == abs(y1-y2):
			if x1 > x2 and y1 > y2:
				x = x2
				y = y2
				while x != x1 and y != y1:
					if grid[y][x] == '.':
						grid[y][x] = '1'
					else:
						grid[y][x] = str(int(grid[y][x]) + 1)
					x += 1
					y += 1
			elif x1 > x2 and y2 > y1:
				x = x2
				y = y2
				while x != x1 and y != y1:
					if grid[y][x] == '.':
						grid[y][x] = '1'
					else:
						grid[y][x] = str(int(grid[y][x]) + 1)
					x += 1
					y -= 1
			elif x2 > x1 and y1 > y2:
				x = x1
				y = y1
				while x != x2 and y != y2:
					if grid[y][x] == '.':
						grid[y][x] = '1'
					else:
						grid[y][x] = str(int(grid[y][x]) + 1)
					x += 1
					y -= 1
			elif x2 > x1 and y2 > y1:
				x = x1
				y = y1
				while x != x2 and y != y2:
					if grid[y][x] == '.':
						grid[y][x] = '1'
					else:
						grid[y][x] = str(int(grid[y][x]) + 1)
					x += 1
					y += 1

	counter = 0
	for rows in grid:
		for x in rows:
			if x != '.' and x != '1': # at least 2 overlaps
				counter += 1

	print(counter)

# part_2()