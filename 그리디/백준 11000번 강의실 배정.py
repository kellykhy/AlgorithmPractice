# 백준 11000번 강의실 배정

import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = []
end_points = []

for _ in range(n):
    s, t = map(int, input().split())
    times.append((s,t))
times.sort(key = lambda x: x[0])
    
for s,t in times:
    if not len(end_points) or s < end_points[0]:
        heapq.heappush(end_points, t)
    else:
        heapq.heappop(end_points)
        heapq.heappush(end_points, t)
        
print(len(end_points))