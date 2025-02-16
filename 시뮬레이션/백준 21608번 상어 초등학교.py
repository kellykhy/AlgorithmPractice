# 백준 21608번 상어 초등학교

import sys
input = sys.stdin.readline

n = int(input())
room = [[0 for _ in range(n)] for _ in range(n)]

result = 0

friends = [[] for _ in range(n*n+1)]
for _ in range(n*n):
    std, f1, f2, f3, f4 = map(int, input().split())
    friends[std] += [f1, f2, f3, f4]
   
    scores1 = []
    for x in range(n):
        for y in range(n):
            if room[x][y]: continue
            score1 = 0
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                if room[nx][ny] in (f1, f2, f3, f4):
                    score1 += 1
            scores1.append((score1, x, y))
    scores1.sort(reverse = True)
    
    if (len(scores1) >= 2 and scores1[0][0] != scores1[1][0]) or len(scores1) == 1: # case1
        s, x, y = scores1[0]
        room[x][y] = std
        continue
    
    scores2 = []
    for i in range(len(scores1)):
        ms, x, y = scores1[i]
        
        score2 = 0
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if room[nx][ny] == 0:
                score2 += 1
        scores2.append((score2, x, y))
        
        if i == len(scores1)-1 or scores1[i][0] != scores1[i+1][0]:
            break
    scores2.sort(reverse = True)
    
    if scores2[0][0] != scores2[1][0]: # case2
        s, x, y = scores2[0]
        room[x][y] = std
        continue
    
    scores3 = []
    for i in range(len(scores2)):
        s, x, y = scores2[i]
        scores3.append((s,x,y))
        if i == len(scores2)-1 or s != scores2[i+1][0]:
            break
    scores3.sort(key = lambda x : (x[1], x[2]))
    s, x, y = scores3[0]
    room[x][y] = std
    
for x in range(n):
    for y in range(n):
        score = 0
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if room[nx][ny] in friends[room[x][y]]:
                score += 1
        if score == 0:
            result += 0
        elif score == 1:
            result += 1
        elif score == 2:
            result += 10
        elif score == 3:
            result += 100
        else:
            result += 1000
print(result)