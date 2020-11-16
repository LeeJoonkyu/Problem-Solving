import sys
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    idx = list(range(n))
    idx[m] = 'target'
    order = 1
    while True:
        if data[0] == max(data):
            if idx[0] == 'target':
                print(order)
                break
            else:
                data.pop(0)
                idx.pop(0)
                order += 1
        else:
            data.append(data.pop(0))
            idx.append(idx.pop(0))