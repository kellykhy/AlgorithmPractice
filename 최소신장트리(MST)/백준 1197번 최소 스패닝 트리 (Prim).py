# 백준 1197번 최소 스패닝 트리 (Prim)

import sys
import heapq
input = sys.stdin.readline

# 그룹에 속한 정점들과 그룹에 속하지 않은 정점들 간의 거리의 최소값을 구하고, 해당 정점을 그룹에 포함시키는 과정 반복
# 우선순위큐에 저장할 값 = 정점 번호(그룹에 아직 포함x), 비용

v, e = map(int, input().split())
costs = [[] for _ in range(v+1)]
chk = [0 for _ in range(v+1)]
for _ in range(e):
    v1, v2, c = map(int, input().split())
    costs[v1].append((c, v2))
    costs[v2].append((c, v1))
    
p_queue = []
heapq.heapify(p_queue)
result = 0
chk[1] = 1
for nc, nv in costs[1]:
    heapq.heappush(p_queue, (nc, nv))
cnt = 1
while 1:
    c, v1 = heapq.heappop(p_queue)
    if chk[v1]: continue
    chk[v1] = 1
    cnt += 1
    result += c
    if cnt == v: break
    
    for nc, v2 in costs[v1]:
        if chk[v2]: continue
        heapq.heappush(p_queue, (nc, v2))
print(result)
