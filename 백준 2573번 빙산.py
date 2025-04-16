# 백준 2573번 빙산

from collections import deque

def bfs(i, j, k):
    global N, M, antarc, glacier
    antarc_cpy = [antarc[x][:] for x in range(N)]
    glacier_cpy = glacier
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if antarc[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
            elif not antarc[nx][ny]:
                tmp = antarc_cpy[x][y] - 1
                if tmp == 0:
                    glacier_cpy -= 1
                    antarc_cpy[x][y] = 0
                elif tmp > 0:
                    antarc_cpy[x][y] = tmp
    antarc = antarc_cpy
    if glacier > cnt:
        return k
    glacier = glacier_cpy
    return 0
    
def solution():
    global N, M, antarc, glacier
    N, M = map(int, input().split())
    antarc = []
    glacier = 0
    for i in range(N):
        antarc.append(list(map(int, input().split())))
        for j in range(M):
            if antarc[i][j]:
                glacier += 1
    k = 0
    for i in range(N):
        for j in range(M):
            if antarc[i][j]:
                k += 1
                if bfs(i, j, k):
                    return k-1
    return 0

print(solution())