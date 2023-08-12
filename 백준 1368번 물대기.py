#백준 1368번 물대기
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
well = []
for i in range(N):
    well.append(int(input()))
for i in range(N):
    cost = list(map(int, input().split()))
    graph[i] = cost
    graph[i].append(well[i])
graph[N] = well + [0]

# 크루스칼 알고리즘
# (비용, 정점1, 정점2) 오름차순 정렬 -> Union Find를 통해 모든 간선 연결
group = [i for i in range(N+1)]
p = [-1] * (N+1)

def find(v):
    if p[v] < 0: return v
    p[v] = find(p[v])
    return p[v]

def is_diff_group(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if (p1 == p2): return 0
    if (p[p1] == p[p2]): p[p1]-=1
    if (p[p1] < p[p2]): p[p2] = p1
    else: p[p1] = p2
    return 1

result = 0 # 최소 비용
edge = []
for i in range(N+1):
    for j in range(i+1, N+1):
        edge.append([graph[i][j], i, j])
edge.sort()
for e in edge:
    print("rank: ", p)
    if is_diff_group(e[1], e[2]):
        result += e[0]
print(result)

'''

import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
well = []
for i in range(N):
    well.append(int(input()))
for i in range(N):
    cost = list(map(int, input().split()))
    graph[i] = cost
    graph[i].append(well[i])
graph[N] = well + [0]

# 크루스칼 알고리즘
# (비용, 정점1, 정점2) 오름차순 정렬 -> Union Find를 통해 모든 간선 연결
group = [i for i in range(N+1)]
p = [x for x in range(N+1)]

def find(v):
    if (p[v] == v) : return v
    p[v] = find(p[v])
    return p[v]

def is_diff_group(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if (p1 == p2): return 0
    if (p1 < p2):
        p[p1] = p2
    else:
        p[p2] = p1
    return 1

result = 0 # 최소 비용
edge = []
for i in range(N+1):
    for j in range(i+1, N+1):
        edge.append([graph[i][j], i, j])
edge.sort()

for e in edge:
    if is_diff_group(e[1], e[2]):
        result += e[0]
print(result)