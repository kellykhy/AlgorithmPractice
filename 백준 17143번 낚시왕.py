# 백준 17143번 낚시왕

import sys
input = sys.stdin.readline

def fish(sec):
    for i in range(1, R+1):
        if graph[i][sec]:
            size = shark_info[graph[i][sec]][1]
            graph[i][sec] = 0 # 상어 없앰
            return size # 크기
    return 0

def move():
    global graph, dir
    new_graph = [[0 for _ in range(C+1)] for _ in range(R+1)]
    new_dir = [0 for _ in range(M+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            if graph[r][c]:
                s = shark_info[graph[r][c]][0] # 속력
                
                d = dir[graph[r][c]] # 시작 방향
                nr, nc = r, c
                
                L = 0 # R or C
                l = 0 # r or c (시작 방향)
                if d <= 2:
                    L = R
                    l = r
                else:
                    L = C
                    l = c
                diff = 0
                if d == 1 or d == 4: diff = 2 * L - l - 1
                else: diff = l - 1
                
                x = s % (2*L-2) + diff
                x %= (2*L-2)
                if d <= 2:
                    if x <= R-1:
                        nd = 2
                        nr = x+1
                    else:
                        nd = 1
                        nr = 2*R-x-1
                else:
                    if x <= C-1:
                        nd = 3
                        nc = x+1
                    else:
                        nd = 4
                        nc = 2*C-x-1
                if not (new_graph[nr][nc] and shark_info[new_graph[nr][nc]][1] > shark_info[graph[r][c]][1]): #'이미 점령한 상어가 더 큰 경우'가 아니면
                    new_dir[graph[r][c]] = nd # 방향 업데이트
                    new_graph[nr][nc] = graph[r][c] # 위치 업데이트
                    
    graph = [row[:] for row in new_graph]
    dir = new_dir[:]

R, C, M = map(int, input().split())
graph = [[0 for _ in range(C+1)] for _ in range(R+1)]
shark_info = [0] # 속력, 크기
dir = [0] # 방향
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    graph[r][c] = i
    shark_info.append([s,z])
    dir.append(d)

res = 0
for i in range(1, C+1): # C초 동안 매 초마다 / O(100)
    # 1. 낚시왕이 상어 포획
    res += fish(i) # O(100) => O(100x100) = O(10,000)
    # 2. 상어 이동
    move()
    
print(res)