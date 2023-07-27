# 백준 1707번 이분 그래프

import sys
sys.setrecursionlimit(10 ** 6)

# 입력받기
nodes = []
graphs = []

k = int(sys.stdin.readline())

for i in range(k):
    v, e = [int(x) for x in sys.stdin.readline().split()]
    graph = [[] for _ in range(v+1)]
    node = []
    for j in range(e):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        graph[a].append(b)
        graph[b].append(a)
        node.append([a,b])
    graphs.append(graph)
    nodes.append(node)
#print("nodes: ", nodes)


# dfs
def dfs(graph, cur, visited, color):
    visited[cur] = 1
    check[cur] = color
    #print(cur, end = ' ')
    for i in graph[cur]:
        if (visited[i]): continue
        visited[i] = 1
        dfs(graph, i, visited, color*(-1))

for i in range(k):
    check = [0 for _ in range(len(graphs[i]))]
    flag= 0
    visited = [0 for _ in range(len(graphs[i]))]
    dfs(graphs[i], 1, visited, 1)
    #print(check)
    flag = 0
    for a, b in nodes[i]:
        #print("a:", a, "b:", b)
        if (check[a]+check[b] != 0):
            flag = 1
            break
    if (flag == 1): print("NO")
    else: print("YES")
    check.clear()