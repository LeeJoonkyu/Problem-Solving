a, b = map(int, input().split())

print(type(a))
print(type(b))

for i in range(5):
    if i == 0:
        print(a + b)
    elif i == 1:
        print(a - b)
    elif i == 2:
        print(a * b)
    elif i == 3:
        print(a / b)
    elif i == 4:
        print(a % b)
