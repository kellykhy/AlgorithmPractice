# 백준 2098번 외판원 순회

n = int(input())
W = []
for i in range(n):
    row = list(map(int, input().split()))
    W.append(row)

Cost = [[0]*(1<<n) for i in range(n)]

def dfs(cur, visited):
    if visited == ((1<<n)-1):
        if W[cur][0]:             # 4군데 다 방문했고 출발점으로 돌아가는 경로도 있다면
            return W[cur][0]
        else:                     # 4군데 다 방문했지만 출발점으로 돌아가는 경로가 없다면
            return 987654321
    
    if Cost[cur][visited]:                   # 이미 계산되어 있다면(dp)
        return Cost[cur][visited]

    cost = 987654321
    for i in range(1, n):
        if visited & 1<<i or (not W[cur][i]): # 이미 방문을 했거나 해당 도시로 가는 경로가 없다면
            continue
        cost = min(cost, dfs(i, visited | (1 << i)) + W[cur][i])
    Cost[cur][visited] = cost
    return Cost[cur][visited]

print(dfs(0, 1))