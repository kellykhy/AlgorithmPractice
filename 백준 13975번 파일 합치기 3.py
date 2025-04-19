# 백준 13975번 파일 합치기 3

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input()) # 소설의 장 수
    size = list(map(int, input().split()))
    heapq.heapify(size)
    result = 0
    for i in range(K-1):
        tmp = heapq.heappop(size) + heapq.heappop(size)
        heapq.heappush(size, tmp)
        result += tmp
    print(result)