# 백준 2295번 세 수의 합

import sys
input = sys.stdin.readline

def bsearch2(target):
    st, en = 0, len(two_sum)
    while (st < en):
        mid = (st + en) // 2
        if (two_sum[mid] < target):
            st = mid + 1
        elif (two_sum[mid] > target):
            en = mid
        else:
            return 1
    return 0

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()

two_sum = []
for i in range(n):
    for j in range(i, n):
        if (numbers[i] + numbers[j] > numbers[-1]): break
        two_sum.append(numbers[i] + numbers[j])
two_sum.sort()

flag = 0
for i in range(n-1, -1, -1):
    for j in range(i):
        if (bsearch2(numbers[i]-numbers[j])):
            print(numbers[i])
            flag = 1
            break
    if flag:
        break