# 백준 1600번 말이 되고픈 원숭이

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    dhx, dhy = [1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]
    visited = [[[0 for _ in range(K+1)] for _ in range(w)] for _ in range(h)]
    
    queue.append((0, 0, K))
    visited[0][0][K] = 1
    
    if w == 1 and h == 1:
        return 0
    
    while queue:
        x, y, k = queue.popleft()
        if x == h-1 and y == w-1:
            result = 40000
            for x in visited[x][y]:
                if x == 0: continue
                if result > x: result = x
            return result-1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if graph[nx][ny] or visited[nx][ny][k]: continue
            visited[nx][ny][k] = visited[x][y][k] + 1
            queue.append((nx, ny, k))
        if k:
            for i in range(8):
                nx, ny = x + dhx[i], y + dhy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
                if graph[nx][ny] or visited[nx][ny][k-1]: continue
                visited[nx][ny][k-1] = visited[x][y][k] + 1
                queue.append((nx, ny, k-1))
    return -1

K = int(input().rstrip())
w, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))


print(bfs())