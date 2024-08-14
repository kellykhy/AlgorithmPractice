# 백준 9996번 한국이 그리울 땐 서버에 접속하지

import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()
files = []
for _ in range(n):
    files.append(input().rstrip())

tmp = list(pattern.split('*'))
before = tmp[0]
after = tmp[1]

for file in files:
    flag = 0
    for i in range(len(before)):
        if before[i] == file[i]:
            continue
        else:
            flag = 1
            break
    if flag: 
        print("NE")
        continue
    for i in range(len(after)):
        if len(file)-i-1 == len(before)-1:
            flag = 1
            break
        if after[-i-1] == file[-i-1]:
            continue
        else:
            flag = 1
            break
    if flag:
        print("NE")
        continue
    print("DA")