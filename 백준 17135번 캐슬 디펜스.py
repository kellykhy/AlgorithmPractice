# 백준 17135번 캐슬 디펜스

import sys
from collections import deque
input = sys.stdin.readline
        
N, M, D = map(int, input().split())
field = []
max_cnt = 0
for i in range(N):
    row = list(map(int, input().split()))
    field.append(row)
            
def bfs(status, start):
    queue = deque()
    distance = [[0 for _ in range(M)] for _ in range(N+1)]
    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
    
    queue.append(start)
    distance[start[0]][start[1]] = 1
    
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= start[0] or nx < 0 or ny >= M or ny < 0: continue
            distance[nx][ny] = distance[x][y] + 1
            if distance[nx][ny]-1 > D: return (-1, -1)
            if status[nx][ny] == 1:
                return (nx, ny)
            queue.append((nx, ny))
    return (-1, -1)
                
def attack(archer):
    global max_cnt
    cnt = 0
    status = [x[:] for x in field]
    for i in range(N, 0, -1):
        arr = []
        for archer in archers:
            # 공격 (거리D이하 중 가장 가까운 지점, 거리 동일할 경우 가장 왼쪽)
            ex, ey = bfs(status, (i, archer))
            if (ex == -1 or (ex, ey) in arr): continue
            arr.append((ex, ey))
        # 공격받은 적 없애기
        for x, y in arr:
            status[x][y] = 0
        cnt += len(arr)
    max_cnt = max(max_cnt, cnt)      
        
def position(start, k):
    if k == 3:
        attack(archers)
        return
    for i in range(start, M):
        archers[k] = i
        position(i+1, k+1)
        archers[k] = -1

archers = [-1 for _ in range(3)]
position(0, 0)
print(max_cnt)