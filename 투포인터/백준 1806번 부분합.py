# 백준 1806번 부분합

import sys
input = sys.stdin.readline
N, S = map(int, input().split())
ary = list(map(int, input().split()))

pt1, pt2 = 0, 0
sum = ary[pt1]
ans = int(1e5) + 1
flag = 0

length = 1
flag = 0
while (pt1 <= pt2):
    while (sum < S):
        pt2 += 1
        length += 1
        if (pt2 == N): 
            flag = 1
            break
        sum += ary[pt2]
    if (flag == 1):
        break
    if (sum >= S):
        ans = min(ans, length)
    sum -= ary[pt1]
    length -= 1
    pt1 += 1
    
print(ans if ans != int(1e5) + 1 else 0)

'''

# 다른 풀이 참고
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
ary = list(map(int, input().split()))

pt1, pt2 = 0, 0
sum = ary[pt1]
ans = int(1e5) + 1

length = 1
while True:
    if (sum < S):
        pt2 += 1
        length += 1
        if (pt2 == N): break
        sum += ary[pt2]
    else:
        ans = min(ans, length)
        sum -= ary[pt1]
        length -= 1
        pt1 += 1
print(ans if ans != int(1e5) + 1 else 0)
'''