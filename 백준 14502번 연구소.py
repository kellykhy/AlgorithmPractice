# 백준 14502번 연구소 (python3 시간초과, pypy 통과)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque()
graph = []
min_cnt = 64
vacant = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            queue.append((i,j))
        elif row[j] == 0:
            vacant += 1
    graph.append(row)

def bfs():
    global min_cnt
    queue_cpy = queue.copy()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while (queue_cpy):
        x, y = queue_cpy.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m) or graph[nx][ny] or visited[nx][ny]:
                continue
            queue_cpy.append((nx, ny))
            visited[nx][ny] = 1
            cnt += 1
    min_cnt = min(cnt, min_cnt)
            
def wall(k):
    if k == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                continue
            graph[i][j] = 1
            wall(k+1)
            graph[i][j] = 0
            
wall(0)
print(vacant - min_cnt - 3)