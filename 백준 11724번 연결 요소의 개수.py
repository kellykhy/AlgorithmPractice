# 백준 11724번 연결 요소의 개수

# 무방향 그래프 (N:정점의 개수, M:간선의 개수)

import sys
input = sys.stdin.readline
from collections import deque

#input
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0 #연결 요소의 개수
visited = [0] * (N+1)
queue = deque()

def bfs(v):
    visited[v] = 1
    queue.append(v)
    while(queue):
        cur_v = queue.popleft()
        for new_v in graph[cur_v]:
            if (new_v < 1 or new_v > N): # 굳이 필요 없을지도
                continue
            if (visited[new_v] == 1):
                continue
            visited[new_v] = 1
            queue.append(new_v)
            
        
for v in range(1, N+1):
    if (visited[v] == 0):
        result += 1
        bfs(v)
print(result)