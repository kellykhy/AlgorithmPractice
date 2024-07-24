# 백준 1654번 랜선 자르기

import sys
input = sys.stdin.readline

def lan_count(length):
    result = 0
    for lan in lans:
        result += (lan // length)
    return result

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
lans.sort()

st, en = 1, lans[-1]

while (st < en):
    mid = (st + en + 1) // 2
    cnt = lan_count(mid)
    if (cnt >= n):
        st = mid
    elif (cnt < n):
        en = mid - 1
        
print(st)