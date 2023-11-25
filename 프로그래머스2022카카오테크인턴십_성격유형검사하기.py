# 2022 KAKAO TECH INTERSHIP
# 1. 성격 유형 검사하기

import sys

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

def solution(survey, choices):
    score = {"RT":0, "CF":0, "JM":0, "AN":0}
    answer = ''
    for i in range(len(survey)):
        tmp = ''.join(sorted(survey[i]))
        if (tmp != survey[i]):
            score[tmp] -= choices[i]-4
        else:
            score[tmp] += choices[i]-4
    for item in score.items():
        if (item[1] > 0):
            answer += item[0][1]
        else:
            answer += item[0][0]   
    return answer

print(solution(survey, choices))