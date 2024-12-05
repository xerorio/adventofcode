# part 1
from string import ascii_lowercase

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
    import re
    # from string import ascii_lowercase
    # alphabet = ascii_lowercase

    strings = []
    with open('05.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            strings.append(line.strip())
    
    # string contains two characters next to each other that are the same
    regex_string_1 = r'.*(([a-z])\\1).*'
    pattern = re.compile(regex_string_1)
    # and that it doesn't contain three in a row
    regex_string_2 = r'.*[a-z]\\1\\1.*'
    
    # string contains at least one letter which repeats with exactly one letter between them
    regex_string_3 = r'.*[a-z].{1}[a-z].*'

    counter = 0
    
    for i in range(len(strings)):
        matches = pattern.finditer(strings[i])
        print(list(matches))

part_2()