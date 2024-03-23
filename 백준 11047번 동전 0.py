# 백준 11047번 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

result = 0
for i in range(N):
    if coins[-i-1] <= K:
        result += K // coins[-i-1]
        K %= coins[-i-1]
    if K == 0:
        print(result)
        break