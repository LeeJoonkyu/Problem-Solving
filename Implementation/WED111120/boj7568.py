import sys
n = int(input())

data = []
rank = [1] * n
for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1
    print(rank[i], end=' ')