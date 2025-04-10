# 삼성SW역량테스트 2016 하반기 2번 문제 2048 게임

import sys
input = sys.stdin.readline

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

def move(grid, dir):
    if dir == 0:  # 왼쪽
        return left(grid)
    elif dir == 1:  # 오른쪽
        return right(grid)
    elif dir == 2:  # 위
        return up(grid)
    elif dir == 3:  # 아래
        return down(grid)
    
def left(grid):
    new_grid = []
    for i in range(n):
        cmp = -1
        row = []
        crash = 0
        for j in range(n):
            if grid[i][j] == 0:
                crash += 1
                continue
            if cmp < 0:
                row.append(grid[i][j])
                cmp = j
                continue
            if grid[i][cmp] == grid[i][j]:
                row[-1] *= 2
                cmp = -1
                crash += 1
            else:
                row.append(grid[i][j])
                cmp = j
        row += [0] * crash
        new_grid.append(row)
    return new_grid

def right(grid):
    new_grid = []
    for i in range(n):
        cmp = -1
        row = []
        crash = 0
        for j in range(n-1, -1, -1):
            if grid[i][j] == 0:
                crash += 1
                continue
            if cmp < 0:
                row = [grid[i][j]] + row
                cmp = j
                continue
            if grid[i][cmp] == grid[i][j]:
                row[0] *= 2
                cmp = -1
                crash += 1
            else:
                row = [grid[i][j]] + row
                cmp = j
        row = [0] * crash + row
        new_grid.append(row)
    return new_grid
    
def up(grid):
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n): # 열
        cmp = -1
        col_lidx = 0
        for i in range(n):
            if grid[i][j] == 0:
                continue
            if cmp < 0:
                new_grid[col_lidx][j] = grid[i][j]
                cmp = i
                col_lidx += 1
                continue
            if grid[cmp][j] == grid[i][j]:
                new_grid[col_lidx-1][j] *= 2
                cmp = -1
            else:
                new_grid[col_lidx][j] = grid[i][j]
                cmp = i
                col_lidx += 1
    return new_grid

def down(grid):
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n): # 열
        cmp = -1
        col_lidx = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] == 0:
                continue
            if cmp < 0:
                new_grid[col_lidx][j] = grid[i][j]
                cmp = i
                col_lidx -= 1
                continue
            if grid[cmp][j] == grid[i][j]:
                new_grid[col_lidx+1][j] *= 2
                cmp = -1
            else:
                new_grid[col_lidx][j] = grid[i][j]
                cmp = i
                col_lidx -= 1
    return new_grid

def find_max(grid):
    global result
    for i in range(n):
        result = max(max(grid[i]), result)

def backtracking(grid, k):
    global result
    if k == 5:
        find_max(grid)
        return
    original_grid = [grid[x][:] for x in range(n)]
    for dir in range(4):
        grid = move(original_grid, dir)
        backtracking(grid, k+1)
        
result = 0
backtracking(grid, 0)
print(result)