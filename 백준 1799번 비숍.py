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
def white(N, chess, white_leftdiag, n, cnt, white_cnt):
    if n == N:
        white_cnt[0] = max(white_cnt[0], cnt)
        return
    flag = 1
    for i in range(-N//2, N//2+1):
        if (0<=n+i<N and 0<=n-i<N):
            if chess[n+i][n-i]:
                if white_leftdiag[i]:
                    continue
                white_leftdiag[i] = 1
                flag = 0
                white(N, chess, white_leftdiag, n+1, cnt+1, white_cnt)
                white_leftdiag[i] = 0
    if flag: white(N, chess, white_leftdiag, n+1, cnt, white_cnt)
    
def black(N, chess, black_leftdiag, n, cnt, black_cnt):
    if n == N:
        black_cnt[0] = max(black_cnt[0], cnt)
        return
    flag = 1
    for i in range(-N//2, N//2):
        if (0<=n+1+i<N and 0<=n-i<N):
            if chess[n+1+i][n-i]:
                if black_leftdiag[i]:
                    continue
                black_leftdiag[i] = 1
                flag = 0
                black(N, chess, black_leftdiag, n+1, cnt+1, black_cnt)
                black_leftdiag[i] = 0
    if flag: black(N, chess, black_leftdiag, n+1, cnt, black_cnt)

def solution(N, chess):
    white_cnt = [0] # call by reference는 mutable 자료형에 대해서만 가능하기 때문에 이렇게 해줌
    black_cnt = [0] # 위와 마찬가지로 call by reference를 위해 자료형을 리스트로 함.
    white_leftdiag = {i:0 for i in range(-N//2, N//2+1)}
    black_leftdiag = {i:0 for i in range(-N//2, N//2)}
    white(N, chess, white_leftdiag, 0, 0, white_cnt)
    black(N, chess, black_leftdiag, 0, 0, black_cnt)
    return white_cnt[0] + black_cnt[0]

print(solution(N, chess))