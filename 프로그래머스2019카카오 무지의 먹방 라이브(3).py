# 프로그래머스2019카카오 무지의 먹방 라이브
food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    t = 0
    cut = 0

    if (sum(food_times) <= k):
        return -1

    dict = {}
    length = len(food_times)
    for i in range(len(food_times)):
        dict[i+1] = food_times[i]

    while (min(dict.values()) - cut) * length <= (k - t):
        min_val = min(dict.values())
        t += (min_val - cut) * length
        cut = min_val
        del dict[min(dict, key = dict.get)]
        length -= 1

    result = sorted(dict.items())
    answer = result[(k-t) % length][0]

    return answer

print(solution(food_times, k))