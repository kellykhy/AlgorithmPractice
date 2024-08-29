# 백준 1991번 트리 순회

import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n)]
for _ in range(n):
    tmp = list(input().split())
    graph[ord(tmp[0]) - ord('A')] += [tmp[1], tmp[2]]

# 전위 순회 (m->l->r)
def preorder(v):
    print(v, end = '')
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        preorder(l)
    if r != '.':
        preorder(r)
# 중위 순회
def inorder(v):
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        inorder(l)
    print(v, end = '')
    if r != '.':
        inorder(r)
# 후위 순위
def postorder(v):
    l, r = graph[ord(v)-ord('A')]
    if l != '.':
        postorder(l)
    if r != '.':
        postorder(r)
    print(v, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')