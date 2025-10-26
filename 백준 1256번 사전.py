# 백준 1256번 사전

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

memo = [[1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = memo[i-1][j] + memo[i][j-1]

if memo[n][m] < k:
    print(-1)
    exit()

ans = ''
t = n+m
for idx in range(t):
    # 'a'의 개수가 남아있을 때 & idx번째가 'a'일 때
    if n > 0 and memo[n-1][m] >= k:
        ans += 'a'
        n-=1
    else:
        k -= memo[n-1][m]
        ans += 'z'
        m-=1
print(ans)
        