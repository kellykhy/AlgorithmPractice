# 백준 1717번 집합의 표현

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().rstrip().split())
group = [i for i in range(n+1)]

def root(a):
    if group[a] == a:
        return a
    else:
        ra = root(group[a])
        group[a] = ra
        return ra

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().rstrip().split())
    ra = root(a)
    rb = root(b)
    if op == 0:
        group[ra] = rb
    else:
        if (ra == rb):
            print("YES")
        else:
            print("NO")