# 백준 7576번 토마토

import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split()) # N행, M열
tomatoes = [list(map(int, input().split())) for _ in range(N)]

yet = 0


def bfs():
    turn = 0 # 안익은 토마토가 익은 토마토가 된 횟수
    result = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
        
    while deque:
        cur_x, cur_y, cur_d = deque.popleft()
        for n in range(4):
            new_x = cur_x + dx[n]
            new_y = cur_y + dy[n]
            new_d = cur_d + 1
            if (0 <= new_x < N and 0 <= new_y < M and tomatoes[new_x][new_y] == 0):
                tomatoes[new_x][new_y] = 1
                deque.append((new_x, new_y, new_d))
                turn += 1
                result = max(result, new_d)
    if (turn == yet):
        return result
    else:
        return -1
    
deque = deque()
for i in range(N):
    for j in range(M):
        if (tomatoes[i][j] == 1):
            deque.append((i,j,0))
        elif (tomatoes[i][j] == 0):
            yet += 1
if (yet == 0):
    print(0)
else:
    print(bfs())
    
    
# 1st try : list 사용 -> 시간초과
# 2nd try : collections.deque 사용 -> 통과
