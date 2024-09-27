# 백준 1961번 소수 경로

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    digit = [1000, 100, 10, 1]
    visited[start] = 1
    queue.append(start)
    while (queue):
        prime = queue.popleft()
        for i in range(4):
            nprime1 = prime - digit[i]*int(str(prime)[i]) # 1033 -> (i=2) 1003
            for j in range(10):
                nprime2 = nprime1 + digit[i] * j
                if nprime2 < 1000: continue
                if not primes[nprime2]: continue
                if not visited[nprime2]:
                    queue.append(nprime2)
                    visited[nprime2] = visited[prime] + 1
                    if nprime2 == end:
                        return visited[nprime2]-1
    return -1
    

# 소수 구하기
primes = [1 for _ in range(10000)]
primes[0] = primes[1] = 0
for i in range(2, 5001):
    if primes[i]:
        x = i + i
        while (x < 10000):
            primes[x] = 0
            x += i

n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    if start == end:
        print(0)
        continue
    visited = [0 for _ in range(10000)] # 1000 ~ 9999
    result = bfs(start, end)
    if result == -1: print("Impossible")
    else: print(result)