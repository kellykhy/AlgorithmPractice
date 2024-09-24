# 백준 2461번 대표 선수

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
groups = [] # 학급 별 학생들의 능력치 (n개의 학급, 각 학급 m명의 학생)
heap = [] # n명읟 대표 선수들의 (능력치, 학급)
max_val = 0
for i in range(n):
    group = list(map(int, input().split()))
    group.sort()
    groups.append(group)
    max_val = max(max_val, group[0])
    heapq.heappush(heap, (group[0],i)) # 능력치, 학급

result = 1e+9
p = [1 for _ in range(n)]
if n == 1:
    result = 0
elif m == 1:
    result = max_val - heap[0][0]
else:
    while 1:
        min_val, g = heapq.heappop(heap)
        diff = max_val-min_val
        result = min(result, diff)
        if p[g] >= m: break
        heapq.heappush(heap, (groups[g][p[g]], g))
        max_val = max(max_val, groups[g][p[g]])
        p[g] += 1
print(result)