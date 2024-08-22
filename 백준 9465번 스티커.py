# 백준 9465번 스티커

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input().rstrip())
    dp = [[0 for _ in range(n)] for _ in range(2)] # dp[i][j]: j번째 열의 i(0 or 1)번째 행의 스티커를 떼는 경우 중 최댓값
    stickers = []
    for _ in range(2):
        row = list(map(int, input().split()))
        stickers.append(row)
    for i in range(n):
        if i == 0:
            dp[0][i] = stickers[0][i]
            dp[1][i] = stickers[1][i]
        elif i == 1:
            dp[0][i] = dp[1][i-1] + stickers[0][i]
            dp[1][i] = dp[0][i-1] + stickers[1][i]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
    print(max(dp[0][n-2:] + dp[1][n-2:]))