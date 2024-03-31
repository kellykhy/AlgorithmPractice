# 백준 2178번 미로 탐색 (again)

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    queue.append((0,0))
    visited[0][0] = result + 1
    
    while (queue):
        cur_x, cur_y = queue.popleft()
        if (cur_x, cur_y) == (n-1, m-1):
            return visited[cur_x][cur_y]
        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if (new_x < 0 or new_y < 0 or new_x >= n or new_y >= m):
                continue
            elif (graph[new_x][new_y] == 0 or visited[new_x][new_y] != 0):
                continue
            queue.append((new_x, new_y))
            visited[new_x][new_y] = visited[cur_x][cur_y] + 1

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0
print(bfs())