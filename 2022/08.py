# part 1

def part_1():
    with open('08.txt', 'r') as f:
        trees = [line.strip() for line in f.readlines()]
    visible = 2 * len(trees[0])      # top and bottom row
    visible += 2 * (len(trees) - 2)  # sides

    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees) - 1):
            tree_is_visible = 0
            tree_height = trees[y][x]

            # right direction
            for x2 in range(x + 1, len(trees[0])):
                if tree_height <= trees[y][x2]:  # tree is not visible
                    tree_is_visible += 1
                    break
            # left direction
            for x3 in range(x):
                if tree_height <= trees[y][x3]: # tree is not visible
                    tree_is_visible += 1
                    break
            # bottom direction
            for y2 in range(y + 1, len(trees)):
                if tree_height <= trees[y2][x]:  # tree is not visible
                    tree_is_visible += 1
                    break
            # top direction
            for y3 in range(y):
                if tree_height <= trees[y3][x]:  # tree is not visible
                    tree_is_visible += 1
                    break
            
            if tree_is_visible < 4:
                visible += 1
    
    print(visible)

# part_1()


# part 2

def part_2():
    with open('08.txt', 'r') as f:
        trees = [line.strip() for line in f.readlines()]
    scenic_scores = set()

    # same as part 1 where we iterate away from a tree/point
    # just add one each time we go one step away from that point in each direction
    # multiply it all together

    for x in range(1, len(trees[0]) - 1):
        for y in range(1, len(trees) - 1):
            right = 0
            left = 0
            down = 0
            up = 0
            tree_height = trees[y][x]

            # right direction
            for x2 in range(x + 1, len(trees[0])):
                if tree_height < trees[y][x2]:
                    right += 1
                else:
                    break
            # left direction
            for x3 in range(x):
                if tree_height < trees[y][x3]:
                    left += 1
                else:
                    break
            # bottom direction
            for y2 in range(y + 1, len(trees)):
                if tree_height < trees[y2][x]:
                    down += 1
                else:
                    break
            # top direction
            for y3 in range(y):
                if tree_height < trees[y3][x]:
                    up += 1
                else:
                    break
            
            scenic_scores.add(right * left * down * up)
    
    print(max(scenic_scores))

part_2()
# correct answer: 313200
