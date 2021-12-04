# puzzle input: ckczppom
import hashlib
puzzle_input = 'ckczppom'

# part 1
def part_1():
	for i in range(1000000):
		next_str = puzzle_input + str(i) 
		md5_string = hashlib.md5(next_str.encode()).hexdigest()
		
		if md5_string[:5] == '00000':
			print(i)
			break

# part_1()


# part 2
def part_2():
	for i in range(10000000):
		next_str = puzzle_input + str(i) 
		md5_string = hashlib.md5(next_str.encode()).hexdigest()
		
		if md5_string[:6] == '000000':
			print(i)
			break

# part_2()