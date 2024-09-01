# 백준 1976번 여행 가자

import sys
input = sys.stdin.readline

def find(a):
    if (parent[a] == a):
        return a
    else:
        pa = find(parent[a])
        parent[a] = pa
        return pa
    
def union(a,b):
    parent[find(a)] = find(b)

n = int(input().rstrip())
m = int(input().rstrip())
parent = [i for i in range(n+1)]
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(i+1,n+1):
        if (row[j-1]):
           union(i,j)
schedule = list(set(map(int, input().split())))

flag = 0
for i in range(len(schedule) - 1):
    if find(schedule[i]) == find(schedule[i+1]):
        continue
    flag = 1
    break
if flag:
    print("NO")
else:
    print("YES")
