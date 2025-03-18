# 백준 1325번 효율적인 해킹

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    comp1, comp2 = map(int, input().split()) # comp2 해킹 -> comp1 해킹 가능
    adj[comp2].append(comp1)


def bfs(n):
    visited_node = [0 for _ in range(N+1)]
    queue = deque()
    
    queue.append(n)
    visited_node[n] = 1
    cnt = 1
    
    while queue:
        n = queue.popleft()
        for x in adj[n]:
            if visited_node[x]: continue # 추가
            queue.append(x)
            visited_node[x] = 1
            cnt += 1
    return cnt

result = [0 for _ in range(N+1)]
max_cnt = 0
for n in range(1, N+1):
    result[n] = bfs(n)
    max_cnt = max(max_cnt, result[n])
    
for n in range(1, N+1):
    if result[n] == max_cnt:
        print(n, end = ' ')