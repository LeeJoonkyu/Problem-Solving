import sys

ans = []
for line in sys.stdin:
    line = int(line)
    if line % 2 != 0:
        ans.append(line)

if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))