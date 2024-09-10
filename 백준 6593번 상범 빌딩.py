# 백준 6593번 상범 빌딩

import sys
from collections import deque
input = sys.stdin.readline

def bfs(L, R, C, start, building):
    # 동서남북상하
    dl, dr, dc = [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    queue = deque()
    
    sl, sr, sc = start
    queue.append(start)
    visited[sl][sr][sc] = 1
    while (queue):
        l, r, c = queue.popleft()
        if building[l][r][c] == 'E':
            print("Escaped in", visited[l][r][c]-1, "minute(s).")
            return
        for i in range(6):
            nl, nr, nc = l + dl[i], r + dr[i], c + dc[i]
            if nl < 0 or nl >= L or nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if visited[nl][nr][nc]: continue
            if building[nl][nr][nc] == '#': continue
            queue.append((nl, nr, nc))
            visited[nl][nr][nc] = visited[l][r][c] + 1
    print("Trapped!")
        

while 1:
    L, R, C = map(int, input().split())
    start = (0,0,0)
    end = (0,0,0)
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    for l in range(L):
        level = [] # 한 층(2차원)
        for r in range(R):
            row = input().rstrip()
            row_list = []
            for c in range(C):
                row_list.append(row[c])
                if row[c] == 'S':
                    start = (l, r, c)
            level.append(row_list)
        building.append(level)
        enter = input().rstrip()
    bfs(L, R, C, start, building)