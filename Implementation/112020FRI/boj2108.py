from collections import Counter
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

print(round(sum(arr) / n))  # 산술 평균
print(sorted(arr)[len(arr) // 2])  # 중앙값
for i in range(20):
    cnt = Counter(sorted(arr))
    ans = cnt.most_common()  # 빈도 기준 내림차순 정렬
    #  Counter(sorted(arr)) == Counter(arr) 이지만 내부적으로 키-값 배열 순서가 다르다.
    #  그래서 most_common()은 빈도가 동일하다면 처음에 마주친 값을 기준으로 소팅하기 때문에, 정답 오답 차이가 난다.
    if n > 1:
        if ans[0][1] == ans[1][1]:  # 최빈값이 여러개인 경우
            print(ans[1][0])
            # ans.sort(key=lambda x:x[0], reverse=True)  # 두번째로 작은 값을 찍어야하므로 값 기준 내림차순 정렬
            # ans.sort(key=lambda x:x[1], reverse=True)  # 다시 빈도기준 내림차순 정렬.  없을 시 반례 : 7 1 1 2 2 3 3 4
            # is_multi = True
            # for i in range(len(ans) - 1):
            #     if ans[i][1] != ans[i + 1][1]:
            #         print(ans[i-1][0])
            #         is_multi = False
            #         break
            # if is_multi:  # 모든 원소가 최빈값인 경우
            #     print(ans[-2][0])
        else:
            print(ans[0][0])
    else:
        print(ans[0][0])
s_arr = sorted(arr)
print(s_arr[-1] - s_arr[0])