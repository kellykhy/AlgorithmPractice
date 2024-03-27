# 백준 15990번 1,2,3 더하기 5
    
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
case = []
max = 0
for i in range(t):
    n = int(input())
    if max < n:
        max = n
    case.append(n)
        
dp = [[0,0,0,0]] # dp[n][i] : 합이 n이 되도록 하는 방법들 중 i로 시작하는 방법의 수 (n = 1,2,3)
for i in range(1, max+1):
    if i == 1:
        dp.append([0,1,0,0])
    elif i == 2:
        dp.append([0,0,1,0])
    elif i == 3:
        dp.append([0,1,1,1])
    else:
        dp.append([0, (dp[-1][2] + dp[-1][3])%1000000009, (dp[-2][1] + dp[-2][3])%1000000009, (dp[-3][1] + dp[-3][2])%1000000009]) # 점화식
        # 1000000009 모듈러 해주는 이유 : 수가 기하급수적으로 늘어나서 연산이 오래걸림 -> 시간초과 발생
for i in case:
    print(sum(dp[i])%1000000009)