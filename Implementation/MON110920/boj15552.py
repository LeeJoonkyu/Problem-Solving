import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    print(sum(list(map(int, input().split()))))
    # print(sum(list(map(int, sys.stdin.readline().rstrip().split()))))