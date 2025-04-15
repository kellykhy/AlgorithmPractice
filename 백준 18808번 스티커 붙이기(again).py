# 백준 18808번 스티커 붙이기 (again)

import sys
input = sys.stdin.readline

# input
N, M, K = map(int, input().split())
notebook = [[0 for _ in range(M)] for _ in range(N)]
sticker = []
for _ in range(K):
    s = []
    SN, SM = map(int, input().split())
    for _ in range(SN):
        s.append(list(map(int, input().split())))
    sticker.append(s)
result = 0

# 노트북의 (i,j) 위치에 스티커를 붙일 수 있는가
def check(i, j, s):
    for si in range(len(s)):
        for sj in range(len(s[0])):
            if s[si][sj] and notebook[i+si][j+sj]:
                return 0
    return 1
    
def rotate(s):
    rot = [[0 for _ in range(len(s))] for _ in range(len(s[0]))]
    for i in range(len(s)):
        for j in range(len(s[0])):
            rot[j][len(s)-i-1] = s[i][j]
    return rot

def attach(s, i, j):
    for si in range(len(s)):
        for sj in range(len(s[0])):
            if s[si][sj]:
                notebook[i+si][j+sj] = 1
                
def count():
    result = 0
    for i in range(N):
        for j in range(M):
            if notebook[i][j] == 1:
                result += 1
    return result
     
def round(k):
    global result
    if k == K:
        result = count()
        return
    s = sticker[k]
    for r in range(4):
        for i in range(N-len(s)+1):
            for j in range(M-len(s[0])+1):
                if check(i, j, s):
                    attach(s, i, j)
                    round(k+1)
                    return
        if r == 3: break
        s = rotate(s)
    round(k+1)
    
round(0)
print(result)