# 백준 9466번 팀 프로젝트

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    global cnt
    
    seq.append(n)
    vis[n] = 1
    
    if vis[arr[n]]:
        if arr[n] in seq:
            cnt -= (len(seq)-seq.index(arr[n]))
    else:
        dfs(arr[n])

T = int(input())
for _ in range(T):
    N = int(input()) # 7
    arr = [0] + list(map(int, input().split())) # 3 1 3 7 3 4 6
    vis = [0 for _ in range(N+1)]
    cnt = N
    for n in range(1, N+1):
        if vis[n] : continue
        seq = [0]
        dfs(n)
    print(cnt)