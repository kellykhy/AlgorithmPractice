# 백준 1759번 암호 만들기

import sys
from copy import deepcopy

input = sys.stdin.readline

l, c = map(int, input().split())
letters = list(input().split())
letters.sort()

result = []

def backtracking(k, start):
    if k == l:
        cnt = 0
        for r in result:
            if r in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        if 1 <= cnt <= l-2:
            print(''.join(result))
        return
    for i in range(start, c):
        result.append(letters[i])
        backtracking(k+1, i+1)
        result.pop()
        
backtracking(0)