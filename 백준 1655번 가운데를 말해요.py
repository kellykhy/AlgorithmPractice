# 백준 1655번 가운데를 말해요

import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
upper_min_heap, lower_max_heap = [], [] # max_heap: 부호 바꿔서 넣고 부호 바꿔서 뺴기
for i in range(n):
    x = int(input().rstrip())
    if i == 0:
        heapq.heappush(lower_max_heap, -x)
    elif i == 1:
        if x < -lower_max_heap[0]:
            heapq.heappush(upper_min_heap, -heapq.heappop(lower_max_heap))
            heapq.heappush(lower_max_heap, -x)
        else:
            heapq.heappush(upper_min_heap, x)
    else:
        heapq.heappush(lower_max_heap, -x)
        if upper_min_heap[0] < -lower_max_heap[0]:
            heapq.heappop(lower_max_heap)
            heapq.heappush(upper_min_heap, x)
            if len(upper_min_heap) > len(lower_max_heap):
                tmp = heapq.heappop(upper_min_heap)
                heapq.heappush(lower_max_heap, -tmp)
        elif len(upper_min_heap) < len(lower_max_heap) - 1:
            tmp = heapq.heappop(lower_max_heap)
            heapq.heappush(upper_min_heap, -tmp)
    print(-lower_max_heap[0])