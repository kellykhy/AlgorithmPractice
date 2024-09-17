# 백준 4991번 로봇 청소기

import sys
from collections import deque
input = sys.stdin.readline

def permutation(k, prev, n): # 방문한 더러운 칸의 수, 직전 위치, 더러운 칸 총
    global move, result
    if move >= result:
        return
    if k == n:
        result = min(result, move)
        return
    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = 1
        if distance[prev][i] == -1: continue
        move += distance[prev][i]
        permutation(k+1, i, n)
        move -= distance[prev][i]
        visited[i] = 0
        
def bfs(room, dirty): # 시작점과 더러운 칸들간의 거리(distance) 반환
    h, w = len(room), len(room[0])
    
    distance = [[-1 for _ in range(len(dirty))] for _ in range(len(dirty))] # 더러운 칸들 간의 거리
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(0, len(dirty)):
        x, y = dirty[i]
        queue = deque()
        visited = [[0 for _ in range(w)] for _ in range(h)]
    
        queue.append((x,y))
        visited[x][y] = 1
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
                if visited[nx][ny] or room[nx][ny] == 'x': continue
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                next = room[nx][ny]
                if isinstance(next, int):
                    distance[i][next] = visited[nx][ny]-1
                    distance[next][i] = visited[nx][ny]-1
    return distance


while 1:
    w, h = map(int, input().split())
    if w == 0: break
    
    room = [] # 방의 구조
    dirty = [] # 더러운 칸들의 위치 정보
    begin = (0,0)
    n = 0
    tmp = []
    for i in range(h):
        row_list = []
        row = input().rstrip()
        for j in range(w):
            if row[j] == '*':
                n += 1
                row_list.append(n)
                tmp.append((i, j))
                continue
            if row[j] == 'o':
                begin = (i,j)
            row_list.append(row[j])
        room.append(row_list)
    dirty.append(begin)
    dirty += tmp
        
    # 1. 더러운 칸들간의 거리
    distance = bfs(room, dirty)
    
    # 2. 더러운 칸들의 순열 (방문 순서)
    visited = [0 for _ in range(n+1)]
    move = 0
    result = 401
    permutation(0, 0, n)
    if result == 401: print(-1)
    else: print(result)