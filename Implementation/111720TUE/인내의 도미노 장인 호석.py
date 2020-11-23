''' 오답 후 답안 참조 '''
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
            if stats[x][y] == 'F':
                break
            val = arr[x][y]  # val -1 개의 갯수만큼 dx 또는 dy
            while x >= 0 and x < n and y >= 0 and y < m and val >= 1:
                if stats[x][y] == 'S':
                    stats[x][y] = 'F'
                    score += 1
                    val = max(arr[x][y]-1, val-1)
                else:
                    val -= 1
                x += dx[i]
                y += dy[i]

    # 수비
    x, y = map(int, sys.stdin.readline().split())
    stats[x - 1][y - 1] = 'S'

print(score)
for i in stats:
    for j in i:
        print(j, end=' ')
    print()
