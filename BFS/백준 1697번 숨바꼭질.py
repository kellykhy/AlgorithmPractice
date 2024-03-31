# 백준 1697 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    visited = [0] * 100001
    
    queue.append(start)
    visited[start] = 1
    
    while (queue):
        x = queue.popleft()
        dx = [x, 1, -1]
        for i in range(3):
            new_x = x + dx[i]
            if (new_x < 0 or new_x > 100000):
                continue
            if (visited[new_x]):
                continue
            queue.append(new_x)
            visited[new_x] = visited[x] + 1
            if (new_x == k):
                return visited[k] -1

n, k = map(int, input().rstrip().split())
if (n >= k):
    print(n-k)
else:
    print(bfs(n))