# 백준 11728번 배열 합치기 (again)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary1 = list(map(int, input().split())) # 이미 정렬되어 있음
ary2 = list(map(int, input().split())) # 이미 정렬되어 있음

result = []

p1, p2 = 0, 0
while (p1 < n or p2 < m):
    if (p1 == n):
        result.append(ary2[p2])
        p2 += 1
    elif (p2 == m):
        result.append(ary1[p1])
        p1 += 1
    else:
        if (ary1[p1] < ary2[p2]):
            result.append(ary1[p1])
            p1 += 1
        else:
            result.append(ary2[p2])
            p2 += 1
print(*result)
        
