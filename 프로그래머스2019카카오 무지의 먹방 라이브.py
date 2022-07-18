# 프로그래머스2019카카오 무지의 먹방 라이브
food_times = [3, 1, 2]
k = 5
print("original food_times :", food_times)

def next_idx(food_dict, len): #다음에 섭취할 음식 반환
    global n
    food_idx = n % len
    while (1):
        if food_idx in food_dict and food_dict[food_idx]:
            return food_idx
        n += 1
        print("n:", n)
        food_idx = n % len

def solution(food_times, k):
    global n
    n = 0
    food_dict = dict()
    food_dict_len = len(food_times)
    for i in range(len(food_times)):
        food_dict[i] = food_times[i]
    for sec in range(k): ## s초
        idx = next_idx(food_dict, food_dict_len)
        food_dict[idx] -= 1
        n += 1
        if sum(food_dict.values()) == 0:  # k초가 되기 전에 섭취해야할 음식이 바닥남.
            return -1
        print("%d초 %d번째 음식, food_dict:" %(sec, idx), end = ' ')
        print(food_dict)
        print("n:", n)

    answer = next_idx(food_dict, food_dict_len) +1
    return answer

print(solution(food_times, k))