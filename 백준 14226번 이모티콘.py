# 백준 14226번 이모티콘

from collections import deque

S = int(input())

def bfs():
    queue = deque()
    queue.append((1,0,0))
    visited = [[0 for _ in range(1002)] for _ in range(1002)]
    visited[1][0] = 1

    while queue:
        x, c, t = queue.popleft() # x : 화면, c : 클립보드 스티커 개수, t: 시간
        if x == S:
            return t
        # case1
        nc = x
        queue.append((x, nc, t+1))
        # case2
        nx = x - 1
        if 1002 > nx > 0 and not visited[nx][c]:
            queue.append((nx, c, t+1))  
            visited[nx][c] = 1
        # case3
        nx = x + c
        if 1002 > nx > 0 and not visited[nx][c]:
            queue.append((nx, c, t+1))
            visited[nx][c] = 1

print(bfs())