# 백트래킹 되새김

import sys
input = sys.stdin.readline

# 1~N 자연수 중에서 중복 없이 M개를 고른 수열?

def comb(nums): # 1~N 중에서 중복 없이 M개를 고른 수열
    if len(nums) == m:
       print(' '.join(map(str, nums)))
       return
    for i in range(1, n+1):
        if visited[i]:
            continue
        nums.append(i)
        visited[i] = 1
        comb(nums)
        nums.pop()
        visited[i] = 0
        
        
n, m = map(int, input().split())
visited = [0 for _ in range(n+1)]
comb([])