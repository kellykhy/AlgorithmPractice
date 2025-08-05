# 백준 2638번 치즈

import sys
from collections import deque
input = sys.stdin.readline

def melt_cheese():
    global cheese
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    # 초기값 탐색
    for i in range(N):
        flag = 0
        for j in range(M):
            if cheese[i][j] == 0:
                flag = 1
                queue.append((i,j))
                visited[i][j] = 1
                break
        if flag == 1:
            break
    flag2 = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M): continue
            if cheese[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
            elif cheese[nx][ny] == 1:
                visited[nx][ny] += 1
                flag2 = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                cheese[i][j] = 0
    if flag2 == 0: return False
    else: return True

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))
sec = 0

while melt_cheese():
    sec += 1
print(sec)