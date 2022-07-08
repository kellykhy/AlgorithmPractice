# 프로그래머스2020카카오 가사검색

def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        for word in words:
            if len(query) != len(word):
                continue
            for i in range(len(query)):
                if query[i] != '?' and query[i] != word[i]:
                    break
                if i == len(query)-1:
                    count += 1
        answer.append(count)
    return answer

def solution2(words, queries):
    answer = []
    reversed_words = ["".join(reversed(word)) for word in words]
    for query in queries:
        if query[0] == '?':
            reversed_query = "".join(reversed(query))
            lower_bound = reversed_query.replace('?', 'a')
            upper_bound = reversed_query.replace('?', 'z')
            count = 0
            for word in reversed_words:
                if len(word) != len(query):
                    continue
                if word >= lower_bound and word <= upper_bound:
                    count += 1
        else:
            lower_bound = query.replace('?', 'a')
            upper_bound = query.replace('?', 'z')
            count = 0
            for word in words:
                if len(word) != len(query):
                    continue
                if word >= lower_bound and word <= upper_bound:
                    count += 1
        answer.append(count)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution2(words, queries))

## 제한사항 : 검색 키워드는 '?'가 하나 이상 포함, 접두사 or 접미사 중 하나로만 주어짐.