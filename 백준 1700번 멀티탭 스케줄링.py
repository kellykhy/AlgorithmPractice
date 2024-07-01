# 백준 1700번 멀티탭 스케줄링 (미해결 - 아직은 테스트케이스 다 통과)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))
currentMultitap = [0 for _ in range(K+1)]
result = 0

plugs = 0
for i in range(K):
    if plugs >= N:
        break
    if not currentMultitap[order[i]]:
        currentMultitap[order[i]] += 1
        plugs += 1
        
for i in range(N, K):
    if currentMultitap[order[i]]:
        continue
    elif (sum(currentMultitap) < N):
        currentMultitap[order[i]] += 1
        continue
    else:
        toBeUsed = []
        for j in range(i + 1, K):
            if order[j] in toBeUsed:
                continue
            if currentMultitap[order[j]] == 1:
                toBeUsed.append(order[j])
            if len(toBeUsed) == N - 1:
                break
        
        plug_to_remove = 1
        for plug in range(1, K+1):
            if (currentMultitap[plug] and plug not in toBeUsed):
                plug_to_remove = plug
                break
        currentMultitap[plug_to_remove] -= 1
        currentMultitap[order[i]] += 1
        result += 1    
    
print(result)