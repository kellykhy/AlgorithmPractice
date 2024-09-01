# 백준 11404번 플로이드 (again)

import sys
input = sys.stdin.readline

INF = 100001

n = int(input())
m = int(input())

board = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    board[i][i] = 0
    
for _ in range(m):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            board[a][b] = min(board[a][i] + board[i][b], board[a][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == INF:
            print(0, end = ' ')
        else:
            print(board[i][j], end = ' ')
    print()
