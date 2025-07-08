# 백준 1038번 감소하는 수

import sys
input = sys.stdin.readline

N = int(input())

cand = []
#  k: 맨 뒷자리, s: 현재까지 만든 수
used = [0 for _ in range(10)]
def backtracking(k,s):
    if s:
        cand.append(int(s))
        
    for i in range(k):
        if not used[i]:
            used[i] = 1
            backtracking(i, f'{s}{i}')
            used[i] = 0
    
backtracking(10, "")
cand.sort()
if len(cand) <= N: print(-1)
else: print(cand[N])