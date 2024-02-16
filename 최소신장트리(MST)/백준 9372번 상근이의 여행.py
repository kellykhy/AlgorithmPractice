#백준 9372번 상근이의 여행

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) #국가의 수, 비행기 종류 수
    for _ in range(M):
        input()
    print(N-1)
