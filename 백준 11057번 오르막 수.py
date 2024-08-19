# 백준 11057번 오르막 수

import sys
input= sys.stdin.readline

n = int(input())
elements = [1 for _ in range(10)]
for _ in range(n-1):
    cum_sum = 0
    for i in range(10):
        cum_sum += elements[i]
        elements[i] = cum_sum

print(sum(elements) % 10007)