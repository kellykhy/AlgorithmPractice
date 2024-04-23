# 백준 2170번 선 긋기

import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    x, y = map(int, input().split())
    lines.append([x,y])
lines.sort(key = lambda x : x[1])

length = list()
prior = list()
prior.append((-1000000000, -1000000000))
for (x, y) in lines:
    while (prior and x < prior[-1][0]):
        prior.pop()
        length.pop()
    length.append(y-max(x, prior[-1][1]))
    prior.append((x,y))
print(sum(length))