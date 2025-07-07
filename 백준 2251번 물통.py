# 백준 2251번 물통

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
visited = [[0 for _ in range(201)] for _ in range(201)]
total = c
visited[0][0] = 1
result = []

def dfs(aa, bb):
    cc = total - aa - bb
    if (aa == 0): 
        result.append(cc)
    # a->b
    if (aa > 0 and bb < b):
        tmp = min(aa, b-bb)
        nb = bb + tmp
        na = aa - tmp
        if not visited[na][nb]:
            visited[na][nb] = 1
            dfs(na, nb)
    # a->c
    if (aa > 0 and cc < c):
        tmp = min(aa, c-cc)
        na = aa - tmp
        if not visited[na][bb]:
            visited[na][bb] = 1
            dfs(na, bb)
    # b->a
    if (bb > 0 and aa < a):
        tmp = min(bb, a-aa)
        na = aa + tmp
        nb = bb - tmp
        if not visited[na][nb]:
            visited[na][nb] = 1
            dfs(na, nb)
    # b->c
    if (bb > 0 and cc < c):
        tmp = min(bb, c-cc)
        nb = bb - tmp
        if not visited[aa][nb]:
            visited[aa][nb] = 1
            dfs(aa, nb)
    # c->a
    if (cc > 0 and aa < a):
        tmp = min(cc, a-aa)
        na = aa + tmp
        if not visited[na][bb]:
            visited[na][bb] = 1
            dfs(na, bb)
    # c->b
    if (cc > 0 and bb < b):
        tmp = min(cc, b-bb)
        nb = bb + tmp
        if not visited[aa][nb]:
            visited[aa][nb] = 1
            dfs(aa, nb)
dfs(0,0)
result.sort()
print(*result)