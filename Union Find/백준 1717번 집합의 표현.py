# 백준 1717번 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if group[a] == a:
        return a
    else:
        ra = find(group[a])
        group[a] = ra
        return ra

n, m = map(int, input().split())
group = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    pa = find(a)
    pb = find(b)
    if op == 0:
        group[pa] = pb # union
    else:
        if (pa == pb):
            print("YES")
        else:
            print("NO")
