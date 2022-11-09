# 백준 1012번 유기농배추(2) (메모리: 33224KB, 시간: 80ms)
## https://hei-jayden.tistory.com/100 참고하면서 dfs 개념 다시 익히려고 노력함.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(col,row):
    Map[row][col] -= 1
    m_change = [1, 0, -1, 0] #동(>)남(V)서(<)북(ㅅ) 순
    n_change = [0, 1, 0, -1]
    for i in range(4):
        nc = col+m_change[i]
        nr = row+n_change[i]
        if (0 <= nc < m and 0 <= nr < n): #조건1) Map의 범위 내에 존재
            if (Map[nr][nc] == 1):        #조건2) 배추가 있는지
                Map[nr][nc] -= 1 # 배추가 없는 지점으로 바꿔줌.
                dfs(nc, nr)

t = int(input())
count_list = []
for i in range(t):
    count = 0
    m,n,k = map(int, input().split())
    Map = [[0]*m for _ in range(n)]
    for i in range(k):
        mi, ni = map(int, input().split())
        Map[ni][mi] = 1

    for col in range(m):
        for row in range(n):
            if Map[row][col] == 1:
                dfs(col,row)
                count += 1
    count_list.append(count)

for i in range(t):
    print(count_list[i])