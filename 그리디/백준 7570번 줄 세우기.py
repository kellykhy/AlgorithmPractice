# 백준 7570번 줄 세우기

# idea: 안움직여도 되는 것의 개수의 최댓값은 = 연속된 숫자(오름차순)의 최대길이
# n - (연속된 수의 최대길이)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
kids = list(map(int, input().split()))
idx = [0 for _ in range(n+1)]
for i in range(n):
    idx[kids[i]] = i

length = 1
max_length = 1
for i in range(2,n+1):
    if idx[i-1] < idx[i]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
print(n-max_length)
