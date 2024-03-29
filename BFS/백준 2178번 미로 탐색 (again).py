# 백준 2178번 미로 탐색 (again)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    directions = [(0,1),(1,0),(0,-1),(-1,0)] # 동쪽부터 시계방향
    queue = [(x,y)]
    visited[x][y] = 1
    
    while queue:
        cur_x, cur_y = queue.popleft()
        if (cur_x, cur_y) == (n-1, m-1):
            return visited[n-1][m-1]
        for i in range(4):
            new_x, new_y = cur_x + directions[i][0], cur_y + directions[i][1]
            if (new_x < 0 or new_y < 0 or new_x >= n or new_y >= m):
                continue
            elif (graph[new_x][new_y] == 0 or visited[new_x][new_y] != 0):
                continue
            queue.append((new_x, new_y))
            visited[new_x][new_y] = visited[cur_x][cur_y] + 1

n, m = map(int, input().split())
graph = [list(map(int, input.rstrip())) for _ in range(m)]

visited = [[0 for _ in range(m)] for _ in range(n) ]
bfs(0,0)
print(visited[n-1][m-1])