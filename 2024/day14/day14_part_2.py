with open("14.txt") as fin:
    lines = fin.read().strip().split("\n")


n = 103
m = 101

# n = 7
# m = 11


p = []
v = []

for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))

    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

N = len(p)

def update():
    global p, v
    for i in range(N):
        p[i][0] = (p[i][0] + v[i][0] + n) % n
        p[i][1] = (p[i][1] + v[i][1] + m) % m

seen = {}
step = 0
while True:
    print(f'Step: {step}')
    picture = [[" "] * (m//2+1) for _ in range(n//4+1)]
    for i, j in p:
        picture[i//4][j//2] = "#"

    picture = "\n".join(["".join(line) for line in picture])
    if picture in seen:
        print(f"Saw this picture at step {seen[picture]}, stopping...")
        break
    seen[picture] = step

    print(picture)
    print('\n\n')

    update()

    step += 1