# 백준 1325번 효율적인 해킹 (ver2)

N, M = map(int, input().split())

Adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    Adj[B].append(A)

def dfs(n):
    visited = [0 for _ in range(N+1)]
    stack = []
    
    visited[n] = 1
    stack.append(n)
    cnt = 1
    
    while stack:
        n = stack.pop()
        for x in Adj[n]:
            if visited[x]: continue
            stack.append(x)
            visited[x] = 1
            cnt += 1
    return cnt

result = [0 for _ in range(N+1)]
max_cnt = 0
for n in range(1, N+1):
    result[n] = dfs(n)
    max_cnt = max(max_cnt, result[n])
    
for n in range(1, N+1):
    if result[n] == max_cnt:
        print(n, end = ' ')