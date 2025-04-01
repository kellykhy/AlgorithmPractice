# 백준 17140번 이차원 배열과 연산

import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())
arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

def csort(arr):
    count = dict()
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        if arr[i] not in count.keys():
            count[arr[i]] = 1
        else:
            count[arr[i]] += 1
    count = list(count.items())
    count.sort(key = lambda x : (x[1], x[0]))
    result = []
    for i in range(len(count)):
        result += count[i]
    return result

def flipped(arr):
    flipped_arr = []
    for j in range(len(arr[0])):
        row = []
        for i in range(len(arr)):
            row.append(arr[i][j])
        flipped_arr.append(row)
    return flipped_arr

def padding_zero(arr):
    max_r_len = 0
    for i in range(len(arr)):
        max_r_len = max(max_r_len, len(arr[i]))
    for i in range(len(arr)):
        for j in range(max_r_len - len(arr[i])):
            arr[i] += [0]
    return arr

def cal(arr, x):
    if x == 'C':
        arr = flipped(arr)
    for i in range(len(arr)):
        arr[i] = csort(arr[i])
    arr = padding_zero(arr)
    if x == 'C':
        arr = flipped(arr)
    return arr
        
flag = 0
for i in range(101):
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        print(i)
        flag = 1
        break
    R, C = len(arr), len(arr[0])
    if R >= C:
        arr = cal(arr, 'R')
    else:
        arr = cal(arr, 'C')
        
if not flag: print(-1)