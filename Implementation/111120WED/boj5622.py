s = input()
time = [0, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
ans = 0
for c in s:
    ans += time[ord(c) - 64]
print(ans)
