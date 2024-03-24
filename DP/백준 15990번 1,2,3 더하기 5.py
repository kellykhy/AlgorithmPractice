# 백준 15990번 1,2,3 더하기 5
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
case = []
max = 0
for i in range(t):
    n = int(input())
    if max < n:
        max = n
    case.append(n)
    
dp_sum = [0]
    
dp = deque([[0,0,0]])
for i in range(1, max+1):
    if i == 1:
        dp.append([1,0,0])
    elif i == 2:
        dp.append([0,1,0])
    elif i == 3:
        dp.append([1,1,1])
    else:
        dp.append([dp_sum[-1]-dp[-1][0], dp_sum[-2]-dp[-2][1], dp_sum[-3]-dp[-3][2]])
        dp.popleft()
    dp_sum.append(sum(dp[-1]))
        
for i in case:
    print(dp_sum[i]%1000000009)