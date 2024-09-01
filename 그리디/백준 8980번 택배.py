# 백준 8980번 택배

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input()) # m = 6
delivery = []
capacity = [c for _ in range(n)] # [40, 40, 40, 40, 40, 40]
for _ in range(m):
    f, t, b = map(int, input().split())
    delivery.append((f,t,b))
    
delivery.sort(key = lambda x: x[1])
result = 0
for f, t, b in delivery:
    load = min(min(capacity[f:t]), b)
    for i in range(f, t):
        capacity[i] -= load
    result += load
print(result)
