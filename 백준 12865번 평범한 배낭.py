# 백준 12865번 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N(물품 수), K(배낭 최대 수용 무게)
stuffs = []
for _ in range(N):
    stuffs.append(tuple(map(int, input().split())))
memo = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1): # n번째 물품까지 탐색
    w, v = stuffs[n-1]
    for k in range(1, K+1): # 무게=k
        if k < w:
            memo[n][k] = memo[n-1][k]
        else:
            memo[n][k] = max(memo[n-1][k], v + memo[n-1][k-w])

print(memo[N][K])