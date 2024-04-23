# 백준 2457번 공주님의 정원

import sys
input = sys.stdin.readline

n = int(input())
# 꽃 수명
flower = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flower.append([sm, sd, em, ed])
    
# 꽃을 심어놓아야 하는 기간 (시작=3/1, 끝=11/30)
begin = [3, 1]
end = [11, 30]
 
# 날짜 비교 함수(equal=True: 같거나 크다면, equal=False: 크다면)
def right_greater(m1, d1, m2, d2, equal):
    if (m1 < m2):
        return True
    elif (m1 == m2):
        if (equal): return (d1 <= d2)
        else: return (d1 < d2)
    else:
        return False

# 꽃 수명 시작 날짜를 기준으로 정렬
flower.sort(key=lambda x: (x[0], x[1]))
        
flag = 0
result = 0
max_end = [0, 0]
for lifetime in flower:
    if right_greater(lifetime[0], lifetime[1], begin[0], begin[1], 1):
        if (right_greater(max_end[0], max_end[1], lifetime[2], lifetime[3], 0)):
            max_end = [lifetime[2], lifetime[3]]
    else:
        result += 1
        begin = max_end
        if right_greater(lifetime[0], lifetime[1], begin[0], begin[1], 1):
            if (right_greater(max_end[0], max_end[1], lifetime[2], lifetime[3], 0)):
                max_end = [lifetime[2], lifetime[3]]
        else:
            flag = 1 # 중간에 공백기 여부 체크 (예외1)
            break
    if (right_greater(end[0], end[1], max_end[0], max_end[1], 0)):
        result += 1
        break
    
# right_greater -> 11월 30일까지 피어있는 꽃이 없는 경우 체크 (예외2)
if right_greater(max_end[0], max_end[1], end[0], end[1], 1) or flag:
    print(0) 
else: 
    print(result)