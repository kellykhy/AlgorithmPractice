# 백준 1520번 내리막길(시간초과)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
Map = []
for r in range(m):
    Map.append(list(map(int, input().split())))

def dfs(r,c):
    global h
    r_change = [0, 1, 0, -1]
    c_change = [1, 0, -1, 0]
    if (r == m-1 and c == n-1):
        h += 1
        return
    for i in range(4):
        new_r = r + r_change[i]
        new_c = c + c_change[i]
        if (0 <= new_r < m and 0 <= new_c < n) and Map[new_r][new_c] < Map[r][c]:
                #print(new_r, new_c)
                dfs(new_r, new_c)
h = 0
dfs(0,0)
print(h)