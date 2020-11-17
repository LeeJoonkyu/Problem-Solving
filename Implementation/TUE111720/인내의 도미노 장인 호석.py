import sys

n, m, r = map(int, input().split())
arr = []
stats = [['S'] * m for _ in range(n)]
copy = arr

# 동, 서, 남, 북
dir = ['E', 'W', 'S', 'N']
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

score = 0
for _ in range(r):
    # 공격
    x, y, d = map(str, sys.stdin.readline().split())
    x = int(x) - 1
    y = int(y) - 1
    for i in range(len(dir)):
        if d == dir[i]:  # 방향 결정
            while True:
                f = False
                if x > n-1 or x < 0 or y > m-1 or y < 0:
                    break
                val = arr[x][y]  # val -1 개의 갯수만큼 dx 또는 dy
                if val - 1 == 0:
                    break

                for i in range(val - 1):
                    if stats[x][y] == 'S':
                        stats[x][y] = 'F'
                        score += 1
                    # if i == val -2 and stats[x][y] == 'F':
                    #     break
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx > n-1 or nx < 0 or ny > m-1 or ny < 0:
                        f = True
                        break
                    if stats[nx][ny] == 'S':
                        score += 1
                        stats[nx][ny] = 'F'
                    x = nx
                    y = ny
                if f:
                    break
    # 수비
    x, y = map(int, sys.stdin.readline().split())
    stats[x - 1][y - 1] = 'S'

print(score)
for i in stats:
    for j in i:
        print(j, end=' ')
    print()
