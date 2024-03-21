# 백준 1463번 1로 만들기

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for k in range(2,n+1):
    dp[k] = dp[k-1] + 1
    if (k % 3 == 0):
        dp[k] = min(dp[k], dp[k//3] + 1)
    if (k % 2 == 0):
        dp[k] = min(dp[k], dp[k//2] + 1)
print(dp[n])