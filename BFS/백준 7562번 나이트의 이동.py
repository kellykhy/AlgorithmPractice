# 백준 7562번 나이트의 이동

import sys
from collections import deque
input = sys.stdin.readline

def bfs(l, start, end):
    sx, sy = start
    ex, ey = end
    visited = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    visited[sx][sy] = 1
    queue.append((sx,sy))
    while (queue):
        x, y = queue.popleft()
        if (x == ex and y == ey):
            return (visited[x][y] - 1)
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
            
    
n = int(input())
for i in range(n):
    l = int(input())
    start = map(int, input().split())
    end = map(int, input().split())
    print(bfs(l, start, end))