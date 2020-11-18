import sys
n = int(input())
data = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        data.append(num)
    else:
        data.pop()

print(sum(data))