import sys
from collections import deque
input = sys.stdin.readline

def grow(selection): # bfs
    global avail
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    result = 0
    
    for i in range(len(avail)):
        if selection[i]:
            x, y = avail[i]
            queue.append((x,y))
            visited[x][y] = selection[i]

    while queue:
        x, y = queue.popleft()
        if visited[x][y] == 2500: continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if not garden[nx][ny]: continue
            if visited[nx][ny]:
                if visited[x][y] > 0:
                    if visited[nx][ny] < 0 and not visited[nx][ny] + visited[x][y] + 1:
                        result += 1
                        visited[nx][ny] = 2500
                else:
                    if visited[nx][ny] > 0 and not visited[nx][ny] + visited[x][y] - 1:
                        result += 1
                        visited[nx][ny] = 2500
                continue
            if visited[x][y] > 0:
                visited[nx][ny] = visited[x][y] + 1
            else:
                visited[nx][ny] = visited[x][y] - 1
            queue.append((nx, ny))
    return result


def sow(k, g, r, selection):
    global max_result
    if k == len(avail):
        if g == G and r == R:
            max_result = max(max_result, grow(selection))
        return
    if g < G:
        sow(k+1, g+1, r, selection + [1])
    if r < R:
        sow(k+1, g, r+1, selection + [-1])
    sow(k+1, g, r, selection + [0])
        
        
N, M, G, R = map(int, input().split())
garden = []
avail = []
max_result = 0

for i in range(N):
    row = list(map(int, input().split()))
    garden.append(row)
    for j in range(M):
        if row[j] == 2:
            avail.append((i,j))

sow(0,0,0,[])
print(max_result)