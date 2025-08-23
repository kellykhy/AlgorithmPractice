# 백준 11011번 Fly me to the Alpha Centauri

import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    dx = y-x
    sq = int(math.sqrt(dx))
    if dx <= 3:
        print(dx)
        continue
    if dx == sq ** 2:
        print(2*sq-1)
    elif dx - (sq ** 2) <= sq:
        print(2*sq)
    else:
        print(2*sq+1)
