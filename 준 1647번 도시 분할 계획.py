# 백준 1647번 도시 분할 계획
# N-1개의 길만 남겨둔 연결그래프(최소신장트리)로 만든 뒤, 최대 유지비인 길 없애기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
costs = []
for _ in range(M):
    x, y, c = map(int, input().split())
    costs.append((x,y,c))

costs.sort(key = lambda x : x[2])
parents = [i for i in range(N+1)]

def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]

cnt = 0
summ = 0
max_val = 0
for x,y,c in costs: # x = 3, y = 2
    x = find(x)
    y = find(y)
    if x == y: continue
    parents[x] = y
    cnt += 1
    summ += c
    if cnt == N-1:
        max_val = max(max_val, c)
        break
print(summ - max_val)