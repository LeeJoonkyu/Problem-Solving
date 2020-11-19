n = int(input())
ans = [0, 0]
for _ in range(n):
    op = int(input())
    ans[op] += 1

print("Junhee is not cute!" if ans[0] > ans[1] else "Junhee is cute!")
