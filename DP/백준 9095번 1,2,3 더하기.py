# 백준 9095번 1,2,3 더하기
import sys
input = sys.stdin.readline

T = int(input())
case = []
for _ in range(T):
    case.append(int(input()))
n = max(case)
dp = [0] * (n+1) # dp[n] : n을 1,2,3의 합으로 나타내는 방법의 수

for i in range(0, n+1):
    if (i < 2):
        dp[i] = 1
    elif (i == 2):
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 점화식
        
for i in case:
    print(dp[i])