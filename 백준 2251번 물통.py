# 백준 2251번 물통

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
visited = [[0 for _ in range(201)] for _ in range(201)]
total = c
result = []

def dfs(aa, bb):
    if visited[aa][bb]:
        return
    else:
        visited[aa][bb] = 1
        
    cc = total - aa - bb
    if aa == 0: 
        result.append(cc)
        
    # a->b
    if (aa > 0 and bb < b):
        tmp = min(aa, b-bb)
        nb = bb + tmp
        na = aa - tmp
        dfs(na, nb)
    # a->c
    if (aa > 0 and cc < c):
        tmp = min(aa, c-cc)
        na = aa - tmp
        dfs(na, bb)
    # b->a
    if (bb > 0 and aa < a):
        tmp = min(bb, a-aa)
        na = aa + tmp
        nb = bb - tmp
        dfs(na, nb)
    # b->c
    if (bb > 0 and cc < c):
        tmp = min(bb, c-cc)
        nb = bb - tmp
        dfs(aa, nb)
    # c->a
    if (cc > 0 and aa < a):
        tmp = min(cc, a-aa)
        na = aa + tmp
        dfs(na, bb)
    # c->b
    if (cc > 0 and bb < b):
        tmp = min(cc, b-bb)
        nb = bb + tmp
        dfs(aa, nb)
        
dfs(0,0)
result.sort()
print(*result)