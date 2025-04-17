# 백준 1439번 뒤집기

import sys
input = sys.stdin.readline

def solution():
    stack = []
    nums = input().rstrip()
    for n in nums:
        if not stack:
            stack.append(n)
        else:
            if stack[-1] != n:
                stack.append(n)
    x, y = 0, 0
    for i in range(len(stack)):
        if stack[i] == '1':
            x += 1
        else:
            y += 1
    print(min(x, y))

solution()