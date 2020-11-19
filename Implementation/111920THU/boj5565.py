import sys
total = int(input())
readable = 0
for _ in range(9):
    readable += int(sys.stdin.readline().rstrip())

print(total - readable)