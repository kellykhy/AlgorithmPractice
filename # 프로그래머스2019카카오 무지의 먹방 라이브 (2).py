# 프로그래머스2019카카오 무지의 먹방 라이브
food_times = [4,1,1,1,1,1]
k = 4
print("original food_times :", food_times)

def print_(t, food_times, zero_idx):
    print("food_times:", food_times)
    print("zero_dix:", zero_idx)
    print("t:", t)
    print()

def find_zero(food_times):
    lst = []
    for food in enumerate(food_times):
        if food[1] == 0:
            lst.append(food[0])
    return lst

def solution(food_times, k):
    zero_idx = []
    answer = 0
    t = 0
    if (sum(food_times) <= k):
        return -1

    while t <= k:
        if (len(food_times)-len(zero_idx)) <= k - t:
            change = [-1] * len(food_times)
            for i in zero_idx:
                change[i] = 0
            food_times = [food_times + change for food_times, change in zip(food_times, change)]
            t += (len(food_times) - len(zero_idx))
            zero_idx = find_zero(food_times)
            print_(t, food_times, zero_idx)
        else:
            for i in range(len(food_times)):
                if i not in zero_idx:
                    if food_times[i]:
                        food_times[i] -= 1
                        t += 1
                        print_(t, food_times, zero_idx)
                    if t == k+1:
                        answer = i + 1
                        return answer

print(solution(food_times, k))