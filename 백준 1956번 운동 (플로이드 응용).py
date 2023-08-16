# 백준 1956번 운동 (좀 더 나은 풀이법)
# 플로이드 알고리즘에서 그래프(D)의 대각선 요소를 0으로 초기화시키지 않은 채(매우 큰 수로 둔 채) 3중 for문을 돌리면
# 3중 for문을 돌고 나서 대각선 요소에 저장되는 값은 ?
# 해당 지점(i)에서 다른 지점 거쳐서 다시 해당 지점(i)로 돌아오는 최소 비용이 저장됨.

import sys
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
D = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    D[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if (D[i][k] + D[k][j] < D[i][j]):
                D[i][j] = D[i][k] + D[k][j]

result = INF
for i in range(1, V+1):
    result = min(result, D[i][i]) #위 코드와 다른 점

if (result == INF):
    print(-1)
else:
    print(result)