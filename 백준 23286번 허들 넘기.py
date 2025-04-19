# 백준 23286번 허들 넘기

import sys
input = sys.stdin.readline

INF = 1000000

N, M, T = map(int, input().split())
board = [[INF for _ in range(N+1)] for _ in range(N+1)] # board[a][b] : a -> b 최대 높이의 최솟값
for i in range(1, N+1):
    board[i][i] = 0
for _ in range(M):
    u, v, h = map(int, input().split())
    board[u][v] = h
    
for m in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            board[a][b] = min(board[a][b], max(board[a][m], board[m][b]))
            
for _ in range(T):
    s, e = map(int, input().split())
    if board[s][e] != INF:
        print(board[s][e])
    else:
        print(-1)