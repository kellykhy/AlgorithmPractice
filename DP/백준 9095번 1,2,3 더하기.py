# 백준 9095번 1,2,3 더하기

T = int(input())
case = []
for _ in range(T):
    case.append(int(input()))
n = max(case)
dp = [0] * (n+1)

for i in range(0, n+1):
    if (i < 2):
        dp[i] = 1
    elif (i == 2):
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
for i in case:
    print(dp[i])
