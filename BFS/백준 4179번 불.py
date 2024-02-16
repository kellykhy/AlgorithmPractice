# 백준 4179번: 불!

import sys
input = sys.stdin.readline
from collections import deque


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def fire_path():
    while (F):
        x, y = F.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < R and 0 <= new_y < C):
                continue
            if maze[new_x][new_y] == '#' or fire[new_x][new_y]:
                continue
            fire[new_x][new_y] = fire[x][y] + 1
            F.append((new_x, new_y))

def bfs():
    while (J):
        x, y = J.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not (0 <= new_x < R and 0 <= new_y < C):
                return jihun[x][y]
            if (maze[new_x][new_y] == '#' or jihun[new_x][new_y]):
                continue
            if (fire[new_x][new_y] and jihun[x][y] + 1 >= fire[new_x][new_y]):
                continue
            jihun[new_x][new_y] = jihun[x][y] + 1
            J.append((new_x, new_y))
    return 0


#input  
R, C = map(int, input().split()) # R행, C열
F, J = deque(), deque()
maze = []

fire = [[0] * C for _ in range(R)] #불이 번진 구역
jihun = [[0] * C for _ in range(R)] #지훈이 이동 경로

for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "J":
            jihun[i][j] = 1
            J.append((i,j))
        elif maze[i][j] == "F":
            fire[i][j] = 1
            F.append((i,j))
     

#result
fire_path()
result = bfs()
if (result == 0):
    print("IMPOSSIBLE")
else:
    print(result)
