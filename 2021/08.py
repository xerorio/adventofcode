# part 1
def part_1():
	output_values = []
	with open('08.txt', 'r') as f:
		for i in f.readlines():
			next_output = i.strip().split(' | ')[1].split(' ')
			for n in next_output:
				output_values.append(n)

	counter = 0
	for i in output_values:
		if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
			counter += 1

	print(counter)

# part_1()


# part 2
def part_2():
	"""
	patterns = {
		'0': [6, 'abcefg'],
		'1': [2, 'cf'],
		'2': [5, 'acdeg'],
		'3': [5, 'acdfg'],
		'4': [4, 'bcdf'],
		'5': [5, 'abdfg'],
		'6': [6, 'abdefg'],
		'7': [3, 'acf'],
		'8': [7, 'abcdefg'],
		'9': [6, 'abcdfg']
	}
	0: [6] [right-top, right-bottom, left-top, left-bottom, top, bottom]
	1: [2] [right-top, right-bottom]
	2: [5] [right-top, left-bottom, top, middle, bottom]
	3: [5] [right-top, right-bottom, top, middle, bottom]
	4: [4] [right-top, right-bottom, left-top, middle]
	5: [5] [right-bottom, left-top, top, middle, bottom]
	6: [6] [right-bottom, left-top, left-bottom, top, middle, bottom]
	7: [4] [right-top, right-bottom, top]
	8: [7] [all]
	9: [6] [right-top, right-bottom, left-top, top, middle, bottom]
	"""

	input_signals = []
	with open('08eg2.txt', 'r') as f:
		for i in f.readlines():
			next_input_r = [j.split(' ') for j in i.strip().split(' | ')]
			next_input = []
			for k in next_input_r:
				for m in k:
					next_input.append(list(''.join(sorted(m))))
			input_signals.append(next_input)

<<<<<<< HEAD
	# check for each signal if there are letters recurring in other ones to find patterns

	for signal in input_signals:
		print(signal)
=======
	for signals in input_signals:
		pattern = {
			'top':			'',
			'right-top':	'',
			'right-bottom':	'',
			'left-top':		'',
			'left-bottom':	'',
			'middle':		'',
			'bottom':		''
		}
		for i in signals:
			# compare 7 and 2 to find the top signal
			if len(i) == 3:
				for j in signals:
					if len(j) == 2:
						for charac in i:
							if j.find(charac) == -1:
								pattern['top'] = charac
		print(pattern)
>>>>>>> origin/main

part_2()