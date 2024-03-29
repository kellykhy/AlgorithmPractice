# 백준 11722번 가장 긴 감소하는 부분 수열 
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    max_val = 0
    max_idx = 0
    for k in range(i-1,0,-1):
        if (A[-i] > A[-k] and dp[k] > max_val):
            max_val = dp[k]
            max_idx = k
    dp[i] = dp[max_idx] + 1

print(max(dp))