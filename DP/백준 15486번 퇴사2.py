# 백준 15486번 퇴사2
import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
    
dp = [0] * (N+1)       # dp[i] : (끝에서 시작하여) i번쨰 날 이후의 상담을 할 때 최대 수익 (i번째 날 포함)
max_val = 0
max_list = [0] * (N+1) # max_list[i] : (끝에서 시작하여) i번쨰 날 이후의 상담을 할 때 최대 수익 (i번째 미포함일 수 있음)
for i in range(1, N+1):
    if (info[-i][0] > i): # 퇴사일을 넘겨 수행x
        dp[i] = 0
    else:
        dp[i] = max_list[i-info[-i][0]] + info[-i][1]
        max_val = max(dp[i], max_val)
    max_list[i] = max_val
print(max(dp))


''' 다른 사람 코드 - max_list를 따로 두지 않는 풀이법
import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
    
dp = [0] * (N+1)
max_val = 0
for i in range(1, N+1):
    if (info[-i][0] > i): # 퇴사일을 넘겨 수행x
        dp[i] = max_val
    else:
        dp[i] = max(dp[i-info[-i][0]] + info[-i][1], max_val)
    max_val = dp[i]
print(max_val)
'''