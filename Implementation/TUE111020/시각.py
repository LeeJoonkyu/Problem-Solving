n = int(input())

m, s = 60, 60
cnt = 0
# for i in range(n+1):
#     if '3' in str(i):
#         cnt += 1
#         continue
#     for j in range(m):
#         if '3' in str(j):
#             cnt += 1
#             continue  # 2시 3분 에서 00초 01초 ~ 59초까지 다 세야하는데, 여기서 컨티뉴해버리면 2시 4분으로 넘어감...
#         for k in range(s):
#             if '3' in str(k):
#                 cnt += 1
#
# print(cnt)


n = int(input())

m, s = 60, 60
cnt = 0
for i in range(n+1):
    for j in range(m):
        for k in range(s):
            if '3' in str(i) + str(j) + str(k):
                cnt+=1

print(cnt)
