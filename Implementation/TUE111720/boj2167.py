import sys

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))  # 최대 300 * 300 배열 -> 9만
k = int(input())
for _ in range(k):  # 최대 1만 O(KNM) 소스
    ans = 0
    pos = list(map(int, sys.stdin.readline().split()))
    start = pos[0:2]  # 1,1
    end = pos[2:4]  # 2,3
    if start == end:
        print(arr[start[0]-1][start[1]-1])
    elif start[1] == end[1]:
        for i in range(start[0]-1, n):
            ans += arr[i][end[1]-1]
        print(ans)
    elif start[0] == end[0]:
        for i in range(end[0]-1, m):
            ans += arr[start[0]-1][i]
        print(ans)
    else:
        for i in range(start[0] - 1, end[0]):
            if i == start[0] - 1:
                for j in range(start[1] - 1, m):
                    ans += arr[i][j]
            elif i == end[0] - 1:
                for j in range(end[1]):
                    ans += arr[i][j]
            else:
                for j in range(m):
                    ans += arr[i][j]
        print(ans)

