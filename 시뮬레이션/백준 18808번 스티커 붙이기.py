# 백준 18808번 스티커 붙이기

import sys
input = sys.stdin.readline

# 90도 회전
def rotate(sticker_size, sticker):
    n, m = sticker_size[0], sticker_size[1]
    new_sticker = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_sticker[j].insert(0,sticker[i][j])
    return new_sticker

# 노트북에 스티커 붙이기
def attach(sticker_size, sticker):
    global notebook
    global answer
    n, m = sticker_size[0], sticker_size[1]
    for i in range(N-n+1):
        for j in range(M-m+1):
            flag = 0
            tmp = 0
            notebook_copy = [item[:] for item in notebook]
            for si in range(n):
                for sj in range(m):
                    if (sticker[si][sj] == 1):
                        if (notebook_copy[i+si][j+sj] == 1):
                            flag = 1
                            break                        
                        else:
                            tmp += 1
                            notebook_copy[i+si][j+sj] = 1
                    if (si == n-1 and sj == m-1):
                        answer += tmp
                        notebook = notebook_copy
                        return True
                if (flag == 1):
                    break
    return False

N,M,K = map(int, input().split())
notebook = [[0]*M for _ in range(N)]
answer = 0

for _ in range(K):
    n,m = map(int, input().split())
    sticker_size = [n,m]
    sticker = [list(map(int, input().split())) for _ in range(n)]    
    if (max(sticker_size) > max(N,M)):
            continue
    for _ in range(4):
        if (attach(sticker_size, sticker) == True):
            break
        else:
            sticker = rotate(sticker_size, sticker)
            sticker_size = list(reversed(sticker_size))
print(answer)