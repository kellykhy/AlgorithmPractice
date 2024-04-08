# 백준 7576번 토마토

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0] 
    cnt = 0 # 안익은 토마토->익은 토마토 횟수
    result = 0
    
    while (queue):
        x,y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if (new_x < 0 or new_y < 0 or new_x >= n or new_y >= m):
                continue
            if (graph[new_x][new_y] != 0):
                continue
            queue.append((new_x, new_y))
            graph[new_x][new_y] = graph[x][y] + 1
            result = graph[new_x][new_y]
            cnt += 1
    if (target == 0):
        return 0
    elif (cnt == target):
        return result - 1
    else:
        return -1

m, n = map(int, input().split()) # m:열의 수, n:행의 수
graph = [[] for _ in range(n)]
target = 0 # 익지 않은 토마토의 개수
queue = deque()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        graph[i].append(row[j])
        if (row[j] == 0):
            target += 1
        elif (row[j] == 1):
            queue.append((i,j))
print(bfs())