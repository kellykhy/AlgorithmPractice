# 프로그래머스 조이스틱(시도1)
# 채점결과: test13, test18, test20, test22, test24, test25, test27 실패

# A: 아스키코드 65, Z: 아스키코드 122
# name의 길이: 0 이상 20 이하

def solution(name):
    answer = 0
    count = 0
    start, end = 0, 0
    pre = 0
    min_case3 = 40 # 37
    up_down = 0
    for i, l in enumerate(name):
        if (l!='A'):
            count+=1
            if (count==1): start = i
            else: min_case3 = min((pre*2+len(name)-i), min_case3)
            pre = i
            if (ord(l)<78): up_down+=(ord(l)-65)
            else: up_down+=(90-ord(l)+1)
    end = pre
    case1 = end
    case2 = len(name)-start

    answer = min(case1, case2, min_case3) + up_down
    #print()
    #print("case1:", case1)
    #print("case2:", case2)
    #print("min case3:", min_case3)
    #print("start:", start)
    #print("end:", end)

    return answer

print(solution("AABAAAA")) #2+1=3
print(solution("AABABBB")) #5+4=9