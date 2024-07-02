# 백준 1700번 멀티탭 스케줄링 (미해결 - 아직은 테스트케이스 다 통과)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))
multitap = []
result = 0
        
for i in range(K):
    if order[i] in multitap:
        continue
    if (len(multitap) < N):
        multitap.append(order[i])
        continue
    
    toBeUsed = []
    for plug in multitap:
        if plug in order[i+1:]:
            toBeUsed.append(order[i+1:].index(plug))
        else:
            toBeUsed.append(101)
            
    plug_to_remove = toBeUsed.index(max(toBeUsed))
    multitap.remove(multitap[plug_to_remove])
    multitap.append(order[i])
    result += 1
    
print(result)