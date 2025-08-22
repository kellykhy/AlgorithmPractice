# 백준 1053번 가장 긴 증가하는 부분 수열

import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    maxval = dp[i]
    for j in range(i):
        if A[j] < A[i]:
            maxval = max(maxval, dp[i]+dp[j])
    dp[i] = maxval
print(max(dp))
