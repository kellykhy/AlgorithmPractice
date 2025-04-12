# 삼성SW역량테스트 2016 하반기 2번 문제 2048 게임

import sys
input = sys.stdin.readline

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
    
def move(grid):
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

def find_max(grid):
    global result
    for i in range(n):
        result = max(max(grid[i]), result)
        
def turn(grid):
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[j][n-1-i] = grid[i][j]
    return new_grid

def backtracking(grid, k):
    global result
    if k == 5:
        find_max(grid)
        return
    grids = [grid]
    for _ in range(3):
        grids.append(turn(grids[-1]))
    for grid in grids:
        grid = move(grid)
        backtracking(grid, k+1)
        
result = 0

backtracking(grid, 0)
print(result)
