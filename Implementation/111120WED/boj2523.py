n = int(input())

start, mid, end = 1, n, 2*n
star = '*'
for i in range(start, end):
    if i <= mid:
        print('*'*i)
    else:
        print('*'*(end-i))
