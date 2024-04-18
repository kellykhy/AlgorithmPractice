# 백준 11722번 가장 긴 감소하는 부분 수열 

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(0, N):
    for j in range(i, N):
        if (A[j] < A[i]):
            dp[j] = dp[i] + 1 # dp[i] : i번째 포함한 수열의 길이의 최댓값

print(dp)