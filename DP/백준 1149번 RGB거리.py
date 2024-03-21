# 백준 1149번 RGB거리

import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))
dp = []

for i in range(N):
    if (i==0):
        dp.append([cost[i][0], cost[i][1], cost[i][2]])
    else:
        dp.append([cost[i][0] + min(dp[-1][1], dp[-1][2]), cost[i][1] + min(dp[-1][0], dp[-1][2]), cost[i][2] + min(dp[-1][0], dp[-1][1])])
print(min(dp[N-1]))