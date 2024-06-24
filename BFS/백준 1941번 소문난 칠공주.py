# 백준 1941번 소문난 칠공주

import sys
from collections import deque
input = sys.stdin.readline

graph = [[] for _ in range(5)]
for i in range(5):
    row = input()
    for j in range(5):
        graph[i].append(row[j])
        
combs = []
ary = []
visited = [False for _ in range(25)]

def chooseSeven(k, y):
    if (y >= 4):
        return
    if (k == 7):
        combs.append(ary[:])
        return
    for i in range(25):
        if (not visited[i]):
            if (len(ary) > 0 and i < (ary[-1][0] * 5 + ary[-1][1])):
                continue
            visited[i] = True
            ary.append((i//5, i%5))
            if graph[i//5][i%5] == 'Y':
                chooseSeven(k+1, y+1)
            else:
                chooseSeven(k+1, y)
            visited[i] = False
            ary.pop()
            
def checkAdjacent(comb):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visitedComb = [False for _ in range(7)]
    queue = deque()
    
    visitedComb[0] = True
    queue.append(comb[0])
    
    while (queue):
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if ((nr, nc) in comb):
                idx = comb.index((nr, nc))
                if not visitedComb[idx]:
                    visitedComb[idx] = True
                    queue.append((nr, nc))
                
    if False in visitedComb: return False
    else: return True
    
result = 0
chooseSeven(0, 0)

for comb in combs:
    if checkAdjacent(comb):
        result += 1
        
print(result)