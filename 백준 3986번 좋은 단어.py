# 백준 3986번 좋은 단어
import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0
for _ in range(n):
    stack = []
    tmp = input().rstrip()
    for c in tmp:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    if not stack: result += 1
print(result)