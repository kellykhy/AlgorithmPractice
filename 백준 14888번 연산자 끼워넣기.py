# 백준 14888번 연산자 끼워넣기 

import sys

# (덧셈, 뺄셈, 곱셈, 나눗셈) = (2, 1, 1, 1)
# (0 0 1 2 3), (0 1 2 3 0) ...

def backtracking(k):
    global result, max_result, min_result
    if k == N-1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for i in range(4):
        if cnts[i]:
            cnts[i] -= 1
            result_cpy = result
            if i == 0: # 덧셈
                result += A[k+1]
            elif i == 1: # 뺄셈
                result -= A[k+1]
            elif i == 2: # 곱셈
                result *= A[k+1]
            else: # 나눗셈
                tmp = abs(result) // abs(A[k+1])
                if result * A[k+1] > 0: result = tmp
                else: result = -tmp
            backtracking(k+1)
            result = result_cpy
            cnts[i] += 1
#input
N = int(input().rstrip())
A = list(map(int, input().split()))
cnts = list(map(int, input().split()))
# 연산자 순서 경우의 수 찾기 + 최대, 최소 구하기
max_result, min_result = -1e+9, 1e+9 # 십억
result = A[0]
backtracking(0)

print(int(max_result))
print(int(min_result))