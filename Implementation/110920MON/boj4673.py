arr = [True for _ in range(11001)]

for i in range(1, 10000):
    arr[i + i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10] = False
arr[0] = False
for i in range(1, 10000):
    if arr[i]:
        print(i)