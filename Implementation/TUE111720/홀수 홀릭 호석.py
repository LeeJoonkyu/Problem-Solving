s = input()
ans = []
odd = 0
l = len(s)
def count_odd(s):
    global odd
    for dg in s:
        if int(dg) % 2 != 0:
            odd += 1

def rec(s):
    global odd, ans, l
    count_odd(s)
    if len(s) == 1:
        ans.append(odd)
        odd = 0
        return
    elif len(s) == 2:
        new_s = int(s[0]) + int(s[1])
        s = str(new_s)
        return rec(s)
    else:
        for i in range(1, l - 1):
            for j in range(i+1, l):
                new_s = int(s[0:i]) + int(s[i:j]) + int(s[j:l])
                s = str(new_s)
                return rec(s)

rec(s)
print(min(ans), max(ans))