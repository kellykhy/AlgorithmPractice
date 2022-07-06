# 15686번 치킨배달 문제
import sys

def dist(a, b):
    result = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return result

def dfs(cur, arr):
    global city_chicken_distance
    if len(arr) == m:
        tmp = 0
        for house in houses:
            len_house = sys.maxsize
            for c in arr:
                len_house = min(len_house, dist(house, c))
            tmp += len_house
        city_chicken_distance = min(city_chicken_distance, tmp)
        return
    if cur == len(chicken):
        return
    dfs(cur+1, arr+[chicken[cur]])
    dfs(cur+1, arr)


chicken = []
houses = []
input = sys.stdin.readline
n, m = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            houses.append((i, j))
        elif Map[i][j] == 2:
            chicken.append((i, j))

city_chicken_distance = sys.maxsize
dfs(0, [])
print(city_chicken_distance)