pos = input()
x, y = int(pos[1]), ord(pos[0]) - 96

ans = 0
# d1 = [-1, 1]
# d2 = [-2, 2]
#
# for i in range(2):
#   if y + d2[i] > 0 and y+d2[i]<9:
#     for j in range(2):
#       if x+ d1[j] >0 and x+d1[j]<9:
#         ans +=1
#
# for i in range(2):
#   if x + d2[i] > 0 and x+d2[i]<9:
#     for j in range(2):
#       if y + d1[j] > 0 and y + d1[j] < 9:
#         ans += 1
#
# print(ans)

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
for step in steps:
  next_x = x + step[0]
  next_y = y + step[1]
  if next_x > 0 and next_x < 9 and next_y > 0 and next_y < 9:
    ans += 1
print(ans)
