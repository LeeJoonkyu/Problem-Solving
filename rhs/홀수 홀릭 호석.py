''' 오답 풀이. dfs로 풀어야함'''
s = input()
ans = []
odd = 0
def count_odd(s):
    global odd
    for dg in s:
        if int(dg) % 2 != 0:
            odd += 1

def rec(s):
    global odd, ans
    l = len(s)
    if len(s) == 1:
        count_odd(s)
        ans.append(odd)
        odd = 0
        return
    elif len(s) == 2:
        count_odd(s)
        new_s = str(int(s[0]) + int(s[1]))
        rec(new_s)
        odd = 0
        return
    else:
        for i in range(0, l - 2):
            for j in range(i+1, l-1):
                count_odd(s)
                new_s = str(int(s[:i+1]) + int(s[i+1:j+1]) + int(s[j+1:]))
                rec(new_s)


rec(s)
print(min(ans), max(ans))