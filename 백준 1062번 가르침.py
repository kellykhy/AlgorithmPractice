# 백준 1062번 가르침
# N개의 숫자를 비트화 (ex. 0010001) => N(=50) x 15
# 사용된 철자(5개 이외) 중 2개 선택해서 비트연산(AND) 수행

from itertools import combinations

N, K = map(int, input().split())
essentials = {'a', 'c', 'i', 'n', 't'}
additionals = set()

words = []

if K < 5: 
    print(0)
else:
    for _ in range(N):
        word = input()[4:-4]
        word_bit = 0
        for l in word:
            if l in essentials: continue
            l = ord(l)-ord('a')
            word_bit |= (1 << l)
            additionals.add(l)
        words.append(word_bit)

    ans = 0
    if len(additionals) <= K-5: 
        ans = N
    else: 
        for comb in combinations(additionals, K-5):
            selected = 0
            for n in comb:
                selected |= (1 << n)
            cnt = 0
            for word in words:
                if selected & word == word:
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)