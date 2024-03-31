# 백준 2178번 미로 탐색

import sys

def bfs(x,y):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0] 

    vis[x][y] = 1
    queue = [(x, y)]
    
    while queue:
        x, y = queue.pop()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (new_x < 0 or new_x >= N or new_y < 0 or new_y >= M):
                continue
            if (m[new_x][new_y] == 0 or vis[new_x][new_y] != -1):
                continue
            vis[new_x][new_y] = vis[x][y] + 1
            queue.insert(0, (new_x,new_y))
    return vis[N-1][M-1]
            
#input
N, M = map(int, sys.stdin.readline().split())
m = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

vis = [[-1] * M for _ in range(N)] # (1,1)로부터의 거리 표시
print(bfs(0,0))
