# 삼성SW역량테스트 2015 하반기 1번 문제 바이러스 검사

import sys
input = sys.stdin.readline

n = int(input())
customers = list(map(int, input().split()))
ldr, mbr = map(int, input().split())

total = 0
for i in range(n):
    res = 1
    if customers[i] >= ldr:
        customers[i] -= ldr
        res += customers[i] // mbr + 1 if customers[i] % mbr else customers[i] // mbr

    total += res
    
print(total)