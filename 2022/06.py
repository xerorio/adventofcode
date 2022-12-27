# part 1

def part_1():
    with open('06.txt', 'r') as f:
        data = f.read()
    i = 0
    while i < len(data):
        if len(set(data[i:i + 4])) == len(data[i:i + 4]):
            print(i + 4)
            break
        i += 1

# part_1()


# part 2

def part_2():
    with open('06.txt', 'r') as f:
        data = f.read()
        i = 0
        while i < len(data):
            if len(set(data[i:i + 14])) == len(data[i:i + 14]):
                print(i + 14)
                break
            i += 1

# part_2()
