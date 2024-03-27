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
    
dp = deque([[0,0,0,0]]) # dp[n][i] : 합이 n이 되도록 하는 방법들 중 i로 시작하는 방법의 수 (n = 1,2,3)
for i in range(1, max+1):
    if i == 1:
        dp.append([0,1,0,0])
    elif i == 2:
        dp.append([0,0,1,0])
    elif i == 3:
        dp.append([0,1,1,1])
    else:
        dp.append([0, dp_sum[-1]-dp[-1][0], dp_sum[-2]-dp[-2][1], dp_sum[-3]-dp[-3][2]]) # 점화식
        dp.popleft() # 시간초과 및 메모리초과 이유로 pop(0)에서 수정함.
    dp_sum.append(sum(dp[-1]))
        
for i in case:
    print(dp_sum[i]%1000000009)
    
'''
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
    
dp = [[0,0,0,0]]
dp.append([0,1,0,0])
dp.append([0,0,1,0])
dp.append([0,1,1,1])

for i in range(4, max+1):
    dp.append([0,(sum(dp[-1])-dp[-1][1])%1000000009, (sum(dp[-2])-dp[-2][2])%1000000009, (sum(dp[-3])-dp[-3][3])%1000000009]) # 점화식
# 의문: 왜 여기서 %1000000009 를 생략하면 시간초과가 날까.

for i in case:
    print(sum(dp[i])%1000000009)
    
'''