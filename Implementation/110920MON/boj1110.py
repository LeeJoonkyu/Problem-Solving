N = int(input())
a = N
cycle = 0
while True:
    ten = a // 10
    one = a % 10

    temp = ten + one

    newten = 10 * one
    newone = temp % 10
    new = newten + newone
    cycle += 1
    if new == N:
        break
    a = new
print(cycle)

