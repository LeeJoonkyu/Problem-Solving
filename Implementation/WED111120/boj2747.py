n = int(input())

a = 0
b = 1
c = 1
if n == 0:
    print(a)
elif n == 1:
    print(b)
elif n == 2:
    print(c)
else:
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    print(c)

'''
n = int(input())
a = 0
b = 1

for _ in range(n):
    a, b = b, a+b

print(a)

'''