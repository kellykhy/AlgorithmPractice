# 백준 1956번 운동 
# 다익스트라(heapq)로 다시 풀어보기. Python3에서도 통과되는지 보기.

import sys
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
D = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    D[a][b] = c
#for i in range(1, V+1):
#    D[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if (D[i][k] + D[k][j] < D[i][j]):
                D[i][j] = D[i][k] + D[k][j]

result = INF
visited = []
for i in range(1, V+1):
    for j in range(i+1, V+1):
        if (i not in visited) and (j not in visited) and (D[i][j] != INF) and (D[j][i] != INF):
            if (result > D[i][j] + D[j][i]):
                result = D[i][j] + D[j][i]
                visited.extend([i,j])

if (result == INF):
    print(-1)
else:
    print(result)
