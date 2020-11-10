import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
mn = -1

for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    tmp = min(arr)
    if tmp > mn:
        mn = tmp
print(mn)
