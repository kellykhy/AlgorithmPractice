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