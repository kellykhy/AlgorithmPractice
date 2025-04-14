# 백준 18808번 스티커 붙이기

import sys
from collections import deque
input = sys.stdin.readline

def rotate(sticker):
    R, C = len(sticker), len(sticker[0])
    rotation = [[0 for _ in range(R)] for _ in range(C)]
    for i in range(R):
        for j in range(C):
            rotation[j][R-i-1] = sticker[i][j]
    return rotation

def attach(sticker):
    global board
    R, C = len(sticker), len(sticker[0])

    upperleft = (0,0)
    for j in range(C):
        if sticker[0][j]:
            upperleft = (0, j)
            break
    for i in range(N):
        for j in range(M):
            cnt = 0
            new_board = [board[x][:] for x in range(N)]
            if board[i][j]: continue
            visited = [[0 for _ in range(C)] for _ in range(R)]
            queue = deque()
            
            si, sj = upperleft
            visited[si][sj] = 1
            queue.append((si, sj))
            new_board[i][j] = 1
            cnt += 1
            flag = 0
            while queue:
                si, sj = queue.popleft()
                for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nsi, nsj = si + di, sj + dj
                    if not (0 <= nsi < R and 0 <= nsj < C) or visited[nsi][nsj]: continue
                    if not sticker[nsi][nsj]: continue
                    visited[nsi][nsj] = 1
                    queue.append((nsi, nsj))
                    ni, nj = i+nsi-upperleft[0], j+nsj-upperleft[1]
                    if not (0 <= ni < N and 0 <= nj < M) or new_board[ni][nj]: 
                        flag = 1
                        break
                    new_board[ni][nj] = 1
                    cnt += 1
                if flag: 
                    break
            if not flag:
                board = new_board
                return cnt
    return 0


N, M, K = map(int, input().split()) # 노트북 크기 : N x M, 스티커 개수 : K
result = 0
board = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    # 스티커 정보
    R, C = map(int, input().split())
    sticker = [] # 스티커의 모눈종이
    for _ in range(R):
        sticker.append(list(map(int, input().split())))
    # 스티커 붙이기
    n = attach(sticker)
    for _ in range(3):
        if not n:
            sticker = rotate(sticker)
            n = attach(sticker)
        else:
            break
    result += n
print(result)