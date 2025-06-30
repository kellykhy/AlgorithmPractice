# 백준 1034번 램프

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = dict()
for _ in range(n):
    tmp = input().rstrip()
    if tmp in table.keys():
        table[tmp] += 1
    else:
        table[tmp] = 1
k = int(input())
cand = [0,0]
for key, val in table.items():
    tmp = 0
    for x in key:
        if x == '0':
            tmp += 1
    if tmp > k: continue
    cand[tmp % 2] = max(cand[tmp % 2], val)
print(cand[k % 2])