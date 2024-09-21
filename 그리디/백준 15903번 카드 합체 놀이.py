# 백준 15903번 카드 합체 놀이

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(m):
    A.sort()
    n = A[0] + A[1]
    A[0] = n
    A[1] = n
print(sum(A))