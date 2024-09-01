# 백준 11967번 불켜기

import sys
from collections import deque
input = sys.stdin.readline

switchInfo = {}
N, M = map(int, input().split())
light = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x, y, a, b = map(int, input().split())
    if (x,y) in switchInfo:
        switchInfo[(x,y)].append((a,b))
    else:
        switchInfo[(x,y)] = [(a,b)]
        
def bfs():
    light[1][1] = 1
    
    queue = deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue.append((1,1))
    
    while (queue):
        x, y = queue.popleft()
        visited[1][1] = 1
        
        if ((x,y) in switchInfo):
            for (a,b) in switchInfo[(x,y)]:
                if not light[a][b]:
                    light[a][b] = 1
                    for i in range(4):
                        na, nb = a + dx[i], b + dy[i]
                        if (na < 1 or na > N or nb < 1 or nb > N):
                            continue
                        if visited[na][nb] == 1:
                            queue.append((na, nb))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx < 1 or nx > N or ny < 1 or ny > N):
                continue
            if visited[nx][ny]:
                continue
            if not light[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = 1

bfs()
    
result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if light[i][j] == 1:
            result += 1
print(result)
