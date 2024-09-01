# 백준 16401번 과자 나눠주기

import sys
input = sys.stdin.readline

def lentocnt(unit):
    cnt = 0
    for snack_length in snack_lengths:
        cnt += snack_length // unit
    return cnt

m, n = map(int, input().split())
snack_lengths = list(map(int, input().split()))

l, r = 1, max(snack_lengths)
while (l <= r):
    mid = (l+r) // 2
    cnt = lentocnt(mid)
    if cnt >= m:
        l = mid + 1
    else:
        r = mid - 1
print(r)
