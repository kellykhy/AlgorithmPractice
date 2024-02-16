# 백준 11724번 연결 요소의 개수 (DFS - 재귀&비재귀)
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

# DFS 사용(비재귀 - 덜 직관적인 방식)
'''
result = 0 #연결 요소의 개수
visited = [0] * (N+1)
stack = []

def dfs(v):
    visited[v] = 1
    stack.append(v)
    while (stack):
        cur_v = stack.pop()
        for new_v in graph[cur_v]:
            if (visited[new_v] == 1):
                continue
            visited[new_v] = 1
            stack.append(new_v)
for v in range(1, N+1):
    if (visited[v] == 0):
        result += 1
        dfs(v)
print(result)
'''


# DFS 사용(재귀 - 좀더 직관적인 방식)
sys.setrecursionlimit(10**7)
result = 0 #연결 요소의 개수
visited = [0] * (N+1)

def dfs(v):
    visited[v] = 1
    for new_v in graph[v]:
        if (visited[new_v] == 1):
            continue
        dfs(new_v)
            
for v in range(1, N+1):
    if (visited[v] == 0):
        result += 1
        dfs(v)
print(result)
