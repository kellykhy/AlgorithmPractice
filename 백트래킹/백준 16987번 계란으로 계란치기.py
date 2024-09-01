# 백준 16987번 계란으로 계란치기

import sys
input = sys.stdin.readline

n = int(input())
eggs = []
result = 0
for i in range(n):
	eggs.append(list(map(int, input().split())))
 
def backtracking(k): # k : 계란 깬 횟수
    global cnt, result
    if k == n:
        result = max(result, cnt)
        return
    if eggs[k][0] > 0:
        hit = 0
        for i in range(n):
            if i == k:
                continue
            if eggs[i][0] <= 0:
                continue
            hit = 1
            flag1, flag2 = 0, 0
            eggs[k][0] -= eggs[i][1]
            eggs[i][0] -= eggs[k][1]
            if eggs[k][0] <= 0:
                flag1 = 1
                cnt += 1
            if eggs[i][0] <= 0:
                flag2 = 1
                cnt += 1
            backtracking(k+1)
            eggs[k][0] += eggs[i][1]
            eggs[i][0] += eggs[k][1]
            if flag1:
                cnt -= 1
            if flag2:
                cnt -= 1
        if not hit:
            backtracking(k+1)
    else:
        backtracking(k+1)
        
cnt = 0
backtracking(0)		
print(result)
