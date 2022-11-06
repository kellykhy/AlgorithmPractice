# 백준 1012번 유기농배추(메모리: 33220kb, 실행시간: 2668ms)

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
t = int(input())

count_list = []

def dfs(init, count):
    init[2] = count
    for cabbage in Map:
        if sum(cabbage[0:2]) > sum(init[0:2]) + 1:
            break
        if cabbage[2]:
            continue
        if abs(sum(cabbage[0:2]) - sum(init[0:2])) == 1:
                if abs(init[0]-cabbage[0]) < 2 and abs(init[1]-cabbage[1]) < 2:
                    dfs(cabbage, count)

for i in range(t):
    m,n,k = map(int, input().split())
    Map = [list(map(int,input().split())) + [0] for _ in range(k)]
    Map.sort(key = lambda pos: sum(pos))
    count = 0

    for cabbage in Map:
        if cabbage[2]==0:
            count += 1
            dfs(cabbage, count)
    count_list.append(count)

for i in range(t):
    print(count_list[i])