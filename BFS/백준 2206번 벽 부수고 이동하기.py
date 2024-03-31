# 백준 2206번 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline

#input
n, m = map(int, input().split()) # 0:길, 1:벽
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs():
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue.append((0,0,0))
    visited[0][0][0] = 1
    
    while (queue):
        x, y, crashed = queue.popleft()
        
        if (x == n-1 and y == m-1):
            return visited[x][y][crashed]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (graph[nx][ny] == 0 and visited[nx][ny][crashed] == 0): # 벽 X, 방문 X
                visited[nx][ny][crashed] = visited[x][y][crashed] + 1
                queue.append((nx,ny,crashed))
            elif (graph[nx][ny] == 1 and visited[nx][ny][crashed] == 0): # 벽 O, 방문 X
                if (crashed == 0):
                    visited[nx][ny][1] = visited[x][y][crashed] + 1
                    queue.append((nx,ny,1))
    return -1
        
visited = [[[0]* 2 for _ in range(m)] for _ in range(n)] # a, b = (벽 부수기 전, 벽 부수고 난 후)
print(bfs())