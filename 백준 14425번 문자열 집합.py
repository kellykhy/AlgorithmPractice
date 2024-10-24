# 백준 14425번 문자열 집합

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
words = set()
ans = 0

for _ in range(n):
    words.add(input().rstrip())
for _ in range(m):
    if input().rstrip() in words:
        ans += 1
print(ans)

''' # trie 알고리즘 사용
import sys
ROOT = 0
MX = 500 * 10000 + 5

def insert(s):
    global order
    cur = ROOT
    for c in s:
        tmp = ord(c)-ord('a')
        if nxt[cur][tmp] == -1:
            nxt[cur][tmp] = order
            order += 1
        cur = nxt[cur][tmp]
    chk[cur] = 1
    
def find(s):
    cur = ROOT
    for c in s:
        tmp = ord(c)-ord('a')
        if nxt[cur][tmp] == -1:
            return 0
        cur = nxt[cur][tmp]
    return chk[cur]
    

input = sys.stdin.readline
n, m = map(int, input().split())

nxt = [[-1 for _ in range(26)] for _ in range(MX)]
chk = [0 for _ in range(MX)]
order = 1
for _ in range(n):
    insert(input().rstrip())
result = 0
for _ in range(m):
    result += find(input().rstrip())
print(result)
'''