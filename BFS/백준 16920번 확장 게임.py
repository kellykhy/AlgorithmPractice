# 백준 16920번 확장 게임

import sys
from collections import deque
input = sys.stdin.readline

n, m, p = map(int, input().split())
S = [0] + list(map(int, input().split()))
queues = [deque() for _ in range(p+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = []
result = [0 for _ in range(p+1)]

for i in range(n):
    row = []
    for j, elem in enumerate(input()):
        row.append(elem)
        if ('1' <= elem <= '9'):
           queues[int(elem)].append((i,j,0))
           result[int(elem)] += 1
    board.append(row)

is_continue = 1
round = 0
while (is_continue):
    round += 1
    is_continue = 0
    for player in range(1, p+1):
        s = round * S[player] # 1 * 2 = 2
        queue = queues[player]
        while (queue):
            if (queue[0][2] == s):
                break
            x, y, d = queue.popleft()
            for i in range(4):
                nx, ny, nd = x + dx[i], y + dy[i], d + 1
                if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                    continue
                if (board[nx][ny] != '.'):
                    continue
                board[nx][ny] = str(player)
                result[player] += 1
                queue.append((nx, ny, nd))
        if queue:
            is_continue = 1
            
print(' '.join(map(str, result[1:])))