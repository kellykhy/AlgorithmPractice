#백준 9372번 상근이의 여행

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) #국가의 수, 비행기 종류 수
    for i in range(M):
        route = list(map(int, input().split()))
    print(N-1)