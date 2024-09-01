# 백준 1920번 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def bsearch(target):
    l, r = 0, len(numbers)-1
    while (l <= r):
        if (numbers[l] == target or numbers[r] == target):
            return 1
        mid = (l + r) // 2
        if (numbers[mid] == target):
            return 1
        elif (numbers[mid] < target):
            l = mid + 1
        else:
            r = mid - 1
    return 0

numbers.sort() # O(nlgn)
for target in targets:
    print(bsearch(target)) # O(lgn)
    
# 최종적인 시간복잡도: O(nlgn) + O(mlgn)
