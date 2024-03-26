# 백준 2230번 수 고르기

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort()
left, right = 0, 0
min_val = int(2e9)

while (left < N):
    while (right < N and A[right] - A[left] < M):
        right += 1
    if (right == N):
        break
    min_val = min(min_val, A[right] - A[left])
    left += 1
print(min_val)