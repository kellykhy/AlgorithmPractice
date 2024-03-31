# 백준 10026번 적록색약

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
painting = [(list(input().rstrip())) for _ in range(n)]
result = []

def bfs(i,j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue.append((i,j))
    visited[i][j] = 1
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if (0<=new_x<n and 0<=new_y<n and visited[new_x][new_y]==0):
                if (painting[x][y] != painting[new_x][new_y]):
                    continue
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1
            

cnt = 0  
queue = deque()
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (visited[i][j] == 0):
            cnt += 1
            bfs(i,j)
two_cnt = cnt # 적록색약 X

for i in range(n):
    for j in range(n):
        if (painting[i][j] == 'G'):
            painting[i][j] = 'R'
        visited[i][j] = 0

cnt = 0
for i in range(n):
    for j in range(n):
        if (visited[i][j] == 0):
            cnt += 1
            bfs(i,j)
three_cnt = cnt # 적록색약 O
print(two_cnt, three_cnt)