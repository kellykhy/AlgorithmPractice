# 백준 2751번 수 정렬하기2
# Merge Sort로 구현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
ary = []

for _ in range(N):
    ary.append(int(input()))
    
# 두 정렬된 배열 합치기
def merge(st, end):
    tmp = []
    mid = (st + end)//2
    lidx = st
    ridx = mid
    while (lidx < mid or ridx < end):
        if (lidx == mid): 
            tmp.append(ary[ridx])
            ridx += 1
        elif (ridx == end): 
            tmp.append(ary[lidx])
            lidx += 1
        elif (ary[lidx] < ary[ridx]): 
            tmp.append(ary[lidx])
            lidx += 1
        else: 
            tmp.append(ary[ridx])
            ridx += 1
            
    for i in range(len(tmp)):
        ary[st+i] = tmp[i]
    
def merge_sort(st, end):
    if end <= st+1: 
        return
    mid = (st + end)//2 # 2
    merge_sort(st, mid) # 0 2 -> 0 1, 1 2
    merge_sort(mid, end) # 2 5 -> 2 3, 3 5
    merge(st, end)

merge_sort(0, N)
print(*ary)
