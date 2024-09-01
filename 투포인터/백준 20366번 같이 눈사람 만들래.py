# 백준 20366번 같이 눈사람 만들래?

import sys
input = sys.stdin.readline

n = int(input())
balls = list(map(int, input().split()))
INF = 1e+9

balls.sort()
zero = 0
total_min_d = INF
for i in range(1, n-1):
    for j in range(i+1, n-1):
        base = balls[i] + balls[j]
        min_d = INF
        st, en = i-1, j+1
        while (st >= 0 and en < n):
            cmp = balls[st] + balls[en]
            min_d = min(min_d, abs(base - cmp))
            if (base > cmp):
                en += 1
            elif (base < cmp):
                st -= 1
            else:
                total_min_d = 0
                zero = 1
                break
        if zero:
            break
        total_min_d = min(total_min_d, min_d)
    if zero:
        break
    
print(total_min_d)
