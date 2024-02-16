# 백준 5567번 결혼식

import sys
input = sys.stdin.readline
from collections import deque

#input
n = int(input()) # 정점의 수
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
result = 0 # 초대하는 동기의 수
visited = [0] * (n+1)

def bfs(v):
    global result
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while(queue):
        cur_v = queue.popleft()
        for new_v in graph[cur_v]:
            if (visited[new_v]): continue
            queue.append(new_v)
            visited[new_v] = visited[cur_v] + 1
            if (visited[new_v] < 4) : result += 1
      
bfs(1)
print(result)