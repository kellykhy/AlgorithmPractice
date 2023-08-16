# 백준 11780번 플로이드2

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
D = [[INF]*(n+1) for _ in range(n+1)]
nxt = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    nxt[a][b] = b
    if (c < D[a][b]):
        D[a][b] = c
for i in range(1, n+1):
    D[i][i] = 0

for m in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (D[i][m] + D[m][j]) < D[i][j]:
                D[i][j] = D[i][m] + D[m][j]
                nxt[i][j] = nxt[i][m]
for i in range(1, n+1):
    for j in range(1, n+1):
        if D[i][j] == INF: 
            print(0, end = ' ')
        else: 
            print(D[i][j], end = ' ')
    print()
for a in range(1, n+1):
    for b in range(1, n+1):
        if (D[a][b] == INF or D[a][b] == 0): 
            print(0)
        else:
            x = a
            route = [a]
            while not(nxt[x][b] == b):
                x = nxt[x][b]
                route.append(x)
            route.append(b)
            print(len(route), end = ' ')
            for x in route:
                print(x, end = ' ')
            print()