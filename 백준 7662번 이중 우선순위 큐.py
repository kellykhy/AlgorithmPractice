# 백준 7662번 이중 우선순위 큐

import heapq, sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    minheap, maxheap = [], []
    visited= [False] * 1000001
    for i in range(N):
        ipt1, ipt2 = input().split()
        ipt2 = int(ipt2)
        if (ipt1 == 'I'):
            visited[i] = True
            heapq.heappush(minheap, (ipt2, i))
            heapq.heappush(maxheap, (-ipt2, i))
        elif (ipt2 == -1):
            while (minheap and not visited[minheap[0][1]]):
                heapq.heappop(minheap)
            if minheap: 
                visited[minheap[0][1]] = False
                heapq.heappop(minheap)
        else:
            while (maxheap and not visited[maxheap[0][1]]):
                heapq.heappop(maxheap)
            if maxheap:
                visited[maxheap[0][1]] = False
                heapq.heappop(maxheap)
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)
    if not minheap or not maxheap:
        print("EMPTY")
    else:
        print(-maxheap[0][0], minheap[0][0])