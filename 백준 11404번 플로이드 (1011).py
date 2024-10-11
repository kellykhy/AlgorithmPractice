# 백준 11404번 플로이드(1011)

# n개의 도시(2<=n<=100), m개의 버스(1<=m<=100,000), 도시 간 이동-> 비용 발생 => i->j 의 최소비용?
# 최단경로 알고리즘 (플로이드 와샬) : 거쳐가는 도시를 순회하면서 비용 값 갱신
import sys

input = sys.stdin.readline
INF = 1e+7
n = int(input())
m = int(input())
cost = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)
for i in range(n):
    cost[i][i] = 0
for mid in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][mid]+cost[mid][j])
for i in range(n):
    for j in range(n):
        print(cost[i][j], end = ' ')
    print()