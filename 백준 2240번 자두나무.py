# 백준 2240번 자두나무

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
drop = [0]
for _ in range(T):
    drop.append(int(input()))

dp = [[0 for _ in range(W+1)] for _ in range(T+1)]
for t in range(1, T+1):
    for w in range(W+1):
        j = 1 if drop[t] == w % 2 + 1 else 0
        dp[t][w] = max(dp[t-1][0:w+1]) + j
print(max(dp[T]))