# 백준 10816번 숫자 카드2

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def search_loweridx(target):
    l, r = 0, len(numbers)
    while (l < r):
        mid = (l + r) // 2
        if (numbers[mid] >= target): # 6 7 9 9 9 10  / 6 6 6 9 9 10
            r = mid
        else:
            l = mid + 1
    return l

def search_upperidx(target):
    l, r = 0, len(numbers)
    while (l < r):
        mid = (l + r) // 2
        if (numbers[mid] > target):
            r = mid
        else:
            l = mid + 1
    return l

numbers.sort()
for target in targets:
    print(search_upperidx(target)-search_loweridx(target), end = ' ')
