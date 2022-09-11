# 프로그래머스 N으로 표현(DP 알고리즘)
## 시도1
from collections import defaultdict

def solution(N, number):
    answer = 0
    possible_results = defaultdict(list)
    possible_results[1].append(N)
    found = 0

    for i in range(2,9):
        r0 = possible_results[i-1][0]*10+N
        if (r0 == number):
            found = 1
            break
        possible_results[i].append(r0)
        for result in possible_results[i-1]:
            r1 = result*N  # 곱하기
            if (r1 == number):
                found = 1
                break
            elif (r1 > 0):
                possible_results[i].append(r1)

            r2 = result//N # 나누기***
            if (r2 == number):
                found = 1
                break
            elif (r2 > 0):
                possible_results[i].append(r2)
            r2_2 = N//result
            if (r2_2 == number):
                found = 1
                break
            elif (r2_2 > 0):
                possible_results[i].append(r2_2)

            r3 = result-N # 빼기 ***
            if (r3 == number):
                found = 1
                break
            elif (r3 > 0):
                possible_results[i].append(r3)
            r3_2 = N-result
            if (r3_2 == number):
                found = 1
                break
            elif (r3_2 > 0):
                possible_results[i].append(r3_2)

            r4 = result+N # 더하기
            if (r4 == number):
                found = 1
                break
            elif (r4 > 0):
                possible_results[i].append(r4)
        if (found == 1):
            answer = i
            break
        tmp_set = set(possible_results[i][1:])
        possible_results[i] = [possible_results[i][0]] + list(tmp_set)
    if (found == 0):
        answer = -1

    #print(possible_results)
    return answer

print(solution(5, 127))