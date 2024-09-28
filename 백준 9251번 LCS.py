# 백준 9251번 LCS

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

table = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            table[i][j] = 1
        if i == 0 and j == 0: continue
        if i == 0:
            table[i][j] = max(table[i][j], table[i][j-1])
        elif j == 0:
            table[i][j] = max(table[i][j], table[i-1][j])
        else:
            table[i][j] = max(table[i][j]+table[i-1][j-1], table[i-1][j], table[i][j-1])
print(table[len(str1)-1][len(str2)-1])