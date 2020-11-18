import sys
t = int(input())
for _ in range(t):
    cycle = 0
    room = 0
    h, w, n = map(int, sys.stdin.readline().split())
    while cycle < n:
        cycle += h
        room += 1
    floor = n - h * (room - 1)
    if room >= 10:
        print(str(floor) + str(room))
    else:
        print('{}0{}'.format(floor, room))
