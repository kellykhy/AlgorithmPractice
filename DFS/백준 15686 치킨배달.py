import sys

# [dist 함수] 두 위치 간의 거리 반환
def dist(a, b):
    result = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return result

def dfs(h, chicken_dist):
    global min_sol
    if (h == n_house):
        if (chicken_dist <= min_sol):
            min_sol = chicken_dist
        return
    for c in range(n_chicken):
        if (memo[h][c] == 0):                                                        # (1) memoization
            memo[h][c] = dist(house[h], chicken[c])
        d = chicken_dist + memo[h][c]
        if (d > min_sol):
            continue
        if (visited[c] == 0) and (len(list(filter(lambda x: x > 0, visited))) >= m): # (2) m 고려
            continue
        else:
            visited[c] += 1
        chicken_dist = d
        dfs(h+1, chicken_dist)
        visited[c] -= 1
        chicken_dist -= memo[h][c]

input = sys.stdin.readline
n, m = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(n)]

# 치킨집, 집의 위치 저장
chicken = []
house = []
n_chicken = 0
n_house = 0
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            house.append((i, j))
            n_house+=1
        elif Map[i][j] == 2:
            chicken.append((i, j))
            n_chicken+=1

# dfs(back_tracking && dp)
memo = [[0]*n_chicken for i in range(n_house)] # 치킨거리 저장(memoization)
min_sol = 987654321                                   #global
visited = [0]*n_chicken

dfs(0, 0)
print(min_sol)
