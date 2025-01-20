# 백준 2468번 안전 영역

import sys
from collections import deque
input = sys.stdin.readline


def safe_count(h):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > h:
                count += 1
                queue.append((i,j))
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if visited[nx][ny] or area[nx][ny] <= h:
                            continue
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
    return count

n = int(input())
area = []
max_safe_num = 0
for i in range(n):
    row = list(map(int, input().split()))
    area.append(row)

for h in range(101):
    safe_num = safe_count(h)
    max_safe_num = max(max_safe_num, safe_num)
    if safe_num == 0:
        break

print(max_safe_num)