# 백준 11728번 배열 합치기

import sys
input = sys.stdin.readline

'''
n,m = map(int, input().split())
ary = list(map(int, input().split())) + list(map(int, input().split()))

print(' '.join(list(map(str, sorted(ary)))))
'''

# 투 포인터 사용
n,m = map(int, input().split())
ary1 = list(map(int, input().split()))
ary2 = list(map(int, input().split()))
ans = []

ary1.sort()
ary2.sort()

p1 = 0
p2 = 0
while (p1 < n or p2 < m):
    if (p1 == n):
        while (p2 < m):
            ans.append(ary2[p2])
            p2 += 1
        break
    elif (p2 == m):
        while (p1 < n):
            ans.append(ary1[p1])
            p1 += 1
        break
    if (ary1[p1] < ary2[p2]):
        ans.append(ary1[p1])
        p1 += 1
    else:
        ans.append(ary2[p2])
        p2 += 1
print(' '.join(map(str, ans)))