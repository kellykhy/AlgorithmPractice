# 프로그래머스2019카카오 무지의 먹방 라이브
food_times = [4,1,1,1,1,1]
k = 4

def solution(food_times, k):
    t = 0
    cut = 0

    dict = {}
    length = len(food_times)
    for i in range(len(food_times)):
        dict[i+1] = food_times[i]
    while (min(dict.values()) - cut) * length <= (k - t):
        t += (min(dict.values()) - cut) * length
        cut = min(dict.values())
        dict.delete(min(dict, key = dict.get))
        length -= 1
    result = sorted(dict.items())
    answer = result[(k-t) % length]

    return answer

print(solution(food_times, k))