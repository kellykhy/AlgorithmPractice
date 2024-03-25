# 백준 15486번 퇴사2
import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
    
dp = [0] * (N+1)
max_val = 0
max_list = [0] * (N+1)
for i in range(1, N+1):
    if (info[-i][0] > i):
        dp[i] = 0
    else:
        dp[i] = max_list[i-info[-i][0]] + info[-i][1]
        max_val = max(dp[i], max_val)
    max_list[i] = max_val
print(max(dp))