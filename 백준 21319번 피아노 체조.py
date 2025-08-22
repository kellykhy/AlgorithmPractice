# 백준 21319번 피아노 체조

import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
Q = int(input())
accum = [0 for _ in range(N-1)]
n = 0
for i in range(N-1):
    if seq[i] > seq[i+1]:
        n += 1
    accum[i] = n
for i in range(Q):
    x, y = map(int, input().split())
    if x == y: print(0)
    elif x == 1:
        print(accum[y-2])
    else: print(accum[y-2] - accum[x-2])