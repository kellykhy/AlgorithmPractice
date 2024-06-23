# 백준 1311번 할 일 정하기1

N = int(input())
cost = []                               # cost: 각 작업자(i)가 해당 일(j)을 수행하는데 드는 비용(D_ij) 저장
for i in range(N):
    r = list(map(int, input().split()))
    cost.append(r)
dp = [10**6]*(1<<N)                     # dp: memoization
dp[0] = 0

for i in range(1<<N):
    k = 0
    for j in range(N):                  # k: 현재 작업 완료된 일의 수( = 현재 작업에 투입할 순서인 작업자)
        if i & (1<<j):
            k+=1
    for j in range(N):
        if i & (1 << j) == 0:
            dp[i|(1<<j)] = min(dp[i|(1<<j)], dp[i] + cost[k][j])

print(dp[-1])
