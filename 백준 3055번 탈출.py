#백준 3055번 탈출

import sys
from collections import deque

input = sys.stdin.readline

R,C = map(int, input().split())
forest = []

visited = [[0 for _ in range(C)] for _ in range(R)]
queue = deque()
w_queue = deque()

x, y = 0, 0
for i in range(R):
    row = []
    tmp = input()
    for j in range(C):
        row.append(tmp[j])
        if tmp[j] == 'S':
            visited[i][j] = 1
            queue.append((i,j,1))
            row[j] = '.'
        elif tmp[j] == '*':
            w_queue.append((i,j))
    forest.append(row)
        
def move_water():
    n = len(w_queue)
    for _ in range(n):
        x,y = w_queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<R and 0<=ny<C): continue
            if forest[nx][ny] == '.':
                forest[nx][ny] = '*'
                w_queue.append((nx, ny))

def bfs():
    n = 0
    while queue:
        x,y,c= queue.popleft()
        if visited[x][y] == n+1:
            n = visited[x][y]
            move_water()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<R and 0<=ny<C) or visited[nx][ny]: continue
            if forest[nx][ny] == 'D':
                return visited[x][y]
            elif forest[nx][ny] == '.':
                queue.append((nx, ny, c+1))
                visited[nx][ny] = visited[x][y] + 1
                
    return 0

m = bfs()
if m == 0:
    print('KAKTUS')
else:
    print(m)
                
        