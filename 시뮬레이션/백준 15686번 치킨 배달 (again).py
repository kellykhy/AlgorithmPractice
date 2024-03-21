# 백준 15686번 치킨 배달 (again)

import itertools
import sys
input = sys.stdin.readline

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1-x2) + abs(y1-y2)

N,M = map(int, input().split())
home = []
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1: # 집
            home.append((i,j))
        elif row[j] == 2: # 치킨집
            chicken.append((i,j))

distance_list = [[] for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(home)):
        distance_list[i].append(distance(chicken[i], home[j]))

chicken_idx = [i for i in range(len(chicken))]
chicken_combinations = list(itertools.combinations(chicken_idx, M)) # (M=2) -> ex. [(0,3),(1,0)]
result = 100000
for combi in chicken_combinations:
    chicken_distance = 0
    for i in range(len(home)):
        cd = 100000
        for j in range(len(chicken)):
            if j in combi:
                cd = min(distance_list[j][i], cd)
        chicken_distance += cd
    result = min(result, chicken_distance)
print(result)