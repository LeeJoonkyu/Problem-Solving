import sys

color = []
arr = []
cnt = 0

for idx, line in enumerate(sys.stdin):
    if line == '\n':
        break
    arr.append(list(line.rstrip()))
    if idx % 2 == 0:
        color.append(['w','b','w','b','w','b','w','b'])
    else:
        color.append(['b','w','b','w','b','w','b','w'])


for col, ar in zip(color, arr):
    print(col, ar)
    for c, a in zip(col, ar):
        print(c, a)
        if a == 'F' and c == 'w':
            cnt += 1

print(cnt)


