# 백준 2583번 영역 구하기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    queue = deque()
    paper[i][j] = 1
    queue.append((i,j))
    cnt = 1
    
    while queue:
        x,y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<m and 0<=ny<n) or paper[nx][ny]: continue
            paper[nx][ny] = 1
            queue.append((nx,ny))
            cnt += 1
            
    return cnt

m, n, k = map(int, input().split())
paper = [[0 for _ in range(n)] for _ in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

result = []
for i in range(m):
    for j in range(n):
        if paper[i][j]: continue
        result.append(bfs(i,j))
print(len(result))
print(*sorted(result))