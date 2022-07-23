# 프로그래머스2019카카오 무지의 먹방 라이브(4)

from heapq import heappush, heappop

food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    t = 0
    cut = 0

    if (sum(food_times) <= k):
        return -1

    food_heap = []
    length = len(food_times)
    for i in range(len(food_times)):
        heappush(food_heap, [food_times[i], i+1])

    while (food_heap[0][0] - cut) * length <= (k - t):
        t += (food_heap[0][0] - cut) * length
        cut = food_heap[0][0]
        heappop(food_heap)
        length -= 1

    result = sorted(food_heap, key = lambda x : x[1])
    answer = food_heap[(k-t) % length][1]

    return answer

print(solution(food_times, k))