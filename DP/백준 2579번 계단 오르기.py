# 백준 2579번 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
steps = []
result = 0
dp = []
for i in range(n):
    steps.append(int(input()))
for i in range(n):
    if (i==0):
        dp.append([steps[-1], steps[-1]])
    elif (i==1):
        dp.append([steps[-2] + steps[-1], steps[-2] + steps[-1]])
    elif (i==2):
        dp.append([steps[-3] + steps[-1], steps[-3] + steps[-1]])
    else:
        dp.append([steps[-i-1] + dp[i-1][1], steps[-i-1] + max(dp[i-2])])

if (n == 1):
    print(dp[0][0])
elif (n == 2):
    print(dp[1][0])
else:
    print(max(max(dp[n-1]), max(dp[n-2])))