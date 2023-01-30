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
    # max_scenic_score = 1
    # for x in range(len(trees[0])):
    #     for y in range(len(trees)):
    #         tree_height = trees[y][x]
    #         right_counter = 1
    #         left_counter = 1
    #         bottom_counter = 1
    #         top_counter = 1
    #         # right direction
    #         for x2 in range(x + 1, len(trees[0])):
    #             if trees[y][x2] > tree_height: # point where you can no longer see
    #                 break
    #             elif trees[y][x2] == tree_height: # point where you can no longer see
    #                 right_counter += 1
    #                 break
    #             right_counter += 1
    #         # left direction
    #         for x3 in range(0, x, -1):
    #             if trees[y][x3] > tree_height: # point where you can no longer see
    #                 break
    #             elif trees[y][x3] == tree_height: # point where you can no longer see
    #                 left_counter += 1
    #                 break
    #             left_counter += 1
    #         # top direction
    #         for y3 in range(0, y, -1):
    #             if trees[y3][x] > tree_height: # point where you can no longer see
    #                 break
    #             elif trees[y3][x] == tree_height: # point where you can no longer see
    #                 top_counter += 1
    #                 break
    #             top_counter += 1
            
    #         new_scenic_score = right_counter * left_counter * bottom_counter * top_counter
    #         if new_scenic_score > max_scenic_score:
    #             print(right_counter, left_counter, bottom_counter, top_counter)
    #             max_scenic_score = new_scenic_score
    
    # print(max_scenic_score)

# part_2()
