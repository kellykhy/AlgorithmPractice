# 백준 11728번 배열 합치기

# 투 포인터 사용 x
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ary = list(map(int, input().split())) + list(map(int, input().split()))

print(' '.join(list(map(str, sorted(ary)))))
'''

# 투 포인터 사용 o
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ary1 = list(map(int, input().split()))
ary2 = list(map(int, input().split()))
ans = []

p1 = 0
p2 = 0
while (p1 < n or p2 < m):
    if (p1 == n):
        ans += ary2[p2:] # 슬라이싱으로 for문 대체
        break
    if (p2 == m):
        ans += ary1[p1:] # 슬라이싱으로 for문 대체
        break
    if (ary1[p1] < ary2[p2]):
        ans.append(ary1[p1])
        p1 += 1
    else:
        ans.append(ary2[p2])
        p2 += 1
        
# 새로운 문법: Asterisk(*)로 리스트 압축해제
print(*ans) # 수정 전: print(' '.join(map(str, ans))) 