# 2606번 바이러스

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)] #인접 리스트
visited = [0 for _ in range(n+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
def dfs(graph, n):
    for i in graph[n]:
        if (visited[i] == 0):
            visited[i] = 1
            dfs(graph, i)
dfs(graph, 1)
print(sum(visited) - 1)
