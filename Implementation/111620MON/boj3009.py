import sys
arr_x = []
arr_y = []

for line in sys.stdin:
    if line == '\n':  # 백준에서는 없어도 무방
        break
    l = line.rstrip().split()
    arr_x.append(l[0])
    arr_y.append(l[1])

ans_x = 0
ans_y = 0
for x,y in zip(arr_x, arr_y):
    if arr_x.count(x) == 1:
        ans_x = x
    if arr_y.count(y) == 1:
        ans_y = y

print(ans_x, ans_y)
