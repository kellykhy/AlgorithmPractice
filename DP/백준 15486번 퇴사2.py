# 백준 15486번 퇴사2
import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
    
dp = [0] * (N+1)
max_val = 0
for i in range(1, N+1):
    if (info[-i][0] > i):
        dp[i] = max_val
    else:
        dp[i] = max(dp[i-info[-i][0]] + info[-i][1], max_val)
    max_val = dp[i]
print(max_val)