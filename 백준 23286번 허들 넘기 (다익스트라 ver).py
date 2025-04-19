# 백준 23286번 허들 넘기 (다익스트라 ver.)

import sys
import heapq
input = sys.stdin.readline

INF = 1000001
def di(st):
    ary = [INF for _ in range(N+1)] # 최대 높이의 최솟값
    ary[st] = 0
    heap = [(0, st)]
    while heap:
        c, v = heapq.heappop(heap)
        
        for nv, nc in d[v]:
            tmp = max(c, nc)
            
            if tmp < ary[nv]:
                ary[nv] = tmp
                heapq.heappush(heap, (tmp, nv))
    return ary
        
N, M, T = map(int, input().split())
d = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, h = map(int, input().split())
    d[u].append((v, h))

arys = [[]]
for st in range(1, N+1):
    arys.append(di(st))
    
for _ in range(T):
    s, e = map(int, input().split())
    print(arys[s][e]) if arys[s][e] != INF else print(-1)