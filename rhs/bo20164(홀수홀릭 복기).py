s = input()
ans_min = 0x7fffffff
ans_max = 0
def count_odd(s):
    odd = 0
    for dg in s:
        if int(dg) % 2 != 0:
            odd += 1
    return odd

def dfs(s:str, total_odd_count:int):
    global odd, ans
    l = len(s)
    if len(s) == 1:
        global ans_min, ans_max
        print(ans_min, ans_max)
        ans_min = min(ans_min, total_odd_count)
        ans_max = max(ans_max, total_odd_count)
        return
    elif len(s) == 2:
        new_s = str(int(s[0]) + int(s[1]))
        dfs(new_s, count_odd(new_s)+total_odd_count)
        return
    else:
        for i in range(0, l - 2):
            for j in range(i+1, l-1):
                count_odd(s)
                new_s = str(int(s[:i+1]) + int(s[i+1:j+1]) + int(s[j+1:]))
                dfs(new_s, count_odd(new_s) + total_odd_count)


dfs(s, count_odd(s))
print(ans_min, ans_max)