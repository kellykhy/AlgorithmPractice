# 백준 12015번 가장 긴 증가하는 부분 수열2

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 현재의 수보다 큰 가장 작은 수의 인덱스 찾기
def binary_search(n):
    st, en = 0, len(LIS)
    while st < en:
        mid = (st + en) // 2
        if LIS[mid] < A[i]:
            st = mid + 1
        else:
            en = mid
    return en

LIS = [A[0]]
for i in range(1, N):
    if  LIS[-1] < A[i]:
        LIS.append(A[i])
    else:
        LIS[binary_search(A[i])] = A[i]
print(len(LIS))