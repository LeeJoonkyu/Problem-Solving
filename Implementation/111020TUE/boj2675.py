import sys

t = int(input())
for _ in range(t):
    r, s = map(str, sys.stdin.readline().split())
    r = int(r)
    for i in range(len(s)):
        print(s[i]*r, end='')
    print(" ")