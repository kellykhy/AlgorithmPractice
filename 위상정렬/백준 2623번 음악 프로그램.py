# 백준 2623번 음악 프로그램

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split()) 
deg = [0] * (N+1)
adj = [[] for _ in range(N+1)]
for i in range(M):
    pd = list(map(int, input().split()))
    n = pd.pop(0)
    #print("pd: ", pd)
    for j in range(n-1):
        for h in range(j+1, n):
            #print("j:", j, "h:", h)
            adj[pd[j]].append(pd[h])
#print(adj)

for i in range(1, N+1):
    for nxt in adj[i]:
        deg[nxt]+=1

queue = []
result = []
for i in range(1, N+1):
    if deg[i] == 0:
        queue.append(i)
while (queue):
    cur = queue[0]
    queue.pop(0)
    result.append(cur)
    for nxt in adj[cur]:
        deg[nxt]-=1
        if (deg[nxt] == 0):
            queue.append(nxt)
if (len(result) != N):
    print(0)
else:
    for singer in result:
        print(singer, end = ' ')
