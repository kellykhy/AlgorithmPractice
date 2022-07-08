# 프로그래머스2020카카오 가사검색(2)

from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    word_list = defaultdict(list)
    rev_word_list = defaultdict(list)
    for word in words:
        word_list[len(word)].append(word)
        rev_word_list[len(word)].append(word[::-1])
    for key in word_list.keys():
        word_list[key].sort()
        rev_word_list[key].sort()
    for query in queries:
        start = query.replace('?', 'a')
        end = query.replace('?', 'z')
        if query[0] == '?':
            lst = rev_word_list[len(query)]
            s = bisect_left(lst, start[::-1])
            e = bisect_right(lst, end[::-1])
        else:
            lst = word_list[len(query)]
            s = bisect_left(lst, start)
            e = bisect_right(lst, end)
        answer.append(e-s)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))