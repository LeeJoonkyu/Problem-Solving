n = int(input())
space = ' '
start = '*'

for i in reversed(range(n)):
    print(space*i + start*(n-i))