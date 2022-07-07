# 프로그래머스2021카카오 순위검색( 다른 사람 풀이과정 )
# https://whwl.tistory.com/193
# 정확성 테스트 통과 O / 효율성 테스트 통과 O

from itertools import combinations as combi
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)        ## checkpoint1: <defaultdict> info_dict의 default value는 리스트
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i): ## checkpoint2: <combinations> 조합을 튜플 형식으로
                tmp_key = ''.join(c)     ## checkpoint3: <join 함수> 리스트or튜플을 ~으로 연결하여 하나의 문자열로 만듦
                info_dict[tmp_key].append(info_val)
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')          ## checkpoint4: <remove 함수> 리스트의 특정 원소 제거, 단 제일 먼저 나오는 값부터 제거
        while '-' in query:
            query.remove('-')

        tmp_q = ''.join(query)
        if tmp_q in info_dict:
            scores = info_dict[tmp_q] # list
            # query_score보다 같거나 큰 score의 인덱스 구하기
            if len(scores) > 0:
                front, end = 0, len(scores) # (파이썬스러운 문법임!)
                while front < end:       ## checkpoint5: <lower bount 찾기> 이진탐색과 동일한 로직!
                    mid = (front+end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        front = mid+1
                answer.append(len(scores) - front)
        else:
            answer.append(0)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))