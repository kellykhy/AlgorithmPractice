# 프로그래머스2019카카오 무지의 먹방 라이브
food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    t = 0
    cut = 0

    if (sum(food_times) <= k):
        return -1

    food_dict = {}
    length = len(food_times)
    for i in range(len(food_times)):
        food_dict[i+1] = food_times[i]

    food_dict = sorted(food_dict.items(), key= lambda x : x[1])
    while (food_dict[0][1] - cut) * length <= (k - t):
        t += (food_dict[0][1] - cut) * length
        cut = food_dict[0][1]
        del food_dict[0]
        length -= 1
        food_dict = sorted(food_dict, key= lambda x : x[1])

    food_dict = dict(food_dict)
    result = sorted(food_dict.items())
    answer = result[(k-t) % length][0]

    return answer

print(solution(food_times, k))