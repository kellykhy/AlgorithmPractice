# 백준 1799번 비숍
# 코드 참고) https://rapun7el.tistory.com/60
import sys
input = sys.stdin.readline

# input
N = int(input())
chess = []
for _ in range(N):
    row = list(map(int, input().split()))   
    chess.append(row)

# solution

def white(N, chess, white_leftdiag, n, cnt):
    global white_cnt
    if n == N:
        white_cnt = max(white_cnt, cnt)
        return
    flag = 1
    for i in range(-N//2, N//2+1):
        if (0<=n+i<N and 0<=n-i<N):
            if chess[n+i][n-i]:
                if white_leftdiag[i]:
                    continue
                white_leftdiag[i] = 1
                flag = 0
                white(N, chess, white_leftdiag, n+1, cnt+1)
                white_leftdiag[i] = 0
    if flag: white(N, chess, white_leftdiag, n+1, cnt)
    
def black(N, chess, black_leftdiag, n, cnt):
    global black_cnt
    if n == N:
        black_cnt = max(black_cnt, cnt)
        return
    flag = 1
    for i in range(-N//2, N//2):
        if (0<=n+1+i<N and 0<=n-i<N):
            if chess[n+1+i][n-i]:
                if black_leftdiag[i]:
                    continue
                black_leftdiag[i] = 1
                flag = 0
                black(N, chess, black_leftdiag, n+1, cnt+1)
                black_leftdiag[i] = 0
    if flag: black(N, chess, black_leftdiag, n+1, cnt)
    
def solution(N, chess):
    global white_cnt, black_cnt
    white_cnt = 0
    black_cnt = 0
    white_leftdiag = {i:0 for i in range(-N//2, N//2+1)}
    black_leftdiag = {i:0 for i in range(-N//2, N//2)}
    white(N, chess, white_leftdiag, 0, 0)
    black(N, chess, black_leftdiag, 0, 0)
    return white_cnt + black_cnt

print(solution(N, chess))