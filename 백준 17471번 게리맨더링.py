# 백준 17471번 게리맨더링

import sys
input = sys.stdin.readline

N = int(input())
pop = [0]+ list(map(int, input().split()))
adj = [[]]
for _ in range(N):
    adj.append(list(map(int, input().split()))[1:])

def connected(group):
    visited = [0 for _ in range(N+1)]
    visited[group[0]] = 1
    queue = [group[0]]
    while queue:
        x = queue.pop(0)
        for nx in adj[x]:
            if nx in group and not visited[nx]:
                visited[nx] = 1
                queue.append(nx)
    population = 0
    if sum(visited) == len(group):
        for n in group:
            population += pop[n]
        return population
    else:
        return -1
    
def combinations(arr, n): # N = 5, n = 3
    result = []
    if n > len(arr): return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1): # 3 (0,1,2) -> i = 0
            for j in combinations(arr[i+1:], n-1): # -> j in comb([2,3,4,5], 1)
                result.append([arr[i]]+j)
    
    return result

cand = []
for k in range(1,N//2+1):
    arr = [x for x in range(1,N+1)]
    combs1 = combinations(arr, k)
    for c1 in combs1:
        c2 = []
        for i in range(1, N+1):
            if i not in c1:
                c2.append(i)
        a = connected(c1)
        if a > 0:
            b = connected(c2)
            if b > 0:
                cand.append(abs(a-b))
if len(cand) > 0: print(min(cand))
else: print(-1)