import sys
arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

ans = max(arr)
print(ans)
print(arr.index(ans))