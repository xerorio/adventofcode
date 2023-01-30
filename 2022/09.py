# part 1

def part_1():
    head = (0, 0)
    tail = (0, 0)
    with open('09.txt', 'r') as f:
        instructions = [[line.strip().split(' ')[0], int(line.strip().split(' ')[1])] for line in f.readlines()]
    for instruction in instructions:
        direction = instruction[0]
        times = instruction[1]
        for i in range(times):
            if head == tail:
                if direction == 'L':
                    head[0] -= 1
                elif direction == 'R':
                    head[0] += 1
                elif direction == 'U':
                    head[1] += 1
                elif direction == 'D':
                    head[1] -= 1
            else:
                if direction == 'L':
                    head[0] -= 1
                elif direction == 'R':
                    head[0] += 1
                elif direction == 'U':
                    head[1] += 1
                elif direction == 'D':
                    head[1] -= 1
                horizontal = head[0] - tail[0]
                vertical = head[1] - tail[1]
                if horizontal == 2:
                    pass

part_1()


# part 2

def part_2():
    with open('09.txt', 'r') as f:
        pass

# part_2()
