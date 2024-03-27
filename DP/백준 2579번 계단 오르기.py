# 백준 2579번 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())
steps = []
for i in range(n):
    steps.append(int(input()))
    
dp = [0]
for i in range(1,n+1):
    if (i==1):
        dp.append([steps[-1], steps[-1]])
    elif (i==2):
        dp.append([steps[-2] + steps[-1], steps[-2] + steps[-1]])
    elif (i==3):
        dp.append([steps[-3] + steps[-1], steps[-3] + steps[-1]])
    else:
        dp.append([steps[-i] + dp[i-1][1], steps[-i] + max(dp[i-2])]) # 점화식

if (n == 1):
    print(dp[1][0])
elif (n == 2):
    print(dp[2][0])
else:
    print(max(max(dp[n]), max(dp[n-1])))