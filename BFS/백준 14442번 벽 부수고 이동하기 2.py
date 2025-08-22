# 백준 14442번 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    queue = deque()
    visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    queue.append((0,0,0))
    visited[0][0][0] = 1
    while queue:
        x, y, c = queue.popleft()
        if x == n-1 and y == m-1: 
            result = 1e+6
            for x in visited[n-1][m-1]:
                if x: result = min(x, result)
            return result
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                # 이전에 더 적은 횟수로 벽을 부수고 (nx, ny)에 도달했더라도, 거리가 더 길 여지도 있음
                # 그리고, 이전에 더 짧은 거리로 (nx, ny)에 도달했더라도, 벽을 더 많이 부수었을 수도 있음
                # 즉, 더 적은 횟수로, 더 짧은 거리로 (nx, ny)에 도달했을 경우에만 확실히 배제가 가능함 -> 체크하는 것이 시간복잡도 면에서 비효율적임
                # 따라서 같은 횟수로 벽을 부수었을 때, 이미 도달했다면(거리가 짧거나 같음) 이를 배제함
                visited[nx][ny][c] = visited[x][y][c] + 1
                queue.append((nx,ny,c))
            elif graph[nx][ny] == 1 and c < k and visited[nx][ny][c+1] == 0:
                    visited[nx][ny][c+1] = visited[x][y][c] + 1
                    queue.append((nx,ny,c+1))   
    return -1
n, m, k = map(int, input().split())
graph = []
for i in range(n):
    tmp = []
    row = input()
    for j in range(m):
        tmp.append(int(row[j]))
    graph.append(tmp)
print(bfs())
