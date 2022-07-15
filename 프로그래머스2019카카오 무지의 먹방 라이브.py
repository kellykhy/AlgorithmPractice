# 프로그래머스2019카카오 무지의 먹방 라이브
from collections import defaultdict

food_times = [1, 10, 10, 1, 1]
k = 5
print("original food_times :", food_times)

def next_idx(sec, food_dict, len): #다음에 섭취할 음식 반환
    food_idx = sec % len
    while (1):
        if food_idx in food_dict:
            return food_idx
        food_idx += 1
        food_idx %= len

def solution(food_times, k):
    food_dict = dict()
    food_dict_len = len(food_times)
    for i in range(len(food_times)):
        food_dict[i] = food_times[i]
    for s in range(k): ## s초
        idx = next_idx(s, food_dict, food_dict_len)
        food_dict[idx] -= 1
        if food_dict[idx] == 0:  # idx번째 음식 다 먹음.
            del food_dict[idx]
        if len(food_dict) == 0:  # k초가 되기 전에 섭취해야할 음식이 바닥남.
            return -1
        #print("%d초 %d번째 음식, food_dict:" %(s, idx), end = ' ')
        #print(food_dict)

    answer = next_idx(k, food_dict, food_dict_len) +1
    return answer

print(solution(food_times, k))