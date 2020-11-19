mx = 0
win = 0
for idx, _ in enumerate(range(5)):
    a, b, c, d = map(int, input().split())
    if a + b + c + d > mx:
        mx = a + b + c + d
        win = idx + 1

print(win, mx)
