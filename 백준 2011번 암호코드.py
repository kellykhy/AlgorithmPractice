# 백준 2011번 암호코드

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

code = input().rstrip()
result = 0
stack = []
memo = [0 for _ in range(len(code)+1)]
# backtracking
# k: 현재까지 배치한 (1자리) 숫자 개수
def backtracking(k):
    global stack, result
    if k == len(code):
        result += 1
        return
    n = int(code[k])
    if len(stack) and stack[-1][0] >= 0:
        tmp = stack[-1][1]*10 + n
        if tmp <= 26:
            stack.append((n, tmp))
            backtracking(k+1)
            stack.pop()
        stack.append((-1,0))
        if memo[k]: 
            result += memo[k]
        else:
            result_cpy = result
            backtracking(k)
            memo[k] =  result - result_cpy
        stack.pop()
    else:
        if n != 0:
            stack.append((n, n))
            backtracking(k+1)
            stack.pop()

backtracking(0)
print(result%1000000)