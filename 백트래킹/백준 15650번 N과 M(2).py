# 백준 15650번 N과 M(2)

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
            if (not visited[i]):
                if (len(ary) and (ary[-1] > i)):
                    continue
                visited[i] = 1
                ary.append(i)
                backtracking(k+1)
                visited[i] = 0
                ary.pop()
backtracking(0)