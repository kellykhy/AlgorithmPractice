# 백준 1781번 컵라면

import sys
import heapq

input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort() # deadline, 컵라면 수에 따라 정렬

result = []
ans = 0
t = 1
for i in range(N):
    d, c = arr[i]
    if t <= d: # 시간 <= 데드라인
        heapq.heappush(result, (c,d))
        ans += c
        t += 1
    elif d < t: # 데드라인 < 시간
        if result[0][0] < c:
            ans -= result[0][0]
            ans += c
            heapq.heappop(result)
            heapq.heappush(result, (c,d))
        
print(ans)