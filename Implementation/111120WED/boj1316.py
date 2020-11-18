import sys
ans = 0
n = int(input())
for _ in range(n):
    visited = [False] * 26
    s = sys.stdin.readline().rstrip()
    chk = True
    for idx, c in enumerate(s):
        if idx == 0:
            visited[ord(c)-97] = True
        else:
            if s[idx-1] != s[idx] and not visited[ord(c)-97]:  # 이전과 다르고, 방문한적이 없다 -> 체크
                visited[ord(c)-97] = True
            elif s[idx-1] != s[idx] and visited[ord(c)-97]:  # 다른데 이미 방문한 경우
                chk = False
                break
    if chk:
        ans += 1

print(ans)