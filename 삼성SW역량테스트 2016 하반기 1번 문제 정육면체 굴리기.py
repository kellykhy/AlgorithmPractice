#삼성SW역량테스트 2016 하반기 1번 문제 정육면체 굴리기

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
dirs = list(map(int, input().split()))

d = [(0,0), (0,1), (0,-1), (-1,0), (1,0)] #1: 동, 2: 서, 3: 북, 4: 남
dice = [[0,0,0,0], [0,0,0,0], [0,0,0,0]] # 주사위

def roll(dice, dir):
    # 하단: (1,1), 상단: (1,3)
    if dir == 1: # 동쪽으로 이동
        dice[1] = dice[1][1:] + [dice[1][0]]
    elif dir == 2: #서쪽으로 이동
        dice[1] = [dice[1][3]] + dice[1][:3]
    elif dir == 3: #북쪽으로 이동
        tmp = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = dice[1][3]
        dice[1][3] = tmp
    else: # 남쪽으로 이동
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[1][3]
        dice[1][3] = tmp

for dir in dirs:
    nx, ny = x + d[dir][0], y + d[dir][1]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    x, y = nx, ny
    roll(dice, dir)
    if grid[x][y] == 0:
        grid[x][y] = dice[1][1]
    else:
        dice[1][1] = grid[x][y]
        grid[x][y] = 0
    print(dice[1][3])