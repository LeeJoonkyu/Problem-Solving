l = list(map(int, input().split()))

mn = min(l)
mx = max(l)

ans = 0
for i in l:
    if i != mn and i != mx:
        ans = i

if ans == 0:  # mid 값이 mx, 또는 mn 이랑 겹치는 경우
    if l.count(mn) > l.count(mx):
        ans = mn
    else:
        ans = mx

print(ans)