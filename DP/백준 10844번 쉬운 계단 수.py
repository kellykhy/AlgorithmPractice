# 백준 10844번 쉬운 계단 수

import sys
input = sys.stdin.readline

n = int(input())

memo = [0 for _ in range(10)]
for i in range(1, n+1):
    if i == 1:
        memo = [0] + [1 for _ in range(9)]
        continue
    tmp = memo[:]
    for j in range(10):
        if j == 0:
            tmp[j] = memo[1]
        elif j == 9:
            tmp[j] = memo[8]
        else:
            tmp[j] = (memo[j-1] + memo[j+1])
    memo = tmp
    
print(sum(memo)%1000000000)