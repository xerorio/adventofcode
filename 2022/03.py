letter_values = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

def value_rucksack(rucksack):
    similar_letter = ''
    first_half = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    for l in set(first_half):
        if l in set(second_half):
            similar_letter = l
    if similar_letter == '':
        return 0
    elif similar_letter.isupper():
        return 26 + letter_values[similar_letter.lower()]
    else:
        return letter_values[similar_letter]

# part 1

def part_1():
    rucksacks = []
    total = 0
    with open('03.txt', 'r') as f:
        rucksacks = f.read().split('\n')
        for r in rucksacks:
            total += value_rucksack(r)
    print(total)

# part_1()


# part 2

def part_2():
    rucksack_groups = []
    total = 0
    with open('03.txt', 'r') as f:
        input_rucksacks = f.read().split('\n')
        for i in range(0, len(input_rucksacks), 3):
            rucksack_groups.append([input_rucksacks[i], input_rucksacks[i + 1], input_rucksacks[i + 2]])
    for group in rucksack_groups:
        similar_letter = ''
        for l in set(group[0]):
            if l in set(group[1]) and l in set(group[2]):
                similar_letter = l
        if similar_letter.isupper():
            total += 26
            total += letter_values[similar_letter.lower()]
        else:
            total += letter_values[similar_letter]
    print(total)

# part_2()