# 백준 10844 쉬운 계단 수(다시)
import sys
input = sys.stdin.readline

N = int(input())
memo = [1 for _ in range(10)] # 0~9
for i in range(1, N+1):
    if i == 1: continue
    tmp = memo[:]
    for j in range(10):
        new = 0
        if (j-1 >= 0):
            new += tmp[j-1]
        if (j+1 <= 9):
            new += tmp[j+1]
        memo[j] = new
print(sum(memo[1:])%1000000000)