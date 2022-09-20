# 프로그래머스 조이스틱(시도2번)
# 시도1 채점결과: test13, test18, test20, test22, test24, test25, test27 -> 실패
# 시도2 -> 통과

# A: 아스키코드 65, Z: 아스키코드 122
# name의 길이: 0 이상 20 이하

def solution(name):
    answer = 0
    count = 0
    start, end = 0, 0
    pre = 0
    min_case3, min_case4 = 40, 40
    up_down = 0
    for i, l in enumerate(name):
        if (l!='A'):
            count+=1
            if (count==1): 
                start = i
            else: 
                min_case3 = min(pre*2+len(name)-i, min_case3)
                min_case4 = min((len(name)-i)*2+pre, min_case4) # 시도1 실패요인 (빠뜨린 부분)
            pre = i
            if (ord(l)<78): up_down+=(ord(l)-65)
            else: up_down+=(90-ord(l)+1)
    end = pre
    answer = min(end, len(name)-start, min_case3, min_case4) + up_down

    return answer



print(solution("AABAAAA")) #2+1=3
print(solution("AABABBB")) #5+4=9
print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("AAABBBABA")) #0
print(solution("ABABAAAAABA")) #10 -> 시도1실패케이스