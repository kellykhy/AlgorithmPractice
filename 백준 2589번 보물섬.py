# 백준 2589번 보물섬

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append((x,y))
    visited[x][y] = 1
    n = 0
    while queue:
        x,y = queue.popleft()
        n = visited[x][y]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] : continue
            if mapp[nx][ny] == 'W': continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    return n-1
    

N, M = map(int, input().split())
mapp = []
lands = []
for i in range(N):
    row = input().strip()
    tmp = []
    for j in range(M):
        tmp.append(row[j])
        if row[j] == 'L':
            lands.append((i,j))
    mapp.append(tmp)

result = 0
for x, y in lands:
    result = max(result, bfs(x,y))

print(result)