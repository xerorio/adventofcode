# part 1
def part_1():
    from string import ascii_lowercase
    alphabet = list(ascii_lowercase)

    strings = []

    with open('05.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            strings.append(line.strip())

    counter = 0

    for i in range(len(strings)):
        if (strings[i].count('a') + strings[i].count('e') + strings[i].count('o') + strings[i].count('i') + strings[i].count('u')) >= 3:
            if 'ab' not in strings[i] and 'cd' not in strings[i] and 'pq' not in strings[i] and 'xy' not in strings[i]:
                for letter in alphabet:
                    if f'{letter}{letter}' in strings[i]:
                        counter += 1
                        break
    
    print(counter)

# part_1()


# part 2
def part_2():
    from string import ascii_lowercase
    alphabet = list(ascii_lowercase)

    strings = []

    with open('05.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            strings.append(line.strip())

    counter = 0

    for i in range(len(strings)):
        counter += 1
    
    print(counter)

part_2()