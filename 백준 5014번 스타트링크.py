# 백준 5014번 스타트링크

import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())

def bfs(s):
    dfl = [u, -d]
    queue = deque()
    visited = [0 for _ in range(f+1)]
    
    queue.append(s)
    visited[s] = 1
    
    while queue:
        fl = queue.popleft()
        if (fl == g):
            return visited[fl] - 1
        for i in range(2):
            nfl = fl + dfl[i]
            if (nfl < 1 or nfl > f or visited[nfl]):
                continue
            queue.append(nfl)
            visited[nfl] = visited[fl] + 1
    return "use the stairs"

def solution(f, s, g, u, d):
    answer = bfs(s)
    return answer

print(solution(f, s, g, u, d))