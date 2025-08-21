# 백준 1202번 보석 도둑

import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
bags = []
for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V)) # 무게, 가격
for _ in range(K):
    bags.append(int(input())) # 무게

bags.sort()
gems.sort(key = lambda x : x[0])

result = 0
heap = []

n = 0
for W in bags:
    while n < N and gems[n][0] <= W:
        heapq.heappush(heap, -gems[n][1])
        n += 1
    if not heap: continue
    tmp = -heapq.heappop(heap)
    result += tmp
    
print(result)