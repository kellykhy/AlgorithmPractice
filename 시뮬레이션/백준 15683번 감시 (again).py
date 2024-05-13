# 백준 15683번 감시 (again)

import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
area = [[] for _ in range(n)]
cctvs = [] # CCTV들의 위치 저장
walls = 0  # 벽(6)의 개수
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        area[i].append(row[j])
        if ( 1 <= row[j]  <= 5):
            cctvs.append([i,j])
        elif ( row[j] == 6):
            walls += 1

# 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
cctv_directions = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
]
direction = [(0,1), (1,0), (0,-1), (-1,0)]

max_cctv_cover = 0 # cctv(1~5), wall(6) 미포함
cctv_cover = 0

def backtracking(area, k):
    global direction, max_cctv_cover, cctv_cover
    if (k == len(cctvs)):
        max_cctv_cover = max(max_cctv_cover, cctv_cover)
        return

    x,y = cctvs[k]          # cctv 위치
    cctv_type = area[x][y]  # cctv 타입
    for cctv_dir in cctv_directions[cctv_type]: # ex. cctv2 [[0,2],[1,3]]
        cur_x, cur_y = x, y
        cover = 0                      # 1) 현재 선택된 방향(moves)으로 cctv가 작동할 때, 추가로 감사할 수 있는 영역 크기
        area_cpy = copy.deepcopy(area) # 2) area_cpy : 감시된 영역 표시 ('#')
        for dir in cctv_dir:
            dx, dy = direction[dir]
            new_x = cur_x
            new_y = cur_y
            while (True):
                new_x += dx
                new_y += dy
                if (new_x < 0 or new_x >= n or new_y < 0 or new_y >= m):
                    break
                if (area[new_x][new_y] == 6):
                    break
                if (area[new_x][new_y] == 0):
                    area_cpy[new_x][new_y] = '#'
                    cover += 1
        cctv_cover += cover
        backtracking(area_cpy, k+1)
        cctv_cover -= cover            # 1) 감시 영역 크기 되돌림
        area_cpy = copy.deepcopy(area) # 2) 감시 영역 표시 되돌림

backtracking(area, 0)

print(n*m - len(cctvs) - walls - max_cctv_cover)