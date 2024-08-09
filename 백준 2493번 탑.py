# 백준 2493번 탑

import sys

input = sys.stdin.readline

n = int(input())
towers = [0] + list(map(int, input().split()))
stack = []
result = []

for i in range(1, n + 1):
    if not stack:
        result.append(0)
    else:
        while (stack and towers[stack[-1]] < towers[i]):
            stack.pop()
        if not stack:
            result.append(0)
        else:
            result.append(stack[-1])
    stack.append(i)
print(*result)