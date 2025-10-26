# 백준 4195번 친구 네트워크

import sys

input = sys.stdin.readline

F = int(input().rstrip())

def find(friends, f):
    if friends[f][0] != f:
        p = friends[f][0] # f : f의 부모
        friends[f][0] = find(friends, p)
    return friends[f][0]
    
for _ in range(F):
    friends = dict()
    N = int(input().rstrip())
    for _ in range(N):
        f1, f2 = input().split()
        if f1 not in friends:
            friends[f1] = [f1, 1]
        if f2 not in friends:
            friends[f2] = [f2, 1]
        f1 = find(friends, f1)
        f2 = find(friends, f2)
        if f1 != f2:
            friends[f1][0] = f2
            friends[f2][1] += friends[f1][1]
        print(friends[f2][1])