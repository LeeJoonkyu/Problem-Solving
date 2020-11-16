import sys, itertools
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))


def count_distance(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append(tuple([i+1, j+1]))
        elif arr[i][j] == 2:
            chicken.append(tuple([i+1, j+1]))

print(home, chicken)

if len(chicken) > m:  # 폐업 시켜야하는 경우
    tmp = list(itertools.combinations(chicken, m))
    print(tmp)
    print(tmp[0])
    print(tmp[0][0])
    cd = []
    for cs in tmp:
        for c in cs:
            mn = 987654321
            for h in home:
                if count_distance(h, c) < mn:
                    mn = count_distance(h, c)
            cd.append(mn)
    print(cd)

# cd = []
# for h in home:
#     mn = 987654321
#     for c in chicken:
#         if count_distance(h, c) < mn:
#             mn = count_distance(h, c)
#     cd.append(mn)
#
# print(cd)
#
# if len(chicken) <= m:
#     print(sum(cd))
# else:
#     cd.sort()
#     print(sum(cd[:m]))
#
