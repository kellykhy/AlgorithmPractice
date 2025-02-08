# 백트래킹 되새김

import sys
input = sys.stdin.readline

# boj15649 (1~N 자연수 중에서 중복 없이 M개를 고른 수열?)
'''
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
'''
'''
# boj15650 
def comb2(nums, st): # 1~N 중에서 중복 없이 M개를 고른 '오름차순' 수열
    if len(nums) == m:
       print(' '.join(map(str, nums)))
       return
    for i in range(st, n+1):
        if visited[i]:
            continue
        nums.append(i)
        visited[i] = 1
        comb2(nums, i+1)
        nums.pop()
        visited[i] = 0
        
n, m = map(int, input().split())
visited = [0 for _ in range(n+1)]
comb2([], 1)
'''

