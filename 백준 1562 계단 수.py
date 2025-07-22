# 백준 1562 계단 수
import sys
input = sys.stdin.readline

N = int(input())

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]
for n in range(1,10):
    dp[1][n][1<<n] = 1

for k in range(2, N+1):
    for n in range(10):
        for v in range(1024):
            if (n-1 >= 0):
                dp[k][n][v | (1<<n)] += dp[k-1][n-1][v]
            if (n+1 <= 9):
                dp[k][n][v | (1<<n)] += dp[k-1][n+1][v]

res = 0
for n in range(10):
    res += dp[N][n][1023]

print(res%1000000000)