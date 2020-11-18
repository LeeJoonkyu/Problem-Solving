n = int(input())
move = list(map(str, input().split()))

# arr = [ [0]*(n+1) for _ in range(n+1)]
# i,j = 1,1
# for m in move:
#     if m == 'R' and j+1 != n+1:
#         j += 1
#     elif m == 'L' and j-1 != 0:
#         j -= 1
#     elif m == 'U' and i-1 != 0:
#         i -= 1
#     elif m == 'D' and i+1 != 0:
#         i += 1
#
# print(i, j)
#

x,y = 1,1
# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
nx,ny = 1,1
for m in move:

    for i in range(len(move_types)):
        if m == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx, ny
print(x,y)