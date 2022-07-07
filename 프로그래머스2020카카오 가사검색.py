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

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))