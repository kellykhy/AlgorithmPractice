# 2번
import sys
sys.setrecursionlimit(10**6)


edges = [[2,3],[4,3],[1,1],[2,1]] #given

answer = [0, 0, 0, 0]
count = [0 for i in range(len(edges)+1)]
ex = 0
max = 1
for i in range(len(edges)):
    count[edges[i][0]] += 1
    if (count[edges[i][0]] > 1):
        ex = edges[i][0]
        answer[0] = ex
    if (max < edges[i][0]):
        max = edges[i][0]        
    elif (max < edges[i][1]):
        max = edges[i][1]

map = [[0 for i in range(max+1)] for j in range(max+1)]
for edge in edges:
    if (edge[0] != ex):
        map[edge[0]][edge[1]] = 1




visited = [0 for i in range(max+1)]
visited[ex] = 1

def dfs(map, n, flag):
    for i in range(1, len(map[0])+1):
        if (map[n][i] == 1):
            visited[i] += 1
            if (visited[i] == 2):
                if (flag == 1):
                    return 1
                dfs(map, i, 1)
            if (flag == 1):
                return 3
            dfs(map, i, 0)
    return 2

for i in range(1, max+1):
    if (visited[i] == 0):
        visited[i] += 1
        answer[dfs(map, i, 0)] += 1
    


            
print(answer)