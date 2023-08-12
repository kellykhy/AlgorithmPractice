#백준 11404번 플로이드

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[0]*(n+1)] + [[0] + [INF]*n for _ in range(n)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c =  map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for m in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][m] + graph[m][j], graph[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF: 
            print(0, end = ' ')
        else: 
            print(graph[i][j], end = ' ')
    print()