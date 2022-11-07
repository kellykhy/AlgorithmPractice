# 백준 1012번 유기농배추(2) (메모리: 33224KB, 시간: 80ms)
## https://hei-jayden.tistory.com/100 참고하면서 dfs 개념 다시 익히려고 노력함.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def dfs(col,row):
    graph[row][col] = 0
    m_change = [1, 0, -1, 0]
    n_change = [0, 1, 0, -1]
    for i in range(4):
        new_c = col+m_change[i]
        new_r = row+n_change[i]
        if (0<=new_c<m and 0<=new_r<n):
            if (graph[new_r][new_c]==1):
                graph[new_r][new_c]-=1
                dfs(new_c, new_r)
count_list = []
for i in range(t):
    count = 0
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        mi, ni = map(int, input().split())
        graph[ni][mi] = 1
    for col in range(m):
        for row in range(n):
            if graph[row][col] == 1:
                dfs(col,row)
                count += 1
    count_list.append(count)

for i in range(t):
    print(count_list[i])