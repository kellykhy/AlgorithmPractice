# 프로그래머스 N으로 표현(DP 알고리즘)
## 시도2

from collections import defaultdict

def solution(N, number):
    answer = 0
    possible_results = defaultdict(list)
    tmp = N
    for i in range(1,9):
        possible_results[i].append(tmp)
        tmp = tmp*10+N
    for count in range(2,9):
        for j in range(1, count//2+1):
            h = count-j
            #print("j:", j, "h:", h)
            for result1 in possible_results[j]:
                for result2 in possible_results[h]:
                    r1 = result1 + result2
                    r2 = result1 * result2
                    r3 = result1 // result2
                    r3_ = result2 // result1
                    r4 = result1 - result2
                    if r4 < 0: r4 = result2 - result1
                    tmp_list = [r1, r2, r3, r3_, r4]
                    #print(tmp_list)
                    tmp_list = list(filter(lambda x : x>0, tmp_list))
                    #print(tmp_list)
                    #print()
                    if number in tmp_list:
                        return count
                    else:
                        possible_results[count] += tmp_list
    return -1

print(solution(5, 87))