# 백준 9465번 스티커

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0, 0] for _ in range(n)] # dp[i][j]: i번째 열의 j번째 행의 스티커를 떼는 경우 중 최댓값
    stickers = [[] for _ in range(n)]
    for _ in range(2):
        row = list(map(int, input().split()))
        for i in range(n):
            stickers[i].append(row[i])
    for i in range(n):
        if i == 0:
            dp[i] = stickers[i]
        elif i == 1:
            dp[i][0] = dp[i-1][1] + stickers[i][0]
            dp[i][1] = dp[i-1][0] + stickers[i][1]
        else:
            dp[i][0] = max(dp[i-1][1] + stickers[i][0], dp[i-2][1] + stickers[i][0])
            dp[i][1] = max(dp[i-1][0] + stickers[i][1], dp[i-2][0] + stickers[i][1])
    print(max(dp[n-2] + dp[n-1]))