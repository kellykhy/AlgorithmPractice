# 백준 9461번 파도반 수열

import sys
input = sys.stdin.readline
        
n = int(input())
memo = [0 for _ in range(101)]

for k in range(1, 101):
    if k <= 3:
        memo[k] = 1
    elif k <= 5:
        memo[k] = 2
    else:
        memo[k] = memo[k-5] + memo[k-1]
for _ in range(n):
    print(memo[int(input())])