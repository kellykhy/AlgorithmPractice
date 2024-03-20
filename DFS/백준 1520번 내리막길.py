# 백준 1520번 내리막길(시간초과)

import sys
import time
start = time.time()  # 시작 시간 저장

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r,c):
    global h
    if (r == m-1 and c == n-1):
        h += 1
        return
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (0 <= r+dr <m and 0 <= c+dc < n and Map[r+dr][c+dc] < Map[r][c]):
                dfs(r+dr, c+dc)
    return

m, n = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(m)]
h = 0
dfs(0,0)
print(h)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
