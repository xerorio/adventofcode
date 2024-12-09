# part 1

def check_pair(pair):
    if pair[0] == pair[1]:
        return 1
    elif int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
        return 1
    elif int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1]):
        return 1
    return 0

def part_1():
    pairs = []
    counter = 0
    with open('04.txt', 'r') as f:
        for pair_of_ranges in f.read().split('\n'):
            new_pair = []
            for r in pair_of_ranges.split(','):
                new_pair.append(r.split('-'))
            pairs.append(new_pair)
    for p in pairs:
        counter += check_pair(p)
    print(counter)

# part_1()


# part 2

def overlap(pair):
    for i in pair[0]:
        if i in pair[1]:
            return 1
    return 0

def part_2():
    pairs = []
    counter = 0
    with open('04.txt', 'r') as f:
        for pair_of_ranges in f.read().split('\n'):
            new_pair = [set(), set()]
            new_ranges = []
            for r in pair_of_ranges.split(','):
                new_ranges.append(r.split('-'))
            for x in range(2):
                for i in range(int(new_ranges[x][0]), int(new_ranges[x][1]) + 1):
                    new_pair[x].add(i)
            pairs.append(new_pair)
    for p in pairs:
        counter += overlap(p)
    print(counter)

# part_2()
