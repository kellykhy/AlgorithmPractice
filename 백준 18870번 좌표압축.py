#백준 18870번 좌표압축

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers_cpy = sorted(list(set(numbers)))

def bsearch(target): # numbers[index] = target인 index 중 가장 작은 것을 리턴
    st, en = 0, len(numbers_cpy)
    while (st < en):
        mid = (st + en) // 2
        if numbers_cpy[mid] < target:
            st = mid + 1
        else:
            en = mid
    return st

numbers_cpy.sort()
for n in numbers:
    print(bsearch(n), end = ' ')