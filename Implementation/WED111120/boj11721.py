s = input()
# k = 10
# div = len(s) // k
# res = len(s) % k
#
# length = len(s)
# if length < 10:
#     print(s)
# else:
#     while True:
#         for i in range(k - 10, k):
#             print(s[i], end='')
#         print()
#         k += 10
#         if length - k < 0:
#             for i in range(k - 10, length):
#                 print(s[i], end='')
#             break
#

'''pythonic'''
for i in range(0, len(s), 10):
    print(s[i:i + 10])
