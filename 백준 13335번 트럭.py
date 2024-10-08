# 백준 13335번 트럭

import sys
from collections import deque

input = sys.stdin.readline
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

def solution(n, w, l, trucks):
    bridge = deque()
    for _ in range(w): 
        bridge.append(0)
    
    bridge_weight = 0
    t = 0
    while (trucks or bridge_weight):
        bridge_weight -= bridge.popleft()
        
        available = l - bridge_weight
        if trucks and trucks[0] <= available:
            weight = trucks.pop(0)
            bridge_weight += weight
            bridge.append(weight)
        else:
            bridge.append(0)

        t += 1
    return t

print(solution(n, w, l, trucks))