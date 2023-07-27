# 백준 2252번 줄 세우기

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split()) # N = 학생수(노드수), M = 키 비교 횟수(간선의 수)
deg = [0] * (N+1)
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

for i in range(1, N+1):
    for nxt in adj[i]:
        deg[nxt]+=1
        
queue = []
result = []
for i in range(1, N+1):
    if deg[i] == 0:
        queue.append(i)
while (queue):
    cur = queue[0]
    queue.pop(0)
    result.append(cur)
    for nxt in adj[cur]:
        deg[nxt]-=1
        if (deg[nxt] == 0):
            queue.append(nxt)

for student in result:
    print(student, end = ' ')