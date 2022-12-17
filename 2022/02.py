# part 1
def part_1():
    scores = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    with open('02.txt', 'r') as f:
        total_score = sum([scores[i] for i in f.read().split('\n')])
    print(total_score)

# part_1()


# part 2
def part_2():
    scores = {
        'A X': 3,#rocklose
        'A Y': 4,#rockdraw
        'A Z': 8,#rockwin
        'B X': 1,#paperlose
        'B Y': 5,#paperdraw
        'B Z': 9,#paperwin
        'C X': 2,#scissorslose
        'C Y': 6,#scissorsdraw
        'C Z': 7,#scissorswin
    }
    with open('02.txt', 'r') as f:
        total_score = sum([scores[i] for i in f.read().split('\n')])
    print(total_score)

# part_2()