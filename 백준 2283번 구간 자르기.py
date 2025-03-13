# 백준 2283번 구간 자르기

import sys
input = sys.stdin.readline

max_value = 1000000
N, K = map(int, input().split())

## 누적합 구하는 부분 (중요)
arr = [0] * (max_value+2) # 0 ~ 1000001
for _ in range(N):
    s, e = map(int, input().split())
    arr[s+1] += 1
    arr[e+1] -= 1
    
for i in range(1,1000002):
    arr[i] += arr[i-1]

##
s, e = 0, 0
flag = False
value = 0
while (s <= e <= max_value):
    if value < K:
        e += 1
        value += arr[e]
    elif value > K:
        s += 1
        value -= arr[s]
    else:
        flag = True
        break
if flag:
    print(s, e)
else:
    print("0 0")