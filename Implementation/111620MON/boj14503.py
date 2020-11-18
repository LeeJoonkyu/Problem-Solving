import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = []
visited = [[False] * m for _ in range(n)]
visited[x][y] = True
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))


def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3


turn_time = 0
cnt = 1
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    # 방문하지 않았고, 빈칸인 경우
    if not visited[nx][ny] and arr[nx][ny] == 0:
        visited[nx][ny] = True
        x = nx
        y = ny
        cnt += 1
        turn_time = 0  # 새로운 칸이므로 턴타임 초기화
        continue
    # 이미 청소했거나, 벽인 경우
    else:
        turn_time += 1  # 돈 방향으로 전진 할 수 없는 경우 턴타임 추가
        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if arr[nx][ny] == 1:  # 뒤가 막힌 경우
                break
            else:
                x = nx
                y = ny
                turn_time = 0

print(cnt)
