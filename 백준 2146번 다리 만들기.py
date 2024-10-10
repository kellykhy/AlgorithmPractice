# 백준 2146번 다리 만들기 
import sys
from collections import deque
input = sys.stdin.readline

#input
n = int(input())
jido = []
for _ in range(n):
    jido.append(list(map(int, input().split())))
   
#solution 
def territory_check(x,y,island): # bfs1
    queue = deque()
    queue.append((x,y))
    territory[x][y] = island
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if territory[nx][ny] == 1:
                    territory[nx][ny] = island # 섬 구분/표시 (2부터 시작)
                    queue.append((nx,ny))
                elif not jido[nx][ny]:
                    if distance[nx][ny]: continue
                    queue2.append((nx,ny))
                    territory[nx][ny] = island
                    distance[nx][ny] = 1
                    
def distance_check(): #bfs2
    result = n*n
    flag = 0
    while queue2:
        x,y = queue2.popleft()
        if distance[x][y] == flag: return result
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not territory[nx][ny]: # 바다인 경우, 영토 확장
                    territory[nx][ny] = territory[x][y]
                    distance[nx][ny] = distance[x][y] + 1
                    queue2.append((nx,ny))
                elif territory[nx][ny] != territory[x][y]: # 다른 섬 영토와 맞닿은 경우, 해당 깊이(depth)만 돌고 최소값 리턴
                    flag = distance[x][y] + 1
                    if distance[nx][ny] == 0:
                        return 1
                    if distance[nx][ny] < distance[x][y] + 1:
                        result = min(result, 2*distance[nx][ny])
                    else:
                        result = min(result, 2*distance[x][y]+1)
def solution(n, jido):
    global distance, territory, queue2, dx, dy
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    queue2 = deque()

    territory = [x[:] for x in jido]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    island = 2
    for x in range(n):
        for y in range(n):
            if territory[x][y] == 1: 
                territory_check(x,y,island)
                island += 1
    return(distance_check())

print(solution(n, jido))