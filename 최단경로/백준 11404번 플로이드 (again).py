# 백준 11404번 플로이드 (again)
# n개의 도시, m개의 버스
# 도시 A->B의 최소비용?


import sys

INF = int(1e+7)
input = sys.stdin.readline
n = int(input()) # 도시의 수
m = int(input()) # 버스의 수
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)
for i in range(1, n+1):
    distance[i][i] = 0

for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][x] + distance[x][j])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end = ' ')
        else: print(distance[i][j], end = ' ')
    print()
