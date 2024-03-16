# 미로 탐색 응용 (ㅎㄴㄱㅁㅌㅇㅇ 2번)
import sys

def dfs(x,y):
    dx = [0, -1, 0, 1] # 행
    dy = [1, 0, -1, 0] # 열

    vis[x][y] = 0
    
    stack = []
    stack.append((x,y))
    
    while stack:
        x, y = stack.pop()
        d = vis[x][y]
        
        for i in range(4):
            new_x = x
            new_y = y
            new_d = d
            while True:
                new_d += 1
                new_x = new_x + dx[i]
                new_y = new_y + dy[i]
                if (new_x < 0 or new_x >= N or new_y < 0 or new_y >= M):
                    break
                if (graph[new_x][new_y] == 'R' and vis[new_x-dx[i]][new_y-dy[i]] == -1):
                    stack.append((new_x-dx[i], new_y-dy[i]))
                    vis[new_x-dx[i]][new_y-dy[i]] = new_d -1
                    break
                if (graph[new_x][new_y] == 'O'):
                    return new_d
    return 0
            
#input
N, M = map(int, sys.stdin.readline().split())
start = tuple() # 시작점

graph = []
for i in range(N):
    row = []
    tmp = input()
    for j in range(M):
        row.append(tmp[j])
        if (tmp[j] == 'S'):
            start = (i,j)
    graph.append(row)

vis = [[-1] * M for _ in range(N)] # 시작점으로부터 거리 표시
print(dfs(start[0], start[1]))