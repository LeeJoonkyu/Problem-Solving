''' 답안 참고한 풀이 '''
import sys, itertools
import copy
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))


def count_distance(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])

home = []
chicken = []
cd = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append(tuple([i+1, j+1]))
        elif arr[i][j] == 2:
            chicken.append(tuple([i+1, j+1]))
tmp_chicken = copy.deepcopy(chicken)

def list_sum(l):
    sm = 0
    for i in l:
        sm += sum(i)
    return sm
if len(chicken) > m:  # 폐업 시켜야하는 경우
    tmp = list(itertools.combinations(chicken, m))
    mn = 0x7fffffff
    for c in tmp:
        '''폐업한 집을 제외한 치킨집들 하나씩에 대해'''
        for close in chicken:
            if close not in c:
                tmp_chicken.remove(close)

        print(tmp_chicken)
        d = 0x7fffffff
        for h in home:
            '''어떤 집 하나의 치킨거리를 구한다'''
            for tc in tmp_chicken:
                d = min(count_distance(h, tc), d)
            print(h)
            cd[h[0]-1][h[1]-1] = d


        '''모든 집의 치킨거리가 나온 상태'''
        mn = min(list_sum(cd), mn)
        tmp_chicken = copy.deepcopy(chicken)
    print(mn)
else:  # 폐업 안시키는 경우 각 집의 치킨거리의 합이 곧 도시의 치킨 거리
    d = 0x7fffffff
    for h in home:
        for c in chicken:
            d = min(count_distance(h, c), d)
        cd[h[0]-1][h[1]-1] = d
    print(list_sum(cd))

