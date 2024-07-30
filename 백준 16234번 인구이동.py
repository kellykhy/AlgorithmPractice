# 백준 16234번 인구이동

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    locations = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    queue.append((x,y))
    locations.append((x, y))
    visited[x][y] = 1
    gsumm = continent[x][y]
    gcnt = 1
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            pop_diff = abs(continent[x][y] - continent[nx][ny])
            if (visited[nx][ny] or pop_diff < l or pop_diff > r):
                continue
            visited[nx][ny] = 1
            queue.append((nx, ny))
            locations.append((nx, ny))
            gsumm += continent[nx][ny]
            gcnt += 1
    
    # 인구이동 (continent 값 조정)
    for x, y in locations:
        continent[x][y] = int(gsumm/gcnt)
        
    return gcnt > 1

n, l, r = map(int, input().split())

continent = []
for i in range(n):
    continent.append(list(map(int, input().split())))
days = 0
while (1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    moved = False
    adj = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                moved |= bfs(i,j) # or 연산자 (moved = moved | bfs(i,j))
    if not moved:
        break
    
    days += 1

print(days)