# 백준 1520번 내리막길

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(r,c):
    if r == m-1 and c == n-1:
        return 1
    if dp[r][c] == -1:
        dp[r][c] = 0
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            if (0<=r+dr<m and 0<=c+dc<n and Map[r+dr][c+dc]<Map[r][c]):
                dp[r][c] += dfs(r+dr, c+dc)
    #print("dp[", r, "][", c, "] =", dp[r][c])
    return dp[r][c]

print(dfs(0,0))