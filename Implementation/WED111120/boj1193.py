n = int(input())

threshold = 0
where = 0
before = 0
for i in range(1, 10000000):
    threshold += i
    if n <= threshold:
        where = i
        before = threshold - i
        break

if where % 2 == 0:
    numer = n - before
    denom = where - numer + 1
else:
    denom  = n - before
    numer = where - denom + 1

print('{}/{}'.format(numer, denom))
