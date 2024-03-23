# 백준 1931번 회의실 배정

import sys
input = sys.stdin.readline

N = int(input())
timeline = []
for _ in range(N):
    timeline.append(list(map(int, input().split())))

timeline.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간이 같다면, 시작 시간이 빠른 순으로 정렬해야 함. (시작과 동시에 끝나는 회의 배정도 카운트 하기 위함)
finish = 0
result = 0
for i in range(N):
    if (i == 0):
        finish = timeline[i][1]
        result += 1
    else:
        if (timeline[i][0] >= finish):
            finish = timeline[i][1]
            result += 1
print(result)