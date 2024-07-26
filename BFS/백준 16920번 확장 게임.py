# 백준 16920번 확장 게임

import sys
from collections import deque
input = sys.stdin.readline

n, m, p = map(int, input().split())
S = [0] + list(map(int, input().split()))
queue = [deque() for _ in range(p+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = []
distance = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    row_list = []
    row = input()
    for j in range(m):
       row_list.append(row[j])
       if ('1' <= row[j] <= '9'):
           queue[int(row[j])].append((i,j,0))
    board.append(row_list)

queue_status = [0] + [0 for _ in range(p)] # 큐가 비면 1
round = 0
while (sum(queue_status) < p):
    round += 1
    for player in range(1, p+1):
        s = round * S[player] # 1 * 2 = 2
        while(queue[player]):
            topx, topy, topd = queue[player][0]
            if (topd == s):
                break
            x, y, d = queue[player].popleft()
            for i in range(4):
                nx, ny, nd = x + dx[i], y + dy[i], d + 1
                if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                    continue
                if (board[nx][ny] != '.'):
                    continue
                board[nx][ny] = board[x][y]
                queue[player].append((nx, ny, nd))
        if not queue[player]:
            queue_status[player] = 1

result = [0 for _ in range(p)]
for i in range(n):
    for j in range(m):
        if ('1' <= board[i][j] <= '9'):
            result[int(board[i][j])-1] += 1
            
print(' '.join(map(str, result)))