# 백준 11725번 트리의 부모 찾기

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    p[1] = 1
    while(queue):
        v = queue.popleft()
        for nv in adj[v]:
            if p[nv]: continue
            p[nv] = v
            queue.append(nv)

n = int(input().rstrip())
adj = [[] for _ in range(n+1)]
p = [0 for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
    
bfs()
result = p[2:]
for x in result:
    print(x)