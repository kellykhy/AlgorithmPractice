# 백준 2616번 소형기관차

import sys
input = sys.stdin.readline

n = int(input())
passengers = [0] + list(map(int, input().split()))
m = int(input())

psum = [] # 0, 35, 75, 125, 135, 165, 210, 270
summation = 0
for p in passengers:
    summation += p
    psum.append(summation)
    
dp = [[0 for _ in range(n+1)] for _ in range(4)]
for j in range(m, n+1):
    dp[1][j] = max(dp[1][j-1], psum[j] - psum[j-m])
for i in range(2,4):
    for j in range(i*m, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + psum[j] - psum[j-m])

print(dp[3][n])