import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

ans = ''
for j in range(len(arr[0])):
    target = arr[0][j]
    is_same = True
    for i in range(1, len(arr)):
        if target != arr[i][j]:
            is_same = False
            break
    if not is_same:
        ans += '?'
    else:
        ans += target

print(ans)
