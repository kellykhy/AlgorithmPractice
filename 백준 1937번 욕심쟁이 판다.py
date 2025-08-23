# 백준 1937번 욕심쟁이 판다

import sys

input = sys.stdin.readline

n = int(input())
forest = []
position = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        position.append((row[j], i, j))
    forest.append(row)
position.sort(reverse = True)
memo = [[0 for _ in range(n)] for _ in range(n)]

result = 0
for b, x, y in position:
    mpath = 0
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if not (0<=nx<n and 0<=ny<n): continue
        if forest[nx][ny] <= forest[x][y]: continue
        mpath = max(mpath, memo[nx][ny] + 1)
    memo[x][y] = mpath
    result = max(mpath, result)
print(result+1)