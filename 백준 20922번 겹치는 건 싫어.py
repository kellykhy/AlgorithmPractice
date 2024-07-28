# 백준 20922번 겹치는 건 싫어

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ary = list(map(int, input().split()))

cnt = [0 for _ in range(max(ary)+1)]
result = 0
st = 0
for en in range(n):
    cnt[ary[en]] += 1
    while cnt[ary[en]] > k:
        cnt[ary[st]] -= 1
        st += 1
    result = max(result, en-st+1)
        
print(result)