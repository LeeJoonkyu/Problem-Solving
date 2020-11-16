s = input()
data = [0 for _ in range(26)]
for c in s:
    data[ord(c)-97] += 1

for ans in data:
    print(ans, end=' ')