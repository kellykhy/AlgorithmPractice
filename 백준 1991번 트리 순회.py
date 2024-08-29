# 백준 1991번 트리 순회

import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(input().split())
    graph[ord(tmp[0]) - ord('A')] += [tmp[1], tmp[2]]

# 전위 순회 (m->l->r)
def before(v):
    print(v, end = '')
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        before(l)
    if r != '.':
        before(r)
# 중위 순회
def middle(v):
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        middle(l)
    print(v, end = '')
    if r != '.':
        middle(r)
# 후위 순위
def after(v):
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        after(l)
    if r != '.':
        after(r)
    print(v, end = '')

before('A')
print()
middle('A')
print()
after('A')