# 백준 15683번 감시

import sys
import copy
input = sys.stdin.readline


N,M = map(int, input().split())
graph = [[] for _ in range(N)]
cctv_list = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        graph[i].append(row[j])
        if (row[j] != 6 and row[j] != 0):
            cctv_list.append([i,j, row[j]])
  
answer = 100

# 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
cctv_directions = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
]
direction = [(0,1), (1,0), (0,-1), (-1,0)]

def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: 
                cnt += 1
    return cnt

def watch(r, c, cctv_dir, graph):
    for dir in cctv_dir:
        dr, dc = direction[dir]
        new_r = r
        new_c = c
        while (True):
            new_r += dr
            new_c += dc
            if (new_r < 0 or new_r >= N or new_c < 0 or new_c >= M):
                break
            if (graph[new_r][new_c] == 6):
                break
            if (graph[new_r][new_c] == 0):
                graph[new_r][new_c] = '#'
            

def func(k, graph):
    global answer
    if (k == len(cctv_list)):
        #print(count_zero(graph))
        answer =  min(answer, count_zero(graph))
        return
    r,c,type = cctv_list[k]
    graph_copy = copy.deepcopy(graph)
    for cctv_dir in cctv_directions[type]: # cctv_directions[type] = [[0],[1],[2],[3]]
        watch(r, c, cctv_dir, graph_copy)
        func(k+1, graph_copy)
        graph_copy = copy.deepcopy(graph)
    
func(0, graph)
print(answer)
