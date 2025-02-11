# 백준 2667번 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    nh = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while (queue):
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n or not mapp[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            queue.append((nx,ny))
            nh += 1
    return nh

n = int(input())
mapp = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
n_house = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or not mapp[i][j]:
            continue
        n_house.append(bfs(i,j))

print(len(n_house))
n_house.sort()
for i in range(len(n_house)):
    print(n_house[i])