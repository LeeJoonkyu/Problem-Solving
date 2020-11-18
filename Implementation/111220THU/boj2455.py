cur = 0
mx = -1
for i in range(4):
    minus, plus = map(int, input().split())
    cur -= minus
    cur += plus
    if cur > mx:
        mx = cur

print(mx)
