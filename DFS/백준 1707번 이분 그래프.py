# 백준 1707번 이분 그래프 (https://ji-gwang.tistory.com/293)

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# dfs
def dfs(cur, color):
    visited[cur] = color
    for nxt in graph[cur]:
        if (not visited[nxt]):
            result = dfs(nxt, -color)
            if (result == False):
                return result
        elif (visited[cur] == visited[nxt]):
            return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v+1)
    for i in range(1, v+1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break
    print("YES" if result else "NO")
