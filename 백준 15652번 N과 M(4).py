# 백준 15652번 N과 M(4)

import sys
input = sys.stdin.readline

def backtracking(k, st, ary):
    if k == M:
        print(*ary)
        return
    for x in range(st, N+1):
        ary.append(x)
        backtracking(k+1, x, ary)
        ary.pop()
        
def solution():
    global N, M
    N, M = map(int, input().split())
    backtracking(0, 1, [])

solution()