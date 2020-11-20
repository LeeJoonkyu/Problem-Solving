from collections import Counter
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

if n == 1:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(arr[0] - arr[0])
else:
    print(round(sum(arr) / n))  # 산술 평균
    print(sorted(arr)[len(arr) // 2])  # 중앙값

    cnt = Counter(sorted(arr))  # 소팅 후의 카운터 사용과 아닌 것의 차이?
    ans = cnt.most_common()  # 빈도 기준 내림차순 정렬
    if len(ans) > 1:
        if ans[0][1] == ans[1][1]:  # 최빈값이 여러개인 경우
            # ans.sort(key=lambda x:x[0], reverse=True)
            # is_multi = True
            # for i in range(len(ans) - 1):
            #     if ans[i][1] != ans[i + 1][1]:
            #         print(ans[i-1][0])
            #         is_multi = False
            #         break
            # if is_multi:  # 모든 원소가 최빈값인 경우
            #     print(ans[-2][0])
            print(ans[1][0])

        else:
            print(ans[0][0])
    else:
        print(ans[0][0])
    s_arr = sorted(arr)
    print(abs(max(s_arr) - min(s_arr)))

