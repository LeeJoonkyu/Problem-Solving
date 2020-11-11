import sys
yoot = ['A', 'B', 'C', 'D', 'E']
res = [3, 2, 1, 0, 4]

for line in sys.stdin:
    print(yoot[res.index(sum(list(map(int,line.split()))))])