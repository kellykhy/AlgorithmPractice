# 백준 15903번 카드 합체 놀이

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
heap = list(map(int, input().split()))

heapq.heapify(heap) # O(n)
for i in range(m):
    v1 = heapq.heappop(heap) # O(logn)
    v2 = heapq.heappop(heap) # O(logn)
    
    heapq.heappush(heap, v1+v2) # O(logn)
    heapq.heappush(heap, v1+v2) # O(logn)
    
print(sum(heap))