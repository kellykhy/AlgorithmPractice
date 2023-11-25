# 프로그래머스2023카카오테크인턴십
# 1. 프로그래밍


friends = ["a", "b", "c"]
#gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]



from itertools import combinations

def solution(friends, gifts):
    num_map = [i for i in range(len(friends))]
    mapping = dict(zip(friends, num_map))

    pair_dict = {}
    give_count = [0 for i in range(len(friends))]
    take_count = [0 for i in range(len(friends))]
    count = [0 for i in range(len(friends))]
    for gift in gifts:
        gift_list = gift.split()
        sorted_gift = ' '.join(sorted(gift_list))
        if (sorted_gift not in list(pair_dict.keys())):
            pair_dict[sorted_gift] = 0
        if (gift != sorted_gift):
            pair_dict[sorted_gift] -= 1
        else:
            pair_dict[sorted_gift] += 1
        give_count[mapping[gift_list[0]]] += 1
        take_count[mapping[gift_list[1]]] += 1

    combination = []
    for c in combinations(friends, 2):
        combination.append(' '.join(sorted(list(c))))

    for pair in combination:
        a = pair.split(' ')[0]
        b = pair.split(' ')[1]
        if (pair not in list(pair_dict.keys()) or pair_dict[pair] == 0):
            diff = (give_count[mapping[a]] - take_count[mapping[a]]) - (give_count[mapping[b]] - take_count[mapping[b]])
            if (diff > 0):
                count[mapping[a]] += 1
            elif (diff < 0):
                count[mapping[b]] += 1
        elif (pair_dict[pair] > 0):
            count[mapping[a]] += 1
        else:
            count[mapping[b]] += 1
    return max(count)

print(solution(friends, gifts))