import sys

n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
x, y, dir = map(int, input().split())
visited[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


cnt = 1
turn_time = 0
while True:
    # 처음에 왼쪽을 보고
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전한 후 정면을 방문하지 않았다면 이동(좌표갱신)
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 회전한 후 정면의 칸을 이미 방문했거나 바다인 경우
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤가 바다가 아닌 경우
        if arr[nx][ny] != 1:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)
