t = int(input())
d = {0: [10], 1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1],
     }
for i in range(10, 100):
    if i % 10 in d:
        d[i] = d[i % 10]
print(d)
for _ in range(t):
    a, b = map(int, input().split())

    l = len(d[a])
    print(d[a][(b % l) - 1])
