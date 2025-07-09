# 백준 1043번 거짓말쟁이

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
l = list(map(int, input().split()))

if len(l) == 0:
    print(M)
else:
    adj = [[] for _ in range(N+1)]

    trues = set(l[1:])
    queue = deque(l[1:])
    
    parties = []
    for _ in range(M):
        l = list(map(int, input().split()))

        P = l[1:]
        parties.append(P)
        for x in P:
            for y in P:
                adj[x].append(y)
                adj[y].append(x)
    while queue:
        x = queue.popleft()
        for nx in adj[x]:
            if nx in trues: continue
            trues.add(nx)
            queue.append(nx)
    tmp = 0
    for i in range(M):
        for j in parties[i]:
            if j in trues:
                tmp += 1
                break

    print(M-tmp)