# 프로그래머스2021카카오 순위검색( 다른 사람 풀이과정 )
# https://whwl.tistory.com/193

from itertools import combinations as combi
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list) # info_dict의 default value는 리스트
    for info in infos:
        info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key] = info_val
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)
        if tmp_q in info_dict:
            scores = info_dict[tmp_q] # list
            # query_score보다 같거나 큰 score의 인덱스 구하기
            front, end = 0, len(scores) # 파이썬스러운 문법임!
            while front < end:
                mid = (front+end) // 2
                if scores[mid] >= query_score:
                    end = mid
                else:
                    start = mid+1
            answer.append(len(scores) - start)
        else:
            continue
    return answer