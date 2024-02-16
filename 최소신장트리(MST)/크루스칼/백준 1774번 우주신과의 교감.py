# 백준 1774번 우주신과의 교감
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

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
p = [-1] * (N+1)
total_dis = 0

def find(v):
    print("v=", v)
    if (p[v] < 0): return v
    p[v] = find(p[v])
    return p[v]

def union(p1, p2):
    if (p[p1] == p[p2]): 
        p[p1]-=1
    if (p[p1] < p[p2]): 
        p[p2] = p1
    else: 
        p[p1] = p2

for _ in range(M):
    a, b = map(int, input().split())
    if (a > b): a,b = b,a
    p1 = find(a)
    p2 = find(b)
    union(p1, p2)

for i in range(len(graph)):
    p1 = find(graph[i][1])
    p2 = find(graph[i][2])
    if (p1 != p2):
        total_dis += graph[i][0]
        union(p1, p2)

print("{:.2f}".format(total_dis))
