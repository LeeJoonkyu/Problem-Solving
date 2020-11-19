import math
m = int(input())
n = int(input())
ans = []
for i in range(m, n+1):
    if math.sqrt(i) - int(math.sqrt(i)) == 0:
        ans.append(i)

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)