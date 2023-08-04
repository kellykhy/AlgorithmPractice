# 백준 1774번 우주신과의 교감
import sys
import math
input = sys.stdin.readline

def dis(v1, v2):
    return math.sqrt((V[v1-1][0] - V[v2-1][0])**2 + (V[v1-1][1] - V[v2-1][1])**2)

N, M = map(int, input().split())
V = []
for _ in range(N):
    V.append(list(map(int, input().split())))

graph = []
for i in range(N-1):
    for j in range(i+1, N):
        graph.append((dis(i+1,j+1), i+1, j+1))
graph = list(set(graph))
graph.sort()

# 크루스칼 알고리즘
p = list(range(N+1))
total_dis = 0

def find(v):
    if (v != p[v]):
        p[v] = find(p[v])
    return p[v]

def is_diff_group(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if (p1 == p2): return 0
    return 1

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if (p1 < p2): p[p2] = p1
    else: p[p1] = p2

for _ in range(M):
    a, b = map(int, input().split())
    if (a > b): a,b = b,a
    union(a, b)

for i in range(len(graph)):
    if (is_diff_group(graph[i][1], graph[i][2])):
        total_dis += graph[i][0]
        union(graph[i][1], graph[i][2])

print("{:.2f}".format(total_dis))