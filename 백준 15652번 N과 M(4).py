# 백준 15652번 N과 M(4)

import sys
input = sys.stdin.readline

def backtracking(k, ary):
    if k == M:
        print(*ary)
        return
    if not len(ary):
        for x in range(1, N+1):
            ary.append(x)
            backtracking(k+1, ary)
            ary.pop()
    else:
        for x in range(ary[-1], N+1):
            ary.append(x)
            backtracking(k+1, ary)
            ary.pop()
        
def solution():
    global N, M
    N, M = map(int, input().split())
    backtracking(0, [])

solution()