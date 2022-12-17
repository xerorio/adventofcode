# part 1
def part_1():
    with open('01.txt', 'r') as f:
        print(max([sum([int(x) for x in elf.split('\n')]) for elf in f.read().split('\n\n')]))

# part_1()


# part 2
def part_2():
    with open('01.txt', 'r') as f:
        calories = [sum([int(x) for x in elf.split('\n')]) for elf in f.read().split('\n\n')]
        calories.sort()
        print(sum(calories[-3:]))

# part_2()