# 백준 15651번 N과 M(3)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = []
visited = [0 for _ in range(N+1)]

def backtracking(k):
    if (k == M):
        print(*ary)
        return
    else:
        for i in range(1,N+1):
            visited[i] = 1
            ary.append(i)
            backtracking(k+1)
            visited[i] = 0
            ary.pop()
backtracking(0)