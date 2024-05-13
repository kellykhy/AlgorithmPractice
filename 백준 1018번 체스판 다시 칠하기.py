# 백준 1018번 체스판 다시 칠하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[c for c in input()] for _ in range(n)]

sample = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
min_diff = 2500
for i in range(n-7):
    for j in range(m-7):
        diff1, diff2 = 0, 0
        for r in range(8):
            for c in range(8):
                if (sample[r%2][c] != graph[i+r][j+c]):
                    diff1 += 1
                if (sample[1-r%2][c] != graph[i+r][j+c]):
                    diff2 += 1
        min_diff = min(min_diff, diff1, diff2)
print(min_diff)