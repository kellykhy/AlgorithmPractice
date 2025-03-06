# 백준 6198번 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

N = int(input())
height = []

for _ in range(N): height.append(int(input()))

stack = [(N, 1000000001)]
result = 0
for idx in range(N-1, -1, -1):
    while stack and height[idx] > stack[-1][1]:
        stack.pop()
    nxt_idx = stack[-1][0]
    result += nxt_idx - idx - 1
    stack.append((idx, height[idx]))
print(result)