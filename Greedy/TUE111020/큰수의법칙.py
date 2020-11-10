import sys
n, m, k = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

'''me'''
# mx = max(data)
# mxtwice = False
# cnt = 0
# for i in data:
#     if i == mx:
#         cnt+=1
# if cnt >= 2:
#     mxtwice = True
#
# ans = 0
# if mxtwice:
#     ans = mx * m
# else:
#     data.remove(mx)
#     mx2 = max(data)
#     for idx, i in enumerate(range(m)):
#         if idx == 0:
#             ans += mx
#         elif i % k != 0:
#             ans += mx
#         else:
#             ans += mx2
#         print(mx, mx2, ans)
#
# print(ans)

'''na-naive'''
# data.sort()
# mx = data[-1]
# mx2 = data[-2]
# ans = 0
# while True:
#     for i in range(k):
#         if m == 0:  # 이 조건문이 m-=1 아래에 있으면 포문을 돌다가 m이 음수가 되어버리는 경우 무한루프
#             break
#         ans += mx
#         m -= 1
#     if m == 0:
#         break
#     ans += mx2
#     m -= 1
# print(ans)

'''na-advanced'''
data.sort()  # O(nlogn)
mx = data[-1]
mx2 = data[-2]
ans = 0

ans += (m // (k+1) * k + m % (k+1) ) * mx
ans += m // (k+1) * mx2
print(ans)