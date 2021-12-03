# puzzle input: ckczppom
import hashlib
puzzle_input = 'ckczppom'

# part 1
def part_1():
	for i in range(10000000):
		i_string_len = len(str(i))
		if i_string_len < 10:
			next_str = puzzle_input + '0000' + str(i)
		elif i_string_len < 100:
			next_str = puzzle_input + '000' + str(i)
		elif i_string_len < 1000:
			next_str = puzzle_input + '00' + str(i)
		elif i_string_len < 10000:
			next_str = puzzle_input + '0' + str(i)
		elif i_string_len < 100000:
			next_str = puzzle_input + str(i)

		md5 = hashlib.md5(next_str.encode())
		if next_str[5:] == '00000':
			print(md5.hexdigest())
			break

part_1()


# part 2
def part_2():
	pass

# part_2()