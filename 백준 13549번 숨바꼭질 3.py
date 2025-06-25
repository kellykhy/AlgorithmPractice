# 백준 13549번 숨바꼭질 3
# 0-1 BFS

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def zero_one_bfs():
    visited = [0 for _ in range(100001)]
    queue = deque()
    
    queue.append((n, 0))
    
    while queue:
        x, s = queue.popleft()
        visited[x] = 1
        if x == k:
            return s
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if not (0 <= nx <= 100000) or visited[nx]: continue
            if i < 2:
                queue.append((nx, s+1))     
            else:
                queue.appendleft((nx, s))
    
print(zero_one_bfs())