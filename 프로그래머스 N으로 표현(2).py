# 프로그래머스 N으로 표현(DP 알고리즘)
## 시도2(통과)

from collections import defaultdict

def solution(N, number):
    answer = 0
    if N == number:                 # 테스트9 실패 요인
        return 1
    possible_results = defaultdict(list)
    tmp = N
    for i in range(1,9):
        possible_results[i].append(tmp)
        tmp = tmp*10+N
    for count in range(2,9):
        for i in range(1, count//2+1):
            j = count - i
            for result1 in possible_results[i]:
                for result2 in possible_results[j]:
                    r1 = result1 + result2
                    r2 = result1 * result2
                    r3 = result1 // result2
                    r3_ = result2 // result1
                    r4 = result1 - result2
                    if r4 < 0: r4 = result2 - result1
                    tmp_list = [r1, r2, r3, r3_, r4]
                    tmp_list = list(filter(lambda x : x>0, tmp_list))
                    possible_results[count] += tmp_list
                    if number == possible_results[count][0] or number in tmp_list:
                        return count
        possible_results[count][1:] = list(set(possible_results[count][1:]))

    return -1

print(solution(5, 127)) # 6