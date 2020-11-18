import sys

n, m, r = map(int, input().split())
domino = []
stats = [['S'] * m for _ in range(n)]
score = 0

# 동, 서, 남, 북
ddir = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
for i in range(n):
    domino.append(list(map(int, sys.stdin.readline().split())))


def attack(x, y, d):
    global score
    if stats[x][y] == 'F':
        return
    dx, dy = ddir[d]
    val = domino[x][y]
    while x >= 0 and x < n and y >= 0 and y < m and val >= 1:
        if stats[x][y] == 'S':
            stats[x][y] = 'F'
            score += 1
            val = max(domino[x][y] - 1, val - 1)
        else:
            val -= 1
        x += dx
        y += dy


for _ in range(r):
    x, y, d = map(str, sys.stdin.readline().split())
    x = int(x) - 1
    y = int(y) - 1
    # 공격
    attack(x, y, d)

    # 수비
    x, y = map(int, sys.stdin.readline().split())
    stats[x - 1][y - 1] = 'S'

print(score)
for i in stats:
    for j in i:
        print(j, end=' ')
    print()
