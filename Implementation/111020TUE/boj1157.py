# s = input()
# s = s.lower()

'''시간 초과'''
# mx = 0
# flag = 0
# ans = None
# for c in s:  # 100만
#     tmp = s.count(c)  # 100만
#     if tmp > mx:
#         mx = tmp
#         ans = c
#         flag += 1
#
# if flag > 2:
#     print('?')
# else:
#     print(ans[0].capitalize())

from collections import defaultdict

s = input()
s = s.upper()
d = defaultdict(int)
for c in s:
    d[c] += 1
mx = 0
ans = ''
for k, v in d.items():
    if v >= mx:
        ans = k
        mx = v

print(d)
cnt = 0
for k, v in d.items():
    if v == mx:
        cnt += 1

if cnt >= 2:
    print('?')
else:
    print(ans.upper())
