# 백준 3190번 뱀

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 # 사과표시

l = int(input().rstrip())
turn = deque()
for _ in range(l):
    s, d = input().split()
    s = int(s)
    turn.append((s, d))
    
dir = [0, 1, 2, 3] # 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur = [1,1]
dir = 0
t = 0

snake_body = deque()
snake_body.append(cur.copy())
board[cur[0]][cur[1]] = 3
turn_t, turn_dir = turn.popleft()
while (1):
    t += 1
    cur[0] += dx[dir]
    cur[1] += dy[dir]
    if (cur[0] < 1 or cur[0] > n or cur[1] < 1 or cur[1] > n or board[cur[0]][cur[1]] == 3):
        break
    apple = board[cur[0]][cur[1]]
    snake_body.append(cur.copy())
    board[cur[0]][cur[1]] = 3
    
    if not apple: # 사과 x
        tail = snake_body.popleft()
        board[tail[0]][tail[1]] = 0
        
    if (t == turn_t):
        if (turn_dir == 'D'):
            dir = (dir + 1) % 4
        elif (turn_dir == 'L'):
            dir = (dir - 1) % 4 # dir = 0 -> 3, dir = -1 -> 2
        if turn:
            turn_t, turn_dir = turn.popleft()
        
print(t)
