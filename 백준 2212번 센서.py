# 백준 2212번 센서

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
distances = []
for i in range(N-1):
    dis = sensors[i+1] - sensors[i]
    distances.append(dis)
distances.sort()
print(sum(distances[:N-K]))